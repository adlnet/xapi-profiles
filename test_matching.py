import uuid

from itertools import chain
from string import printable, ascii_uppercase
from pprint import pprint
from hypothesis import given, settings
from hypothesis.strategies import data, integers, lists, recursive, uuids, sampled_from, tuples, just, one_of


# first, install the dependencies with `pip install -r requirements.txt`
# then, run this file by running `py.test` in the same directory

# This section is the matching algorithm from the spec, written in python

template = (uuid.UUID, basestring)
success = True
failure = False
partial = None

def matches(statements, element):
    if isinstance(element, template):
        if len(statements) == 0:
            return partial, []
        if statements[0] == element:
            return success, statements[1:]
        else:
            return failure, statements
    elif 'sequence' in element:
        next_statements = statements
        for next_element in element[1]:
            next_matches, next_statements = matches(next_statements, next_element)
            if next_matches is failure:
                return next_matches, statements
            if next_matches is partial:
                return partial, []
        return success, next_statements
    elif 'alternates' in element:
        next_matches, next_statements = failure, statements
        for next_element in element[1]:
            maybe_matches, maybe_statements = matches(statements, next_element)
            if maybe_matches is success:
                next_matches = success
                if len(maybe_statements) < len(next_statements):
                    next_statements = maybe_statements
            if maybe_matches is partial and next_matches is failure:
                next_matches = partial
        if next_matches is partial:
            return partial, []
        return next_matches, next_statements
    elif 'oneOrMore' in element:
        next_matches = failure
        last_statements = next_statements = statements
        while True:
            cont, next_statements = matches(last_statements, element[1])
            if cont is success:
                next_matches = success
            elif next_matches is failure and cont is partial:
                return partial, []
            else:
                if cont is partial and len(last_statements) > 0:
                    return partial, last_statements
                return next_matches, last_statements
            if len(next_statements) == len(last_statements):
                return success, next_statements
            last_statements = next_statements
    elif 'zeroOrMore' in element:
        last_statements = statements
        while True:
            cont, statements = matches(last_statements, element[1])
            if cont is failure:
                return success, last_statements
            elif cont is partial and len(last_statements) > 0:
                return partial, last_statements
            if len(statements) == len(last_statements):
                return success, statements
            last_statements = statements
    elif 'optional' in element:
        if len(statements) == 0:
            return success, []
        next_matches, next_statements = matches(statements, element[1])
        if next_matches in [success, partial]:
            return next_matches, next_statements
        else:
            return success, statements
    else:
        raise Exception("not possible")



# This section is the generative code for validating invariants
# we require patterns to have. For example, one of the tests
# validates that, if we generate a random pattern, then use it to generate
# a set of statements, the statements should match the pattern.
# Another tests that, if we follow the same procedure as above but truncate
# the statements to a random length, then we should either successfully
# or partially match.


# various helpers

def seq(*values):
    return "sequence", values

def alt(*values):
    return "alternates", values

def star(value):
    return "zeroOrMore", value

def plus(value):
    return "oneOrMore", value

def opt(value):
    return "optional", value




# This uses UUIDs in the patterns because, since UUIDs have no duplicates,
# greedily undecidable patterns can't be created, while still
# validating all the pattern-related logic.

# Of course, there will be real-world patterns with repeated templates/atoms,
# but only greedily decidable ones are good ideas. There's no easy way
# to generate those that I've found yet, so the generative tests all use
# UUIDs.


prefix_pattern = recursive(uuids(),  # our atoms
    lambda el: ( # el is generator making either atoms or previously generated
        # pieces.
        # for a new piece we generate a sequence/alternatives with at least
        # 2 members, or a oneOrMore/zeroOrMore/optional with one member
        (
            tuples(
                just(seq), lists(el, min_size=2)
            ) | tuples(
                just(alt), lists(
                    # we disallow optional and zeroOrMore directly inside
                    # alternates, as that can mean truncating statements does
                    # not lead to matchability.
                    el.filter(
                        lambda e: isinstance(e, template) or e[0] not in ["optional", "zeroOrMore"]
                ), min_size=2)
            )
        ).map(
            lambda (func, els): func(*els)
        ) | tuples(
                sampled_from((plus, opt, star)),
                el).map(
            lambda (func, els): func(els))
        )
    ).filter(lambda p: isinstance(p, tuple)) # patterns can't be just an atom


# the only difference with prefix_pattern is not having the structures that
# make truncation sometimes return false
matching_pattern = recursive(uuids(),
    lambda el: (
        (
            tuples(
                just(seq), lists(el, min_size=2)
            ) | tuples(
                just(alt), lists(el, min_size=2)  # filtering removed
            )
        ).map(
            lambda (func, els): func(*els)
        ) | tuples(
                sampled_from((plus, opt, star)),
                el).map(
            lambda (func, els): func(els))
        )
    ).filter(lambda p: isinstance(p, tuple))

# this is  for flattening 'statements' out into a single unnested list
def unpack_list(items):
    return chain.from_iterable(item if isinstance(item, list) else [item] for item in items)

# this transforms a particular pattern into a generator for statements
def pattern_to_statements(pattern):
    if isinstance(pattern, template):
        return lists(just(pattern), min_size=1, max_size=1)
    rule, value = pattern
    if rule == 'sequence':
        return tuples(*map(pattern_to_statements, value)).map(unpack_list).map(list)
    elif rule == 'alternates':
        return one_of(*map(pattern_to_statements, value))
    elif rule == 'zeroOrMore':
        return lists(pattern_to_statements(value)).map(unpack_list).map(list)
    elif rule == 'oneOrMore':
        return lists(pattern_to_statements(value), min_size=1).map(unpack_list).map(list)
    elif rule == 'optional':
        return lists(pattern_to_statements(value), min_size=0, max_size=1).map(unpack_list).map(list)
    else:
        raise Exception("impossible!", rule)



# this replicates the current scorm pattern, a realistic example of medium
# complexity. Note it has repeated elements, just not in ambiguous ways.
scorm_pattern = seq(
    "initialization",
    star(alt("scoactivity", "otheractivity", "commenting", "interactionactivity", "completing")),
    star(seq(
        "suspension",
        "resumption",
        star(alt("scoactivity", "otheractivity", "commenting", "interactionactivity", "completing"))
    )),
    "termination"
)

@given(pattern_to_statements(scorm_pattern))
def test_scormlike_example(statements):
    works, unhandled = matches(statements, scorm_pattern)
    assert works is success
    assert len(unhandled) == 0


def test_partial_success_hybrid():
    pattern = plus(seq("a", "b"))
    statements = ["a", "b", "a"]
    works, unhandled = matches(statements, pattern)
    assert works is partial
    assert unhandled == ["a"]

def test_simple_partial():
    statements = ["a", "b"]
    pattern = seq("a", "b", "c")
    works, unhandled = matches(statements, pattern)
    assert works is partial
    assert len(unhandled) == 0

@given(data(), prefix_pattern.flatmap(lambda p: tuples(just(p), pattern_to_statements(p))))
def test_prefix_complex(data, stuff):
    pattern, statements = stuff
    quantity = data.draw(integers(min_value=0, max_value=max(0, len(statements) - 1)))
    statements = statements[:quantity]

    works, unhandled = matches(statements, pattern)
    assert works in [partial, success]

@given(matching_pattern.flatmap(lambda p: tuples(just(p), pattern_to_statements(p))))
def test_patterns(stuff):
    pattern, statements = stuff
    works, unhandled = matches(statements, pattern)
    assert works is success
    assert len(unhandled) == 0
