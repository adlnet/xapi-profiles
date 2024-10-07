# xAPI Profiles

* Part One: [About xAPI Profiles](./xapi-profiles-about.md#part-one)
   *  1.0. [Introduction](./xapi-profiles-about.md#introduction)
   *  2.0. [How to Use This Document](./xapi-profiles-about.md#how-to-use-this-doc)
      *  2.1. [MUST / SHOULD / MAY](./xapi-profiles-about.md#def-must-should-may)
      *  2.2. [Guidelines for Interpreting Descriptive Text and Tables](./xapi-profiles-about.md#interpret-text-table)
   *  3.0. [Definitions](./xapi-profiles-about.md#definitions)
* Part Two: [xAPI Profiles Document Structure Specification](./xapi-profiles-structure.md#part-two)  
   *  1.0.  [Reference Specifications](./xapi-profiles-structure.md#ref-spec)
   *  2.0.  [Technical Foundations](./xapi-profiles-structure.md#tech-foundations)
   *  3.0.  [Structure](./xapi-profiles-structure.md#structure)
   *  4.0.  [Document Interpretation and General Restrictions](./xapi-profiles-structure.md#doc-interp-gen-restrict)
   *  5.0.  [Using Profiles in Statements](./xapi-profiles-structure.md#using-prof-statements)
   *  6.0.  [Profile Properties](./xapi-profiles-structure.md#prof-props)
      *  6.1.  [Profile Version Objects](./xapi-profiles-structure.md#prof-ver-obj)
      *  6.2.  [Organizations and Persons](./xapi-profiles-structure.md#orgs-persons)
   *  7.0.  [Concepts](./xapi-profiles-structure.md#concepts)
      *  7.1.  [Verbs, Activity Types, and Attachment Usage Types](./xapi-profiles-structure.md#verb-activity-attach)
      *  7.2.  [Extensions](./xapi-profiles-structure.md#extensions)
      *  7.3.  [Document Resources](./xapi-profiles-structure.md#doc-resources)
      *  7.4.  [Activities](./xapi-profiles-structure.md#activities)
   *  8.0.  [Statement Templates](./xapi-profiles-structure.md#statment-templates)
      *  8.1.  [Statement Template Rules](./xapi-profiles-structure.md#statement-template-rules)
   *  9.0.  [Patterns](./xapi-profiles-structure.md#patterns)
   *  10.0. [The Context](./xapi-profiles-structure.md#context)
* Part Three: [xAPI Profiles Communication and Processing Specification](./xapi-profiles-communication.md#part-three)  
   * 1.0. [Profile Server](./xapi-profiles-communication.md#prof-server)
      * 1.1. [Profile Versions](./xapi-profiles-communication.md#prof-versions)
      * 1.2. [Best Practices](./xapi-profiles-communication.md#best-practices)
      * 1.3. [Example SPARQL Queries](./xapi-profiles-communication.md#example-sparql)
   * 2.0. [Algorithms](./xapi-profiles-communication.md#algorithms)
      * 2.1. [Statement Template Validation](./xapi-profiles-communication.md#statement-template-valid)
      * 2.2. [Pattern Validation](./xapi-profiles-communication.md#pattern-valid)
  * 3.0. [Libraries](./xapi-profiles-communication.md#libraries)



<a name="part-three"></a>
# Part Three: Communication and Processing

In addition to the ability to host Profiles as documents, there will be infrastructure
for querying and manipulating Profiles. This document describes the algorithms for
processing Profiles, including the exact rules by which Statement Templates and Patterns
are validated against Statements. It also describes a “Profile Server” to make it easier
to manage and answer questions about Profiles from a centralized location, including
implementing the algorithms.

## Authored Profiles

ADL maintains a [centralized public repository of authored xAPI profiles](https://github.com/adlnet/xapi-authored-profiles) based on this specification. The repository of profiles are imported and synchronized regularly into ADL's Profile Server, [http://xapi.vocab.pub](http://xapi.vocab.pub). 

<a name="prof-server"></a>
## 1.0 Profile Server

A Profile Server manages xAPI Profiles from a centralized location. [An RDF triple store](https://en.wikipedia.org/wiki/Triplestore) is responsible for the storage of Profiles.
A Profile Server will allow administrators to add Profiles by their contents or by URI to the Profile Server

ADL's Profile Server will host a SPARQL endpoint containing the RDF information from the
contained Profiles at the path /sparql (e.g., http://xapi.vocab.pub/sparql). This enables xAPI Profiles to be queried. SPARQL
servers have the ability to divide information into multiple datasets, or graphs, and
offer separate querying on them. One of these is the default graph, which is queried
when no other graph is specified. The default graph at this SPARQL endpoint will
contain all the current versions of Profiles.

A Profile Server will include inference logic for the following, at minimum: all SKOS predicate relationships, and `profile:concepts`, `profile:templates`, and `profile:patterns` being subproperties of the inverse of `skos:inScheme`.

**Note: ** As stated in the section [Part One: About xAPI Profiles, section 2.2](./xapi-profiles-about.md#interpret-text-table) this specification does not place any limits on character limits on xAPI Profile fields but a Profile Server implementation MAY choose to include character limits for purposes like security or data storage.

<a name="prof-versions"></a>
### 1.1 Profile Versions

Every Profile version will be in a [Named Graph](https://www.w3.org/TR/sparql11-query/#namedGraphs)
with a URI equal to the Profile version's URI.  Non-current (and current) versions of
Profiles are required to be in named graphs with URIs of their version.  This means
they can be queried directly by specifying the URI. Additionally, the current version
in the default graph has the versioning information, making it possible to traverse
them without knowing their URIs in advance. Reasons why one would query versions
of xAPI Profiles include retrieving a version used by an xAPI Statement, and/or
understanding when a concept was deprecated or removed.

The URI of the named graph is always the URI of the Profile version. Note: The URI of the
named graph doesn't mean the URI it is retrieved at, it means the URI used to refer to it
within SPARQL/the RDF store.

In summary: by default, queries will only operate on up to date
information; if historical Profile information is needed, it is available.

<a name="best-practices"></a>
### 1.2 Best Practices

Some best practices are recomended when adding a Profile to a Profile Server. A technical
review process is warranted to check Profiles for following the specification. As well,
analysis is recommended to ensure the contents of a Profile are of the highest quality.
Upon following these practices, a Profile should be added to a Profile server.

As Profiles support localizations to multiple languages and localities, it is advisable to
provide mechanisms to encourage contribution of xAPI Profile translations. To promote and
to protect the use of an xAPI Profile made publicly available, it is strongly encouraged
that any xAPI Profile provided through a Profile Server be open-licensed.

<a name="example-sparql"></a>
### 1.3 Example SPARQL Queries


Here are a selection of questions and the SPARQL queries that answer them, for retrieving
commonly needed information from the server. All these SPARQL queries can also be run
locally by loading one or more Profiles into an RDF library and running SPARQL queries
against them directly, with minor modifications depending on how the data is loaded.

All queries start with the following block of prefixes:

```sparql
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX xapi: <https://w3id.org/xapi/ontology#>
PREFIX profile: <https://w3id.org/xapi/profiles/ontology#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX schemaorg: <http://schema.org/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
```

“What profiles are on the server?”

```sparql
select
    ?profile,
    ?prefLabel,
    ?definition
where {
    ?profile a profile:Profile ;
             skos:prefLabel ?prefLabel ;
             skos:definition ?definition .
}
```


“What verbs and activity types does this Profile describe?”


```sparql
select
    ?concept,
    ?prefLabel,
    ?definition
where {
    (?concept a xapi:Verb || ?concept a xapi:ActivityType) .                
    ?concept skos:inScheme <http://example.org/profiles/sports> ;
             skos:prefLabel ?prefLabel ;
             skos:definition ?definition .
}
```


“What Statement Templates are available in this Profile?”, “What Patterns are available
in this Profile?”

Virtually identical to the above, just replace being a Verb or Activity Type with Statement
Template or Pattern. We're able to use inScheme because the server includes semantic
metadata letting it know that being a Statement Template, being a Concept, and being a
Pattern are all forms of being inScheme, which is a general inclusion predicate.

<a name="algorithms"></a>
## 2.0 Algorithms

This section specifies two primary algorithms. The first, given a Statement and a set of
Statement Templates, validates the Statement against all applicable Statement Templates in
those provided and returns the Statement Templates that match, or an error if any of the
matching Statement Templates does not validate against the Statement. The second, given a
collection of Statements and a set of Patterns, validates if the Statements follows any of
the Patterns.

<a name="statement-template-valid"></a>
### 2.1 Statement Template Validation

To validate a Statement against the Statement Templates of a Profile, call the `validates`
function described in pseudocode below with the Statement and all the Statement Templates
from the Profile. This function returns an outcome and an array of Statement Templates. To
interpret the results, consult the table after the algorithm definition.

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
success   | non empty | one or more Statement Templates matched and all their rules are followed. The templates array contains all matched Statement Templates.
invalid   | non empty | one or more Statement Templates matched but not all their rules were followed. The templates array contains all Statement Templates that matched but had some rules unfollowed.
unmatched | empty     | no Statement Templates matched


<a name="pattern-valid"></a>
### 2.2 Pattern Validation

To validate a series of Statements sharing a registration (and, if applicable, subregistration)
follows a specified Profile, apply the `follows` algorithm described below, which returns
simple success or failure. For more nuanced interpretation, examine the `matches` algorithm,
which is used by `follows`. A table for interpreting the return values of the `matches`
algorithm is provided following the pseudocode for the algorithms.

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
success | empty                | Pattern validates for these Statements
success | non empty            | Pattern matches some of the Statements, but not all
partial | empty                | Pattern was in the middle of matching and ran out of Statements
partial | non empty            | outcome could be interpreted as success with non empty remaining, but Pattern could also continue matching
failure | original statements  | Pattern failed to match Statements. Note: if an optional or zeroOrMore Pattern is directly inside an alternates Pattern, it is possible for failure to be returned when partial is correct, due to decidability issues.


A Pattern only matches if it matches greedily. That is, each optional, zeroOrMore, oneOrMore,
and alternate Pattern MUST always be considered to match the maximum length possible before
considering any Patterns later in a sequence. No backtracking is allowed. This constrains
useful Patterns, but guarantees efficient processing, as once a Statement is matched it does
not need to be reconsidered (except in cases where it is part of an ultimately unmatched
alternate).

When checking previously collected Statements for matching a Pattern, ordering MUST be based
on timestamp. In the event two or more Statements have identical timestamps, any order within
those Statements is allowed.

When checking Statements for matching a Pattern upon receipt, ordering MUST be based on receipt
order insofar as that can be determined. If Statements are received in the same batch and they
are being checked upon receipt, within the batch Statements MUST be ordered first by timestamp,
and if timestamps are the same, by order within the Statement array, with lower indices earlier.

<a name="libraries"></a>
## 3.0 Libraries

Any programming library that implements the algorithms given here, exposing all of the listed
functions, will be an xAPI Profile Processor library.

For each of the `validates`, and `follows`, the Profile Server will provide web APIs that are
strongly Not Recommended for production usage, but are suitable for experimentation and
demonstration. Code on the critical path (such as validating Statements against Profiles on LRS
intake), or that might be used when internet access is not available (such as when using an
authoring tool), should not use these APIs, and should use their own code or an xAPI Profile
Processor Library as appropriate.

Additionally, the pseudocode above isn't written to support processing as data is received,
as that both adds complication and needs to be adapted to the exact capabilities of the
implementing system.

Their URL paths will be /validate_templates and /validate_patterns, respectively. The first
will take a single xAPI Statement and a Profile specified by id, specified in POST variables
as “statement” and “profile”. The second will take an array of xAPI Statements and a Profile
specified by id, both specified in POST variables as “statements” and “profile”.

Both will perform the algorithms above and return 204 on successful validation and 400 on
failure, with descriptive comments that provide information as to which rule was violated (in
the case of statement template processing) or which part of the pattern was violated (in the
case of pattern processing.
