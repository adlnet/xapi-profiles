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

## Document Interpretation and General Restrictions

* All properties in tables are required in all cases unless marked optional.
* Properties marked optional may be required in some situations. If no additional information is provided on the usage of an optional property, including it or not is entirely up to the profile author.
* All properties that are not JSON-LD keywords (or aliases thereof) in profile documents MUST expand to absolute IRIs during processing as defined in the JSON-LD specification.
* All properties that are not JSON-LD keywords (or aliases thereof) in a profile MUST be described by this specification or be expressed using compact IRIs.
* JSON-LD keywords (or aliases thereof) that are not specified as properties in this document MAY be included anywhere they are legal in JSON-LD.
* Values in a profile MUST NOT be: empty objects, null, empty strings, or empty arrays.

## Using Profiles in Statements

Using an introduced Concept, such as an activity type, verb, attachment usage type, extension, activity, or document resource, should be done freely, provided the defined usage and meaning are adhered to. But a Learning Record Provider can go further, and make sure to adhere to profile-described statement templates and patterns. Learning Record Providers creating statements that conform to matching profile-described statement templates and patterns SHOULD include the most up to date conformant profile version as a category context activity with id equal to the version's `@id` in those statements, and statements containing a profile version as a category context activity MUST conform to any matching templates and patterns that profile version describes.

## Profile Metadata

Name | Values
---- | ------
`@id` | The IRI of the profile overall (not a specific version)
`@type` | Must be `Profile`.
`conformsTo` | Canonical URI of the profile specification version conformed to. The profile specification version of this document is https://github.com/DataInteroperability/xapi-profiles/tree/master#1.0-development, and it is a development version that may undergo incompatible changes without updating the version URI.
`prefLabel` | Language map of names for this profile.
`definition` | Language map of descriptions for this profile. If there are additional rules for the profile as a whole that cannot be expressed using this specification, include them here.
`seeAlso` | *Optional*. A URL containing information about the profile. Recommended instead of especially long definitions.
`versions` | An array of all profile version objects for this profile, see below.
`author` | An Organization or Person, see below.
`concepts` | *Optional*. The concepts that make up this Profile, see the Concepts section.
`templates` | *Optional*. The Statement Templates for this profile, see that section.
`patterns` | *Optional*. The Patterns for this profile, see that section.



### Profile Version Objects

Name | Values
---- | ------
`@id` | The IRI of the version ID
`wasRevisionOf` | *Optional*. an array, usually of length one, of IRIs of all profile versions this version was written as a revision of
`generatedAtTime` | the date this version was created on

* wasRevisionOf MUST be used with all versions that succeed other profile versions.

Profile version objects make it convenient to track version history for profiles, following recommendations for SKOS concept schemes and PROV version tracking generally. By using versions this way, it is possible to answer precise questions such as “what version of this profile was current on the 3rd of January last year?”. Lack of robust versioning is frequently identified as an issue with RDF data.

### Organizations and Persons

Use one of these in the `author` property to indicate the author of this profile version.

Name | Values
---- | ------
`@type` | `Organization` or `Person`
`name` | A string with the name of the organization or person
`url` | *Optional*. A URL for the Person or Group.

## Concepts

* All members of a profile's `concepts` array MUST be one of the concepts listed in this section.

### Core Concepts: Verbs, Activity Types, and Attachment Usage Types

These Concepts are the most central to building rich, reusable profiles.

Name | Values
---- | ------
`@id` | The IRI of this core concept
`@type` | `Verb`, `ActivityType`, or `AttachmentUsageType`
`inScheme` | The IRI of the specific profile version currently being described
`prefLabel` | A language map of the preferred names in each language
`definition` | A language map of the precise definition, including how to use the concept properly in statements
`deprecated` | *Optional*. A boolean. If true, this concept is deprecated.
`broader` | *Optional*. An array of IRIs of concepts of the same @type from this profile version that have a broader meaning.
`narrower` | *Optional*. An array of IRIs of concepts of the same @type from this profile version that have a narrower meaning.
`broadMatch` | *Optional*. An array of IRIs of concepts of the same @type from a different profile that have a broader meaning.
`narrowMatch` | *Optional*. An array of IRIs of concepts of the same @type from different profiles that have narrower meanings.
`exactMatch` | *Optional*. An array of IRIs of concepts of the same @type from a different profile or a different version of the same profile that have exactly the same meaning. This should be used rarely, mostly to describe connections to vocabularies that are no longer managed and do not use good URLs.
`relatedMatch` | *Optional*. An array of IRIs of concepts of the same @type from a different profile or a different version of the same profile that has a related meaning that is not clearly narrower or broader. Useful to establish conceptual links between profiles that can be used for discovery. This SHOULD be used to connect possible replacement Concepts to removed Concepts from previous versions of the same profile, and for possible replacement Concepts in other profiles of deprecated concepts, as well as other loose relations.
`related` | *Optional*. An array of IRIs of concepts of the same @type from this profile version that are close conceptual matches to this concept's meaning. This property MUST only be used on concepts that are deprecated to indicate possible replacement concepts in the same profile, if there are any.

### Extensions


Name | Values
---- | ------
`@id` | The IRI of the extension, used as the extension key in xAPI
`@type` | `ContextExtension`, `ResultExtension`, or `ActivityExtension`
`inScheme` | The IRI of the specific profile version currently being described
`prefLabel` | A language map of descriptive names for the extension
`definition` | A language map of descriptions of the purpose and usage of the extension
`deprecated` | *Optional*. A boolean. If true, this concept is deprecated.
`recommendedActivityTypes` | *Optional*. Only allowed on `ActivityExtension`s. An array of activity type URIs that this extension is recommended for use with (extending to narrower of the same).
`recommendedVerbs` | *Optional*. Only allowed on `ContextExtension`s and `ResultExtension`s. An array of verb URIs that this extension is recommended for use with (extending to narrower of the same).
`context` | *Optional*. the IRI of a JSON-LD context for this extension
`schema` | *Optional*. the IRI for accessing a JSON Schema for this extension. The JSON Schema may constrain the extension to a single type.
`inlineSchema` | *Optional*. A JSON Schema inline. Must be a string that contains a legal JSON Schema.

* profiles MUST use at most one of `schema` and `inlineSchema` for Extensions.

Learning Record Providers MUST, for xAPI Statements using Extensions defined here, follow the following rules:
* a ContextExtension MUST only be used in context
* a ResultExtension MUST only be used in result
* an ActivityExtension MUST only be used in an Activity Definition.

### Document Resources

The @id MUST be used as the stateId or profileId (as appropriate) when interacting with the corresponding resource.


Name | Values
---- | ------
`@id` | The IRI of the document resource, used as the stateId/profileId in xAPI
`@type` | One of: `StateResource`, `AgentProfileResource`, `ActivityProfileResource`
`inScheme` | The IRI of the specific profile version currently being described
`prefLabel` | A language map of descriptive names for the document resource
`definition` | A language map of descriptions of the purpose and usage of the document resource
`contentType` | The content-type for the resource
`deprecated` | *Optional*. A boolean. If true, this concept is deprecated.
`context` | *Optional*. the IRI of a JSON-LD context for this document resource
`schema` | *Optional*. the IRI for accessing a JSON Schema for this document resource.
`inlineSchema` | *Optional*. A JSON Schema inline. Must be a string that contains a legal JSON Schema.

* profiles MUST use at most one of `schema` and `inlineSchema` for Document Resources


### Activities

These Concepts are just literal xAPI Activity definitions the profile wants to provide for use. This is the profile's canonical version of the Activity. Except for `@context`, the activityDefinition in this Concept MUST be a legal xAPI Activity Definition. When using the Activity, a Statement MUST use the `@id` for the Activity `id`, and MUST NOT include `@context` in the Activity definition. All other properties of the activityDefinition are considered part of the definition, and any Statement using the Activity SHOULD either not include the definition, or SHOULD include all properties given here in the definition exactly as given, except for `name` and `description` or other language maps, which SHOULD only include languages appropriate to the situation, possibly including ones not present in the profile yet.

Due to restrictions in JSON-LD, all extensions in the Activity definition that do not have primitive values (string, number, boolean, null, or arrays thereof) MUST include a JSON-LD @context in the top-level object, or in every top-level object if array-valued.

Name | Values
---- | ------
`@id` | The IRI of the activity
`@type` | `Activity`
`inScheme` | The IRI of the specific profile version currently being described
`deprecated` | *Optional*. A boolean. If true, this concept is deprecated.
`activityDefinition` | An Activity Definition as in xAPI, plus an @context, as in the table below.

Name | Values
---- | ------
`@context` | Must be TODO create an Activity context and host it at a URI.
`type` | *Optional*. As in xAPI Activity Definitions.
`name` | *Optional*. As in xAPI Activity Definitions.
`description` | *Optional*. As in xAPI Activity Definitions.
`moreInfo` | *Optional*. As in xAPI Activity Definitions.
`extensions` | *Optional*. As in xAPI Activity Definitions.
`interactionType` | *Optional*. As in xAPI Activity Definitions.
`correctResponsesPattern` | *Optional*. As in xAPI Activity Definitions.
`choices` | *Optional*. As in xAPI Activity Definitions.
`scale` | *Optional*. As in xAPI Activity Definitions.
`source` | *Optional*. As in xAPI Activity Definitions.
`target` | *Optional*. As in xAPI Activity Definitions.
`steps` | *Optional*. As in xAPI Activity Definitions.

## Statement Templates

A Statement Template describes one way statements following the profile may be structured. The verb, object activity type, attachment usage types, and context activity types listed are the determining properties. When authoring a statement to follow a template, a Learning Record Provider MUST include all the determining properties, as well as follow all rules in the template. Any statement including all the determining properties and using the profile version as a category context activity MUST follow the rules, object StatementRef property, and context StatementRef property.  We recommend picking one of the determining properties to use in all Statement Templates in a profile to be reused in Patterns, with different values in each, since this ensures each statement matches at most one Statement Template in a given profile. A profile SHOULD ensure each statement following any of its Statement Templates used in Patterns will match at most one Statement Template.

If a statement matches a Statement Template's determining values and uses the profile version as a category context activity, it MUST be sent as part of a Pattern or Implied Pattern.

Name | Values
---- | ------
`@id` | A URI for this Statement Template.
`@type` | `StatementTemplate`
`inScheme` | The IRI of the specific profile version currently being described
`prefLabel` | a language map of descriptive names for the Statement Template
`definition` | A language map of descriptions of the purpose and usage of the Statement Template
`allowedSolo` | *Optional*. A boolean, default false. If true, this Statement Template can be used as a single statement Implied Pattern (see that section). A Statement Template may be both used in Patterns and allowedSolo true.
`deprecated` | *Optional*. A boolean, default false. If true, this Statement Template is deprecated.
`verb` | *Optional*. Verb IRI
`objectActivityType` | *Optional*. Object activity type IRI
`contextGroupingActivityType` | *Optional*. Array of contextActivities grouping activity type IRIs
`contextParentActivityType` | *Optional*. Array of contextActivities parent activity type IRIs
`contextOtherActivityType` | *Optional*. Array of contextActivities other activity type IRIs
`contextCategoryActivityType` | *Optional*. Array of contextActivities category activity type IRIs
`attachmentUsageType` | *Optional*. Array of attachment usage type IRIs
`objectStatementRefTemplate` | *Optional*. An array of Statement Template identifiers from this profile version. May not be used with `objectActivityType`. If specified, the Statement object must be a StatementRef and the Learning Record Provider MUST make it the UUID of a Statement matching at least one of the specified Statement Templates.
`contextStatementRefTemplate`. *Optional*. An array of Statement Template identifiers from this profile version. If specified, the Statement context statement property must be a StatementRef and the Learning Record Provider MUST make it the UUID of a Statement matching at least one of the specified Statement Templates.
`rules` | *Optional*. Array of Statement Template Rules


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
`rule` | *Optional*. `included`, `excluded`, or `recommended`. If included, there must be at least one matchable value for this Statement Template Rule to be fulfilled, and if excluded, no matchable values. If `recommended`, this rule represents a recommended inclusion and `any`, `all`, and `none` requirements on the same rule are only applied if the results of looking up `location` are nonempty.
`any` | *Optional*. an array of values that are allowed in this location. Useful for constraining the presence of particular activities, for example. If the rule returns multiple values for a statement, then this Statement Template Rule is fulfilled if any one returned value matches any one specified value — that is, if the intersection is not empty.
`all` | *Optional*. an array of values, which all values returned by the JSONPath must match one of to fulfill this Statement Template Rule.
`none` | *Optional*. an array of values, which no values returned by the JSONPath may match to fulfill this Statement Template Rule.
`scopeNote` | *Optional*. A language map describing usage details for the parts of Statements addressed by this rule. For example, a profile with a rule requiring result.duration might provide guidance on how to calculate it.

A Statement Template Rule MUST include one or more of `rule`, `any`, `all`, or `none`.

When processing a statement for Statement Template Rules, it MUST have normalized contextActivities, with singletons replaced by arrays of length one.
The syntax of JSONPath is described at http://goessner.net/articles/JsonPath/index.html#e2, except filter and script expressions may not be used. The union operator (a comma) may be used inside array or child expressions, so the result is the union on each expression being used separately. The legal values in an array or child expression are: strings (child expressions), non-negative integers (array expressions), and the star character `*` representing all children/members. Effectively this means the `@` syntax is also illegal. TODO: consider allowing limited scripting a la https://github.com/json-path/JsonPath . TODO: consider if use cases require allowing a JSONPath expression to be a union of other JSONPath expressions.

### Statement References

I'm unsure enough how to do this I propose we do not include statement reference constraints in the initial draft. It would probably be included as a special case in the statement template rules, above.

## Patterns

Patterns are groups of statements matching particular statement templates, ordered in certain ways. For example, an allowed pattern in a video profile might start with a statement about playing a video and then be followed by statements about pausing, skipping, playing again, and so forth. A pattern is determined by a given registration, and possibly subregistration, a new extension. Specifically,

* all statements following a primary Pattern MUST use the same registration.
* when only one profile or only one pattern occurrence of each profile will be used, in a given registration, subregistrations SHOULD NOT be used.
* if any Statements following a primary Pattern do not contain a subregistration, all statements with the same registration and profile version in category MUST follow that primary Pattern.
* if any Statements with a given registration contain the subregistration extension, then all statements with that registration with the same subregistration identifier for a given profile version MUST follow the same primary Pattern.
* the extension key of the subregistration extension is https://TODO/REPLACE/WITH/REAL/ID (a value in the w3id xAPI space should be used for this).
* the subregistration extension MUST only be present in Statements with a registration.
* the subregistration extension is an array-valued context extension. The array MUST NOT be empty. Each value of the array MUST be an object with the properties in the table below.

Name | Values
---- | ------
`profile` | The URI of a profile present in the category context activities that this is a subregistration for.
`subregistration` | A variant 2 UUID as specified in RFC 4122. This is the subregistration identifier in the requirements above.


Patterns have these properties:


Name | Values
---- | ------
`@id` | A URI for the template.
`@type` | `Pattern`
`primary` | *Optional*. Boolean. Default false. Only primary patterns are checked for matching sequences of statements.
`inScheme` | The IRI of the specific profile version currently being described
`prefLabel` | A language map of descriptive names for the pattern
`definition` | A language map of descriptions of the purpose and usage of the pattern
`deprecated` | *Optional*. A boolean. If true, this pattern is deprecated.
`alternates` | *Optional*. A two-or-more length array of pattern or statement template identifiers. An alternates pattern matches if any member of the array matches
`optional` | *Optional*. A single pattern or statement template identifier. An optional pattern matches if the identified thing matches once, or is not present at all
`oneOrMore` | *Optional*. A single pattern or statement template identifier. A oneOrMore pattern matches if the identified thing matches once, or any number of times more than once
`sequence` | *Optional*. An two-or-more length array of pattern or statement template identifiers. A sequence pattern matches if the identified things match in the order specified.
`zeroOrMore` | *Optional*. A single pattern or statement template identifier. A zeroOrMore pattern matches if the identified thing is not present or is present one or more times


A primary pattern MUST include prefLabel and definition. They are optional otherwise.
A pattern MUST contain exactly one of `alternates`, `optional`, `oneOrMore`, `sequence`, and `zeroOrMore`.

A pattern MUST not refer to any pattern that has itself in the array or single value for any of `alternates`, `optional`, `oneOrMore`, `sequence`, or `zeroOrMore`, considered recursively.
A pattern only matches if it matches greedily. That is, each optional, zeroOrMore, oneOrMore, and alternate pattern MUST always be considered to match the maximum length possible before considering any patterns later in a sequence. That is, no backtracking is allowed. This constrains useful statement patterns, but guarantees efficient processing, as once a statement is matched it does not need to be reconsidered (except in cases where it is part of an ultimately unmatched alternate).
When checking previously collected statements for matching a pattern, ordering MUST be based on timestamp. In the event two or more statements have identical timestamps, any order within those statements is allowed.
When checking statements for matching a pattern upon receipt, ordering MUST be based on receipt order insofar as that can be determined. If statements are received in the same batch and they are being checked upon receipt, within the batch statements MUST be ordered first by timestamp, and if timestamps are the same, by order within the statement array, with lower indices earlier.

Some Profiles may contain Patterns very similar to Statement data sent by previously existing Learning Record Providers, not strictly following this specification. It may be very close, but not follow it in all particulars, such as by missing a registration. While the details of how to handle this are outside the scope of this specification, Profiles aware of such existing data SHOULD make note of this and include descriptive language covering the degree of adherence.

### Implied Patterns

If a Statement Template is allowed solo, Learning Record Providers MAY send it as an Implied Pattern. If it is not, Learning Record Providers MUST NOT send it as an Implied Pattern. An Implied Pattern MUST include the profile version in category, and MAY include a registration (and subregistration) as if it were described as a Pattern with a sequence of one statement template, but MAY leave off the registration (and subregistration).

When checking for pattern match of a Statement with a registration, if there is only one Statement for the registration and it matches a Statement Template that is allowed solo, it MUST be considered an Implied Pattern. Implied Patterns MUST NOT be used in Statements with registrations present in multiple statements.

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
failure | original statements  | pattern failed to match statements. Note: if an optional or zeroOrMore pattern is directly inside an alternates pattern, it is possible for failure to be returned when partial is correct, due to decidability issues. Profile authors SHOULD NOT put optional or zeroOrMore directly inside alternates.


### Libraries

Any library that implements the algorithms given here will be an xAPI Profile Processor library. Reference implementation libraries in one or more languages will be provided.

For each of the library operations, the Profile Server will provide web APIs that are strongly Not Recommended for production usage, but are suitable for experimentation and demonstration.

One URL will be at /validate_templates, and the other at /validate_patterns. The first will take a single xAPI statement and a profile specified by id, specified in POST variables as “statement” and “profile”. The second will take an array of xAPI statements and a profile specified by id, both specified in POST variables as “statements” and “profile”. Both will check if the single statement or sequence of statements matches any template or pattern in the profile given.

Both will perform the algorithms above and return 204 on successful validation and 400 on failure, with descriptive comments attached on failure.

TODO: figure out if the profile parameter is really needed, consider return values that are the array of profiles with a matching template or pattern, or maybe even the templates or patterns themselves?
