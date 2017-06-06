# xAPI Profiles Draft Specification

## Reference Specifications

* [http://json-ld.org](http://json-ld.org/)
* [https://www.w3.org/TR/skos-reference/](https://www.w3.org/TR/skos-reference/)
* [https://www.w3.org/TR/2013/REC-prov-dm-20130430/](https://www.w3.org/TR/2013/REC-prov-dm-20130430/)
* [https://www.w3.org/TR/activitystreams-core/](https://www.w3.org/TR/activitystreams-core/)
* [https://www.w3.org/TR/rdf-sparql-query/](https://www.w3.org/TR/rdf-sparql-query/)

## Technical Foundations

This specification describes how to author an xAPI Profile. It describes a set of rules for authoring JSON, specifically JSON-LD. Since JSON-LD is a syntax for RDF, the resulting profile is really a set of triples—subject, predicate, object—creating a semantic data set. However, for authoring, all that matters is following the rules given for JSON, which will lead to the richer semantic data naturally. Because of this, no JSON-LD processing is required by systems consuming xAPI Profiles, though there will be advantages to doing so for some purposes.

The serialized JSON form of an xAPI Profiles 1.0 profile version must be consistent with what would be produced by the standard JSON-LD 1.1 Processing Algorithms and API Compaction Algorithm using, at least, the normative JSON-LD @context definition provided.

Under the hood, xAPI Profiles will use several well-established semantic web technologies: SKOS, to connect xAPI concepts together, and PROV, to describe the provenance (most notably the versioning) of profiles. Several properties in xAPI Profiles use names of properties from SKOS and PROV.

# Structure

Profiles serve two primary technical goals. First, they contain metadata about xAPI Concepts intended for reuse within statements, such as verbs and activity types. The metadata includes connections between Concepts, not just within the current profile, but also as used in other profiles, supporting a rich ecosystem of related terms. An xAPI Concept is any building block for use in Statements, and new versions of the profile specification may introduce new Concepts that can be described. The basis for xAPI Concepts is the SKOS Concept, a flexible way to refer to "specific ideas or meanings established within a knowledge organization system."

Second, they contain specific rules about using those Concepts properly in specific situations, both on how to form individual statements containing specific Concepts, and how to group those statements together in patterns of multiple statements. These rules allow profile authors to require specific elements, describe precise orderings, and many other options.

To assist in accomplishing these two primary goals, profiles also contain metadata about themselves—descriptions, authorship, versioning, and so forth.

## Using Profiles in Statements

Using an introduced Concept, such as an activity type, verb, attachment usage type, extension, activity, or document resource, should be done freely, provided the defined usage and meaning are adhered to. But a Learning Record Provider can go further, and make sure to adhere to profile-described statement templates and patterns. Learning Record Providers creating statements that conform to matching profile-described statement templates and patterns SHOULD include the most up to date conformant profile version as a category context activity with id equal to the version's `@id` in those statements, and statements containing a profile version as a category context activity MUST conform to any matching templates and patterns that profile version describes.

## Profile Metadata

Name | Values
---- | ------
`@id` | The IRI of the profile overall (not a specific version)
`@type` | Must be `Profile`.
`conformsTo` | Canonical URI of the profile specification version conformed to. The profile specification version of this document is https://github.com/DataInteroperability/xapi-profiles/tree/master#1.0.0-development, and it is a development version that may undergo incompatible changes without updating the version URI.
`name` | Language map of names for this profile.
`definition` | Language map of descriptions for this profile. If there are additional rules for the profile as a whole that cannot be expressed using this specification, include them here.
`seeAlso` | A URL containing information about the profile. Recommended instead of especially long definitions.
`versions` | An array of all profile version objects for this profile, see below.
`author` | An Organization or Person, see below.
`concepts` | The concepts that make up this Profile, see the Concepts section.
`templates` | The Statement Templates for this profile, see that section.
`patterns` | The Patterns for this profile, see that section.



### Profile Version Objects

Name | Values
---- | ------
`@id` | The IRI of the version ID
`wasRevisionOf` | an array, usually of length one, of IRIs of all profile versions this version was written as a revision of
`generatedAtTime` | the date this version was created on

Profile version objects make it convenient to track version history for profiles, following recommendations for SKOS concept schemes and PROV version tracking generally. By using versions this way, it is possible to answer precise questions such as “what version of this profile was current on the 3rd of January last year?”. Lack of robust versioning is frequently identified as an issue with RDF data.

### Organizations and Persons

Use one of these in the `author` property to indicate the author of this profile version.

Name | Values
---- | ------
`@type` | Organization or Person
`name` | A string with the name of the organization or person

## Concepts

### Core Concepts: Verbs, Activity Types, and Attachment Usage Types

These Concepts are the most central to building rich, reusable profiles. When describing verbs, activity types, and attachment usage types, a profile MUST use the following structure:

Name | Values
---- | ------
`@type` | `Verb`, `ActivityType`, or `AttachmentUsageType`
`inScheme` | The IRI of the specific profile version currently being described
`prefLabel` | A language map of the preferred names in each language
`altLabel` | An array of language-tagged alternative names. Array members MUST be expanded value objects with @value and @language keys.
`definition` | A language map of the precise definition, including how to use the concept properly in statements
`deprecated` | Optional. A boolean. If true, this concept is deprecated.
`broader` | An array of IRIs of concepts of the same @type from this profile version that have a broader meaning.
`narrower` | An array of IRIs of concepts of the same @type from this profile version that have a narrower meaning.
`broadMatch` | An array of IRIs of concepts of the same @type from a different profile that have a broader meaning.
`narrowMatch` | An array of IRIs of concepts of the same @type from different profiles that have narrower meanings.
`exactMatch` | An array of IRIs of concepts of the same @type from a different profile or a different version of the same profile that have exactly the same meaning. This should be used rarely, mostly to describe connections to vocabularies that are no longer managed and do not use good URLs.
`relatedMatch` | An array of IRIs of concepts of the same @type from a different profile or a different version of the same profile that has a related meaning that is not clearly narrower or broader. Useful to establish conceptual links between profiles that can be used for discovery. This SHOULD be used to connect possible replacement Concepts to removed Concepts from previous versions of the same profile, and for possible replacement Concepts in other profiles of deprecated concepts, as well as other loose relations.
`related` | An array of IRIs of concepts of the same @type from this profile version that are close conceptual matches to this concept's meaning. This property MUST only be used on concepts that are deprecated to indicate possible replacement concepts in the same profile, if there are any.

### Extensions

For describing Extension Concepts, a profile MUST use the following structure:

Name | Values
---- | ------
`@id` | The IRI of the extension, used as the extension key in xAPI
`@type` | `Extension`
`inScheme` | The IRI of the specific profile version currently being described
`name` | A language map of descriptive names for the extension
`definition` | A language map of descriptions of the purpose and usage of the extension
`deprecated` | Optional. A boolean. If true, this concept is deprecated.
`placement` | An array of placement locations. Must contain at least one element, no elements may be repeated, and the only allowed elements are `context`, `result`, `activity` and IRIs (which must be Activity Type IRIs in this or other profiles).
`context` | *Optional*. the IRI of a JSON-LD context for this extension
`schema` | *Optional*. the IRI for accessing a JSON Schema for this extension. The JSON Schema may constrain the extension to a single type.
`inlineSchema` | *Optional*. A JSON Schema inline. Must be a string that contains a legal JSON Schema.

An Extension MUST include at most one of schema and inlineSchema.

### Document Resources

When describing document resource Concepts, a profile MUST use the following structure, which is similar to the one used for extensions. The @id MUST be used as the stateId or profileId (as appropriate) when interacting with the corresponding resource.


Name | Values
---- | ------
`@id` | The IRI of the document resource, used as the stateId/profileId in xAPI
`@type` | One of: `StateResource`, `AgentProfileResource`, `ActivityProfileResource`
`inScheme` | The IRI of the specific profile version currently being described
`name` | A language map of descriptive names for the document resource
`definition` | A language map of descriptions of the purpose and usage of the document resource
`deprecated` | Optional. A boolean. If true, this concept is deprecated.
`context` | *Optional*. the IRI of a JSON-LD context for this document resource
`schema` | *Optional*. the IRI for accessing a JSON Schema for this document resource.
`inlineSchema` | A JSON Schema inline. Must be a string that contains a legal JSON Schema.
`contentType` | The content-type for the resource

### Activities

These Concepts are just literal xAPI Activity definitions the profile wants to provide for use. This is the profile's canonical version of the Activity. Except for `@context`, the activityDefinition in this Concept MUST be a legal xAPI Activity Definition. When using the Activity, a Statement MUST use the `@id` for the Activity `id`, and MUST NOT include `@context` in the Activity definition. All other properties of the activityDefinition are considered part of the definition, and any Statement using the Activity SHOULD either not include the definition, or SHOULD include all properties given here in the definition exactly as given, except for `name` and `description` or other language maps, which SHOULD only include languages appropriate to the situation, possibly including ones not present in the profile yet.

Due to restrictions in JSON-LD, all extensions in the Activity definition that do not have primitive values (string, number, boolean, null, or arrays thereof) MUST include a JSON-LD @context in the top-level object, or in every top-level object if array-valued.

Name | Values
---- | ------
`@id` | The IRI of the activity
`@type` | `Activity`
`inScheme` | The IRI of the specific profile version currently being described
`deprecated` | Optional. A boolean. If true, this concept is deprecated.
`activityDefinition` | An Activity Definition as in xAPI, plus an @context, as in the table below.

Name | Values
---- | ------
`@context` | Must be TODO create an Activity context and host it at a URI.
`type` | As in xAPI
`name`
`description`
`moreInfo`
`extensions`
`interactionType`
`correctResponsesPattern`
`choices`
`scale`
`source`
`target`
`steps`

## Statement Templates

A Statement Template describes one way statements following the profile may be structured. The verb, object activity type, attachment usage types, and context activity types listed are the determining properties. When authoring a statement to follow a template, a Learning Record Provider MUST include all the determining properties, as well as follow all rules in the template. Any statement including all the determining properties and using the profile version as a category context activity MUST follow the rules. In a profile, no Statement Template's determining properties may be a subset of any other Statement Template's determining properties. Additionally, we recommend picking one of the determining properties to use in all Statement Templates in a profile, with different values in each, since this ensures each statement matches at most one Statement Template in a given profile. A profile SHOULD ensure each statement following any of its Statement Templates will match at most one Statement Template.

If a statement matches a Statement Template's determining values and uses the profile version as a category context activity, it MUST be sent as part of a Pattern or Implied Pattern.

Name | Values
---- | ------
`@id` | The identifier or short name of the template, in the form :name
`@type` | `StatementTemplate`
`inScheme` | The IRI of the specific profile version currently being described
`name` | a language map of descriptive names for the Statement Template
`definition` | A language map of descriptions of the purpose and usage of the Statement Template
`allowedSolo` | Optional. A boolean, default false. If true, this Statement Template can be used as a single statement Implied Pattern (see that section). A Statement Template may be both used in Patterns and allowedSolo true.
`deprecated` | Optional. A boolean, default false. If true, this Statement Template is deprecated.
`verb` | *Optional*. Verb IRI
`objectActivityType` | *Optional*. Object activity type IRI
`contextGroupingActivityType` | *Optional*. Array of contextActivities grouping activity type IRIs
`contextParentActivityType` | *Optional*. Array of contextActivities parent activity type IRIs
`contextOtherActivityType` | *Optional*. Array of contextActivities other activity type IRIs
`contextCategoryActivityType` | *Optional*. Array of contextActivities category activity type IRIs
`attachmentUsageType` | *Optional*. Array of attachment usage type IRIs
`rules` | Array of Statement Template Rules

### Statement Template Rules

Statement Template Rules describe a location or locations within statements using JSONPath, then describe the restrictions on that value, such as inclusion, exclusion, or specific values allowed or disallowed. For example, to require at least one grouping, the rules might be something like:

```
"rules": [
    {
        "location": "context.contextActivities.grouping[0]",
        "rule": "included"
    }
]
```

They have these properties:

Name | Values
---- | ------
`location` | A JSONPath string
`selector` | *Optional*. A JSONPath string. This JSONPath is executed on the array of values resulting from the location selector, and the resulting values are what are used for matching. If it returns nothing on a location, that represents an unmatchable value for that location, meaning "all" will fail, as will included.
`rule` | `included` or `excluded`. If included, there must be at least one matchable value for this Statement Template Rule to be fulfilled, and if excluded, no matchable values.
`any` | an array of values that are allowed in this location. Useful for constraining the presence of particular activities, for example. If the rule returns multiple values for a statement, then this Statement Template Rule is fulfilled if any one returned value matches any one specified value — that is, if the intersection is not empty.
`all` | an array of values, which all values returned by the JSONPath must match one of to fulfill this Statement Template Rule.
`none` | an array of values, which no values returned by the JSONPath may match to fulfill this Statement Template Rule.

A Statement Template Rule MUST include one or more of rule, any, all, or none.

### Alignments?

I propose we do not include alignments in the initial draft

### Statement References

I'm unsure enough how to do this I propose we do not include statement reference constraints in the initial draft. It would probably be included as a special case in the statement template rules, above.

## Patterns

Patterns are groups of statements matching particular statement templates, ordered in certain ways. For example, an allowed pattern in a video profile might start with a statement about playing a video and then be followed by statements about pausing, skipping, playing again, and so forth. A pattern is determined by a given registration — all statements within a Pattern MUST use the same registration, and statements not part of a Pattern MUST NOT use the same registration as any that are.

Patterns have these properties:


Name | Values
---- | ------
`@id` | The identifier or short name of the template, in the form :name
`@type` | `Pattern`
`inScheme` | The IRI of the specific profile version currently being described
`name` | A language map of descriptive names for the pattern
`definition` | A language map of descriptions of the purpose and usage of the pattern
`deprecated` | Optional. A boolean. If true, this pattern is deprecated.
`alternates` | A two-or-more length array of pattern or statement template identifiers. An alternates pattern matches if any member of the array matches
`optional` | A single pattern or statement template identifier. An optional pattern matches if the identified thing matches once, or is not present at all
`oneOrMore` | A single pattern or statement template identifier. A oneOrMore pattern matches if the identified thing matches once, or any number of times more than once
`sequence` | An array of pattern or statement template identifiers. A sequence pattern matches if the identified things match in the order specified.
`zeroOrMore` | A single pattern or statement template identifier. A zeroOrMore pattern matches if the identified thing is not present or is present one or more times



A pattern MUST contain exactly one of `alternates`, `optional`, `oneOrMore`, `sequence`, and `zeroOrMore`.
A pattern with an @id MUST NOT include name, definition, or deprecated.
A pattern without an @id MUST include name and definition.
A pattern MUST not refer to any pattern that has itself in the array or single value for any of `alternates`, `optional`, `oneOrMore`, `sequence`, or `zeroOrMore`, considered recursively.
A pattern only matches if it matches greedily. That is, if, when checking for a match of an optional or zeroOrMore or oneOrMore pattern, the next statement matches the pattern or statement template it applies to, the statement MUST be considered to be part of that match. That is, no backtracking is allowed. This constrains useful statement patterns, but guarantees efficient processing, as once a statement is matched it does not need to be reconsidered (except in cases where it is part of an ultimately unmatched alternate).
When checking previously collected statements for matching a pattern, ordering MUST be based on timestamp. In the event two or more statements have identical timestamps, any order within those statements is allowed.
When checking statements for matching a pattern upon receipt, ordering MUST be based on receipt order insofar as that can be determined. If statements are received in the same batch and they are being checked upon receipt, within the batch statements MUST be ordered first by timestamp, and if timestamps are the same, by order within the statement array, with lower indices earlier.

### Implied Patterns

If a Statement Template is allowed solo, Learning Record Providers MAY send it as an Implied Pattern. If it is not, Learning Record Providers MUST NOT send it as an Implied Pattern. An Implied Pattern MUST include the profile version in category, and MAY include a registration as if it were described as a Pattern with a sequence of one statement template, but MAY leave off the registration.

When checking for pattern match of a Statement with a registration, if there is only one Statement for the registration and it matches a Statement Template that is allowed solo, it MUST be considered an Implied Pattern.

An allowed solo Statement Template MUST describe when Learning Record Providers should use it as an Implied Pattern. While this cannot be checked programmatically, without it Learning Record Providers will be unable to understand the solo usage of Statement Templates.

## Very Preliminary Draft Context

```
{
    "@context": {
        "prov": "http://www.w3.org/ns/prov#",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "xapi": "http://purl.org/xapi/ontology#",

        "type": "@type",
        "id": "@id",
        "Profile": "xapi:Profile",
        "Verb": "xapi:Verb",
        "ActivityType": "xapi:ActivityType",
        "AttachmentUsageType": "xapi:AttachmentUsageType",
        "Extension": "xapi:Extension",
        "inScheme": "skos:inScheme",
        "wasRevisionOf": {
            "@id": "prov:wasRevisionOf",
            "@type": "@id"
        },
        "wasGeneratedBy": {
            "@id": "prov:wasGeneratedBy",
            "@type": "prov:Activity"
        },
        "versions": {
            "@reverse": "prov:specializationOf",
            "@type": "xapi:Profile",
            "@container": "@set"
        },
        "concepts": {
            "@reverse": "xapi:inProfile",
            "@container": "@set"
        },
        "prefLabel": {
            "@id": "skos:prefLabel",
            "@container": "@language"
        },
        "altLabel": "skos:altLabel",
        "definition": {
            "@id": "skos:definition",
            "@container": "@language"
        },
        "broadMatch": {
            "@id": "skos:broadMatch",
            "@type": "@id"
        },
        "narrowMatch": {
            "@id": "skos:narrowMatch",
            "@type": "@id"
        },
        "broader": {
            "@id": "skos:broader",
            "@type": "@id"
        },
        "narrower": {
            "@id": "skos:narrower",
            "@type": "@id"
        },
        "name": {
            "@id": "http://www.w3.org/2000/01/rdf-schema#label",
            "@container": "@language"
        }
    }
}
```

## Initial Very Rough Sketch of an Example Profile

There will be lots of examples, but this is largely an exercise in feeling out what things will look like, for now. Currently contains a number of errors related to the above as it needs updating.

```
{
    "@id": "http://myvocab.example.com/xapi/",
    "@type": "Profile",
    "versions": [
        {
            "@id": "http://myvocab.example.com/xapi/2.0/",
            "wasRevisionOf": "http://myvocab.example.com/xapi/1.0/"
        },
        {
            "@id": "http://myvocab.example.com/xapi/1.0/"
        }
    ],
    "wasGeneratedBy": {
        "name": {
            "en": "Sports and Competition xAPI Vocabulary Working Group"
        }
    },
    "patterns": [
        {
            "name": "",
            "sequence": ["entered", {}, ""]
        }
    ],
    "concepts": [
        {
            "@id": "http://myvocab.example.com/xapi/placed",
            "@type": "Verb",
            "inScheme": "http://myvocab.example.com/xapi/2.0/",
            "prefLabel": {
                "en": "placed"
            },
            "altLabel": {
                "en": "ranked"
            },
            "definition": {
                "en": "To achieve a ranked outcome in the Activity object, which is a competitive event"
            },
            "broadMatch": ["http://www.adlnet.gov/expapi/verbs/completed"],
        },
        {
            "@id": "http://myvocab.example.com/xapi/judgingScores",
            "@type": "Extension",
            "prefLabel": {
                "en": "Judging Scores"
            },
            "definition": {
                "en": "The judging scores, expressed in JUDGING-JSON, as described at ___"
            },
            "seeAlso": "http://judgingjson.example.org",
            "context": "http://judgingjson.example.org/context.jsonld",
            "location": ["result"]
        },
        {
            "@id": "http://myvocab.example.com/xapi/SummerOlympics2016",
            "definition": {
                "type": "http://myvocab.example.com/xapi/OlympicGames",
                "name": {
                    "en": "Summer Olympics 2016"
                }
            }
        }
    ]

}
```

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

To retrieve the information needed to validate a statement, a simple SPARQL query suffices — retrieve all the statement templates, with their rules, for the profile(s) indicated in the statement. From there, apply a series of operations. First, for each profile, find templates that match per verb, object activity type, and attachment usage type. There will generally be one or zero. If zero, this statement does not match any templates in the profile. From there, for each matching template, iterate through the rules, executing the JSONPath queries and checking for included, excluded, or values rules. If all the rules are fulfilled, then the statement matches the template. If the statement matches at least one template in the profile, it matches that profile. If a statement matches every profile in its context, it validates.

The above will be described with more precision, with a (non-web) API interface described, much as JSON-LD does. Any library that implements the algorithms given here will be an xAPI Profile Processor library. Reference implementation libraries in one or more languages will be provided.

Another algorithm will apply for validating multiple statements for matching a pattern, again starting with a simple SPARQL query and proceeding through rules, this time based on the pattern element rules. Again, this will be part of the xAPI Profile Processor library.

For each of the above operations, the Profile Server will provide web APIs that are strongly Not Recommended for production usage.

One URL will be at /validate_templates, and the other at /validate_patterns. The first will take a single xAPI statement and a profile specified by id, specified in POST variables as “statement” and “profile”. The second will take an array of xAPI statements and a profile specified by id, both specified in POST variables as “statements” and “profile”.

Both will perform the algorithms above and return 204 on successful validation and 400 on failure, with descriptive comments attached on failure.
