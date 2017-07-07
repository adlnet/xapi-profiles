
# Communication

In addition to the ability to host profiles separately, there will be one or more pieces of infrastructure for querying and manipulating profiles. A central component will be a “Profile Server” to make it easier to manage and answer questions about profiles from a centralized location.

Administrators will be able to add profiles by their contents or by URI to the Profile Server. On a Public Profile Server run by... DISC? ADL? ... there will be a review process people desiring to add profiles can submit to. The review process will check profiles for following the specification and assist in helping them be of highest quality, after which they will be added to the server.

The Profile Server will host a SPARQL endpoint containing the RDF information from the contained profiles at the path /sparql. SPARQL servers have the ability to divide information into multiple datasets, or graphs, and offer separate querying on them. One of these is the default graph, which is queried when no other graph is specified. The default graph at this SPARQL endpoint will contain all the current versions of profiles. Additionally, every profile version will be in a Named Graph with a URI equal to the profile version's URI. Thus, by default queries will only operate on up to date information, but if historical profile information is needed, it is available.

TODO: consider having the default graph only contain the versioning information, which would make queries slightly more complex but would make it harder for accidental profile trampling to occur...

Here are a selection of SPARQL queries for retrieving commonly needed information from the server. All these SPARQL queries can also be run locally by loading one or more profiles into an RDF library and running sparql queries against them directly.

Using that SPARQL server, it will be easy to answer questions such as:

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

## Validating Statements

To retrieve the information needed to validate a statement, a simple SPARQL query suffices — retrieve all the statement templates, with their rules, for the profile version(s) indicated in the statement. From there, apply a series of operations. First, for each profile, find templates with determining properties that match in full. There will generally be one or zero. If zero, this statement does not match any templates in the profile and does not validate. From there, for each template with matching determining properties, iterate through the rules, executing the JSONPath queries and applying the requirements. Additionally, check if the object StatementRef and context StatementRef requirements are met. If the referenced Statement is available to the checking system, it MUST be checked for matching the given Statement Template, but if it is not, it MUST be assumed to match the given Statement Template. If all the rules are fulfilled, and the StatementRefs check out, then the statement matches the template. If for every Statement Template in a profile with matching determining properties, it matches the template, the statement validates against the profile. If a statement validates for every profile in its context, it validates generally.

### Patterns

To validate a series of statements sharing a registration (and, if applicable, subregistration) matches a pattern for a specified profile, include the profile's patterns in the retrieved data along with the data for statement templates. For each statement, check which statement templates are matched. If a statement does not match at least one statement template for the specified profile, the statements do not match the pattern.

Next, check each top-level pattern in the specified profile for matching. If at least one top-level pattern matches, the series of statements validates. A pattern match validates if matches(series, pattern) returns success for the first value and the second value is empty. The algorithm follows, in pseudocode:

```
function matches(statements, element):
    if element is a template:
        if statements is empty:
            return partial, []
        if statements[0]'s set of statement templates includes element:
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

TODO: continue testing of the above. Fairly extensive testing has already been done using generative testing, in the companion python code.

This table summarizes the possible return values and what they indicate:

outcome | remaining statements | outcome
------- | -------------------- | -------
success | empty                | pattern validates for these statements
success | non empty            | pattern matches some of the statements, but not all
partial | empty                | pattern was in the middle of matching and ran out of statements
partial | non empty            | outcome could be interpreted as success with non empty remaining, but pattern could also continue matching
failure | original statements  | pattern failed to match statements. Note: if an optional or zeroOrMore pattern is directly inside an alternates pattern, it is possible for failure to be returned when partial is correct, due to decidability issues.



A pattern only matches if it matches greedily. That is, each optional, zeroOrMore, oneOrMore, and alternate pattern MUST always be considered to match the maximum length possible before considering any patterns later in a sequence. That is, no backtracking is allowed. This constrains useful statement patterns, but guarantees efficient processing, as once a statement is matched it does not need to be reconsidered (except in cases where it is part of an ultimately unmatched alternate).
When checking previously collected statements for matching a pattern, ordering MUST be based on timestamp. In the event two or more statements have identical timestamps, any order within those statements is allowed.
When checking statements for matching a pattern upon receipt, ordering MUST be based on receipt order insofar as that can be determined. If statements are received in the same batch and they are being checked upon receipt, within the batch statements MUST be ordered first by timestamp, and if timestamps are the same, by order within the statement array, with lower indices earlier.


### Libraries

Any library that implements the algorithms given here will be an xAPI Profile Processor library. Reference implementation libraries in one or more languages will be provided.

For each of the library operations, the Profile Server will provide web APIs that are strongly Not Recommended for production usage, but are suitable for experimentation and demonstration.

One URL will be at /validate_templates, and the other at /validate_patterns. The first will take a single xAPI statement and a profile specified by id, specified in POST variables as “statement” and “profile”. The second will take an array of xAPI statements and a profile specified by id, both specified in POST variables as “statements” and “profile”. Both will check if the single statement or sequence of statements matches any template or pattern in the profile given.

Both will perform the algorithms above and return 204 on successful validation and 400 on failure, with descriptive comments attached on failure.

TODO: figure out if the profile parameter is really needed, consider return values that are the array of profiles with a matching template or pattern, or maybe even the templates or patterns themselves?
