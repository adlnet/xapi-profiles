
Part Three:	[xAPI Profiles Communication and Processing Specification](./xapi-profiles-communication.md#partthree)  
    * 1.0. [Profile Server](./xapi-profiles-communication#1.0)
    * 2.0. [Algorithms](./xapi-profiles-communication#2.0)
        * 2.1. [Statement Template Validation](./xapi-profiles-communication#2.1)
        * 2.2. [Pattern Validation](./xapi-profiles-communication#2.2)
   * 3.0. [Libraries](./xapi-profiles-communication#3.0)


<a name="partthree"></a>
# Part Three: Communication and Processing

In addition to the ability to host profiles as documents, there will be infrastructure for querying and manipulating profiles. This document describes the algorithms for processing profiles, including the exact rules by which Statement Templates and Patterns are validated against Statements. It also describes a “Profile Server” to make it easier to manage and answer questions about profiles from a centralized location, including implementing the algorithms.

## <a name="1.0">1.0</a> Profile Server

A Profile Server will
* allow administrators to add profiles by their contents or by URI to the Profile Server
* provide a review process people desiring to add profiles can submit to.

The review process will check profiles for following the specification and assist in helping them be of highest quality, after which they will be added to the server.

A Profile Server will host a SPARQL endpoint containing the RDF information from the contained profiles at the path /SPARQL. SPARQL servers have the ability to divide information into multiple datasets, or graphs, and offer separate querying on them. One of these is the default graph, which is queried when no other graph is specified. The default graph at this SPARQL endpoint will contain all the current versions of profiles. Additionally, every profile version will be in a Named Graph with a URI equal to the profile version's URI. Thus, by default queries will only operate on up to date information, but if historical profile information is needed, it is available.


### <a name="1.1">1.1</a> Example SPARQL Queries

Here are a selection of questions and the SPARQL queries that answer them, for retrieving commonly needed information from the server. All these SPARQL queries can also be run locally by loading one or more profiles into an RDF library and running SPARQL queries against them directly, with minor modifications depending on how the data is loaded.


“What profiles are on the server?”

```
select
    ?profile,
    ?name,
    ?definition
where {
    ?profile a :Profile ;
             :name ?name ;
             :definition ?definition .
}
```

Depending on some modeling choices, it may be necessary to add a line that prevents retrieving the versions as well.

“What verbs and activity types does this profile describe?”


```
select
    ?name,
    ?definition
where {
    (?concept a :Verb || ?concept a ActivityType) .                
    ?concept :inScheme <profileid> ;
             :name ?name ;
             :definition ?definition .
}
```


“What statement templates are available in this profile?”, “What patterns are available in this profile?”

Virtually identical to the above, just replace being a Verb or Activity Type with templates or patterns. We're able to use inScheme because the server includes semantic metadata letting it know that being a template, being a concept, and being a pattern are all forms of being inScheme, which is a general inclusion operator.

(Prefixes are omitted in these examples until a complete context is ready).

## <a name="2.0">2.0</a> Algorithms

This section specifies two primary algorithms. The first, given a Statement and a set of Statement Templates, validates the Statement against all applicable Statement Templates in those provided and returns the templates that match, or an error if any of the matching templates does not validate against the Statement. The second, given a collection of Statements and a set of Patterns, validates if the Statements follows any of the Patterns.


### <a name="2.1">2.1</a> Statement Template Validation

To validate a Statement against the Statement Templates of a Profile, call the `validates` function described in pseudocode below with the Statement and all the Statement Templates from the Profile. This function returns an outcome and an array of templates. To interpret the results, consult the table after the algorithm definition.

```
function validates(statement, templates):
    matching_templates = []
    failing_templates = []
    outcome = success
    for template in templates:
        if matches_determining_properties(statement, template):
            if follows_rules(statement, template):
                matching_templates.append(template.id)
            else:
                outcome = invalid
                failing_templates.append(template.id)
    if outcome is success:
        if length of matching_templates > 0:
            return success, matching_templates
        else:
            return unmatched, []
    else:
        return invalid, failing_templates


function follows_rules(statement, template):
    if template.objectStatementRefTemplate is specified:
        if statement.object is a StatementRef:
            if a Statement with id == statement.object.id is available to the checking system:
                if validates(that other statement, templates)[1] does not intersect with template.objectStatementRefTemplate:
                    return false
        else:
            return false
    if template.contextStatementRefTemplate is specified:
        if statement.context.statement is a StatementRef:
            if a Statement with id == statement.context.statement.id is available to the checking system:
                if validates(that other statement, templates)[1] does not intersect with template.contextStatementRefTemplate:
                    return false
        else:
            return false
    for rule in template.rules:
        if follows_rule(statement, rule):
            continue
        else:
            return false
    return true


function matches_determining_properties(statement, template):
    for each specified Determining Property in the template:
        if the corresponding Statement locations equal or are a superset of that Determining Properties values:
            continue
        else:
            return false
    return true


function follows_rule(statement, rule):
    strict = true
    values = apply_jsonpath(statement, rule.location)
    if rule.selector:
        originals = values
        values = []
        for value in originals:
            selection = apply_jsonpath(value, rule.selector)
            if selection is empty:
                values.append(UNMATCHABLE)
            else:
                values = values concatenated with selection
    if rule.presence is specified:
        if rule.presence is "included":
            if values contains UNMATCHABLE:
                return false
            if values is empty:
                return false
        if rule.presence is "excluded":
            if values is not empty and any members are not UNMATCHABLE:
                return false
        if rule.presence is "recommended":
            strict = false
    if rule.any is specified:
        if strict or values is not empty:
            if values does not intersect with rule.any:
                return false
    if rule.all is specified:
        if strict or values is not empty:
            if values contains UNMATCHABLE:
                return false
            for value in values:
                if rule.all does not contain value:
                    return false
    if rule.none is specified:
        if strict or values is not empty:
            for value in values:
                if rule.none contains value:
                    return false


function apply_jsonpath(statement, path):
    The definition of this is beyond the scope of this document, but it follows
    the JSONPath specification as constrained by the requirements in this
    specification. If a single value is found in the Statement matching the
    path, it is returned in an array (even if the single value is already an array). If
    multiple values are found, they are returned in an array.
    If no values are found, an empty array is returned.
```

This table summarizes the possible return values of `validates` and what they indicate.

outcome   | templates | outcome
--------- | --------- | -------
success   | non empty | one or more templates matched and all their rules are followed. The templates array contains all matched templates.
invalid   | non empty | one or more templates matched but not all their rules were followed. The templates array contains all templates that matched but had some rules unfollowed.
unmatched | empty     | none of templates matched


### <a name="2.2">2.2</a> Pattern Validation

To validate a series of Statements sharing a registration (and, if applicable, subregistration) follows a specified Profile, apply the `follows` algorithm described below, which returns simple success or failure. For more nuanced interpretation, examine the `matches` algorithm, which is used by `follows`. A table for interpreting the return values of the `matches` algorithm is provided following the pseudocode for the algorithms.

```

function follows(statements, templates, patterns):
    for statement in statements:
        outcome, templates = validates(statement, templates)
        if outcome is not success:
            return failure
        statement.templates = templates
    for pattern in patterns:
        outcome, remaining = matches(statements, pattern)
        if outcome is success and remaining is empty:
            return success
    return failure

function matches(statements, element):
    if element is a template:
        if statements is empty:
            return partial, []
        if statements[0].templates includes element:
            return success, statements[1:]
        else:
            return failure, statements
    else if element is a sequence:
        next statements = statements
        for next element in element.sequence:
            next matches, next statements = matches(next statements, next element)
            if next matches is failure:
                return failure, statements
            if next matches is partial:
                return partial, []
        return success, next statements
    else if element is a alternates:
        next matches, next statements = failure, statements
        for next element in element.alternates:
            maybe matches, maybe statements = matches(statements, next element)
            if maybe matches is success:
                next matches = success
                if maybe statements is shorter than next statements:
                    next statements = maybe statements
            if maybe matches is partial and next matches is failure:
                next_matches = partial
        if next_matches is partial:
            return partial, []
        return next matches, next statements
    else if element is a oneOrMore:
        next matches = failure
        last statements = next statements = statements
        while true:
            continue, next statements = matches(last statements, element.oneOrMore)
            if continue is success:
                next matches = success
            else if next matches is failure and continue is partial:
                return partial, []
            else:
                if continue is partial and last statements is not empty:
                    return partial, last statements
                return next matches, last statements
            if next statements is the same size as last statements:
                return success, next statements
            last statements = next statements
    else if element is a zeroOrMore:
        last statements = statements
        while true:
            continue, statements = matches(last statements, element.zeroOrMore)
            if continue is failure:
                return success, last statements
            if continue is partial and statements is not empty:
                return partial, statements
            if statements is the same size as last statements:
                return success, statements
            last statements = statements
    else if element is a optional:
        if statements is empty:
            return success, []
        next matches, next statements = matches(statements, element.optional)
        if next matches is success or partial:
            return next matches, next statements
        else:
            return success, statements
```

This table summarizes the possible return values of `matches` and what they indicate:

outcome | remaining statements | outcome
------- | -------------------- | -------
success | empty                | pattern validates for these statements
success | non empty            | pattern matches some of the statements, but not all
partial | empty                | pattern was in the middle of matching and ran out of statements
partial | non empty            | outcome could be interpreted as success with non empty remaining, but pattern could also continue matching
failure | original statements  | pattern failed to match statements. Note: if an optional or zeroOrMore pattern is directly inside an alternates pattern, it is possible for failure to be returned when partial is correct, due to decidability issues.


A pattern only matches if it matches greedily. That is, each optional, zeroOrMore, oneOrMore, and alternate pattern MUST always be considered to match the maximum length possible before considering any patterns later in a sequence. No backtracking is allowed. This constrains useful statement patterns, but guarantees efficient processing, as once a statement is matched it does not need to be reconsidered (except in cases where it is part of an ultimately unmatched alternate).
When checking previously collected statements for matching a pattern, ordering MUST be based on timestamp. In the event two or more statements have identical timestamps, any order within those statements is allowed.
When checking statements for matching a pattern upon receipt, ordering MUST be based on receipt order insofar as that can be determined. If statements are received in the same batch and they are being checked upon receipt, within the batch statements MUST be ordered first by timestamp, and if timestamps are the same, by order within the statement array, with lower indices earlier.


## <a name="3.0">3.0</a> Libraries

Any library that implements the algorithms given here, exposing all of the listed functions, will be an xAPI Profile Processor library.

For each of the `validates`, and `follows`, the Profile Server will provide web APIs that are strongly Not Recommended for production usage, but are suitable for experimentation and demonstration.

Their URL paths will be /validate_templates and /validate_patterns, respectively. The first will take a single xAPI statement and a profile specified by id, specified in POST variables as “statement” and “profile”. The second will take an array of xAPI statements and a profile specified by id, both specified in POST variables as “statements” and “profile”.

Both will perform the algorithms above and return 204 on successful validation and 400 on failure, with descriptive comments attached on failure.
