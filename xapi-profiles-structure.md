# xAPI Profiles Document Structure Specification

## Reference Specifications

* [http://json-ld.org](http://json-ld.org/)
* [https://www.w3.org/TR/skos-reference/](https://www.w3.org/TR/skos-reference/)
* [https://www.w3.org/TR/2013/REC-prov-dm-20130430/](https://www.w3.org/TR/2013/REC-prov-dm-20130430/)
* [https://www.w3.org/TR/activitystreams-core/](https://www.w3.org/TR/activitystreams-core/)
* [https://www.w3.org/TR/rdf-sparql-query/](https://www.w3.org/TR/rdf-sparql-query/)

## Technical Foundations

This specification describes how to author an xAPI Profile. It describes a set of rules for authoring JSON, specifically JSON-LD. Since JSON-LD is a syntax for RDF, the resulting profile is really a set of triples—subject, predicate, object—creating a semantic data set. However, for authoring, all that matters is following the rules given for JSON, which will lead to the richer semantic data naturally. Because of this, no JSON-LD processing is required by systems consuming xAPI Profiles, though there will be advantages to doing so for some purposes.

When a profile is serialized into JSON, it MUST be consistent with what would be produced by the standard JSON-LD 1.1 Processing Algorithms and API Compaction Algorithm using, at least, the normative JSON-LD @context definition provided. Following all the rules given in this document is sufficient to ensure that.

Under the hood, xAPI Profiles will use several well-established semantic web technologies: SKOS, to connect xAPI concepts together, and PROV, to describe the provenance (most notably the versioning) of profiles. Several properties in xAPI Profiles use names of properties from SKOS and PROV.

# Structure

Profiles serve two primary technical goals. First, they contain metadata about xAPI Concepts intended for reuse within statements, such as verbs and activity types. The metadata includes connections between Concepts, not just within the current profile, but also as used in other profiles, supporting a rich ecosystem of related terms. An xAPI Concept is any building block for use in Statements, and new versions of the profile specification may introduce new Concepts that can be described. The basis for xAPI Concepts is the SKOS Concept, a flexible way to refer to "specific ideas or meanings established within a knowledge organization system."

Second, they contain specific rules about using those Concepts properly in specific situations, both on how to form individual statements containing specific Concepts, and how to group those statements together in patterns of multiple statements. These rules allow profile authors to require specific elements, describe precise orderings, and many other options.

To assist in accomplishing these two primary goals, profiles also contain metadata about themselves—descriptions, authorship, versioning, and so forth.

## Document Interpretation and General Restrictions

* All properties in tables are required in all cases unless marked optional.
* Properties marked optional may be required in some situations. If no additional information is provided on the usage of an optional property, including it or not is entirely up to the profile author.
* All properties that are not JSON-LD keywords (or aliases thereof) MUST expand to absolute IRIs during processing as defined in the JSON-LD specification.
* All properties that are not JSON-LD keywords (or aliases thereof) and not described by this specification MUST be expressed using compact IRIs or full IRIs.
* JSON-LD keywords (or aliases thereof) that are not specified as properties in this document MAY be included anywhere they are legal in JSON-LD.
* Values in a profile MUST NOT be: empty objects, null, empty strings, or empty arrays.
* All requirements on the structure of Profiles MUST be followed by Profile Authors.
* All requirements on Statements following Profiles MUST be followed by Learning Record Providers when authoring Statements and by Profile Validators when validating Statements.

## Using Profiles in Statements

Using an introduced Concept, such as an activity type, verb, attachment usage type, extension, activity, or document resource, can be done freely, provided the defined usage and meaning are adhered to. But a Learning Record Provider can go further, and make sure to adhere to profile-described statement templates and patterns. Learning Record Providers authoring statements that conform to matching profile-described statement templates and patterns SHOULD include the most up-to-date conformant profile version as a category context activity with id equal to the version's `@id` in those statements, and statements containing a profile version as a category context activity MUST conform to any matching templates and patterns that profile version describes.

## Profile Properties

A Profile includes a variety of metadata, both natural language text for humans to understand the Profile, and structured data about versions and who created it. In addition to the metadata, there are properties for describing the Concepts, Statement Templates, and Patterns of the Profile.

Name | Values
---- | ------
`@id` | The IRI of the profile overall (not a specific version)
`@context` | SHOULD be `http://example.org/figure/out/where/this/goes/profile-context.jsonld` and MUST contain this URI if array-valued.
`@type` | Must be `Profile`.
`conformsTo` | Canonical URI of the profile specification version conformed to. The profile specification version of this document is https://github.com/DataInteroperability/xapi-profiles/tree/master#1.0-development, and it is a development version that may undergo incompatible changes without updating the version URI.
`prefLabel` | Language map of names for this profile.
`definition` | Language map of descriptions for this profile. If there are additional rules for the profile as a whole that cannot be expressed using this specification, include them here, or at the seeAlso URL.
`seeAlso` | *Optional*. A URL containing information about the profile. Recommended instead of especially long definitions.
`versions` | An array of all profile version objects for this profile, see below.
`author` | An Organization or Person, see below.
`concepts` | *Optional*. An array of Concepts that make up this Profile, see the Concepts section.
`templates` | *Optional*. An array of Statement Templates for this profile, see that section.
`patterns` | *Optional*. An array of Patterns for this profile, see that section.

When `seeAlso` is provided `definition` SHOULD only include a short description of the Profile to aid in discovery and display.

### Profile Version Objects

Profile version objects make it convenient to track version history for profiles, following recommendations for SKOS concept schemes and PROV version tracking generally. By using versions this way, it is possible to answer precise questions such as “what version of this profile was current on the 3rd of January last year?”. Lack of robust versioning is frequently identified as an issue with RDF data.


Name | Values
---- | ------
`@id` | The IRI of the version ID
`wasRevisionOf` | *Optional*. an array, usually of length one, of IRIs of all profile versions this version was written as a revision of
`generatedAtTime` | the date this version was created on

`wasRevisionOf` MUST be used with all versions that succeed other profile versions.

`wasRevisionOf` may sometimes contain multiple profile versions to support the scenario where a profile subsumes another. In this case, a new profile version would be defined with the two (or more) contributing profiles listed within the `wasRevisionOf` array.

### Organizations and Persons

Use one of these in the `author` property to indicate the author of this profile version.

Name | Values
---- | ------
`@type` | `Organization` or `Person`
`name` | A string with the name of the organization or person
`url` | *Optional*. A URL for the Person or Group.

## Concepts

All Concepts in a Profile MUST follow the rules of one of the subsections within this section. Since the types listed in each subsection are exclusive and required, that will always distinguish which section applies.

### Verbs, Activity Types, and Attachment Usage Types

Verb, Activity Type, and Attachment Usage Type Concepts share the same properties. They're all Concepts that make sense to relate semantically to others of the same type, such as indicating one is a narrower form of another.

Name | Values
---- | ------
`@id` | The IRI of this Concept
`@type` | `Verb`, `ActivityType`, or `AttachmentUsageType`
`inScheme` | The IRI of the specific profile version currently being described
`prefLabel` | A language map of the preferred names in each language
`definition` | A language map of the precise definition, including how to use the concept properly in statements
`deprecated` | *Optional*. A boolean. If true, this concept is deprecated.
`broader` | *Optional*. An array of IRIs of concepts of the same @type from this profile version that have a broader meaning.
`broadMatch` | *Optional*. An array of IRIs of concepts of the same @type from a different profile that have a broader meaning.
`narrower` | *Optional*. An array of IRIs of concepts of the same @type from this profile version that have a narrower meaning.
`narrowMatch` | *Optional*. An array of IRIs of concepts of the same @type from different profiles that have narrower meanings.
`related` | *Optional*. An array of IRIs of concepts of the same @type from this profile version that are close conceptual matches to this concept's meaning.
`relatedMatch` | *Optional*. An array of IRIs of concepts of the same @type from a different profile or a different version of the same profile that has a related meaning that is not clearly narrower or broader. Useful to establish conceptual links between profiles that can be used for discovery.
`exactMatch` | *Optional*. An array of IRIs of concepts of the same @type from a different profile or a different version of the same profile that have exactly the same meaning.

* `related` MUST only be used on concepts that are deprecated to indicate possible replacement concepts in the same profile, if there are any.
* `relatedMatch` SHOULD be used to connect possible replacement Concepts to removed Concepts from previous versions of the same profile, and for possible replacement Concepts in other profiles of deprecated concepts, as well as other loose relations.
* `exactMatch` SHOULD be used rarely, mostly to describe connections to vocabularies that are no longer managed and do not use good URLs.

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
`schema` | *Optional*. the IRI for accessing a JSON Schema for this extension. The JSON Schema can be used to constrain the extension to a single type.
`inlineSchema` | *Optional*. An alternate way to include a JSON Schema, as a string.

Profiles MUST use at most one of `schema` and `inlineSchema` for Extensions.

Statements including extensions defined in a Profile MUST:
* only use a ContextExtension in context
* only use a ResultExtension in result
* only use an ActivityExtension in an Activity Definition.

### Document Resources

Name | Values
---- | ------
`@id` | The IRI of the document resource, used as the stateId/profileId in xAPI
`@type` | One of: `StateResource`, `AgentProfileResource`, `ActivityProfileResource`
`inScheme` | The IRI of the specific profile version currently being described
`prefLabel` | A language map of descriptive names for the document resource
`definition` | A language map of descriptions of the purpose and usage of the document resource
`contentType` | The media type for the resource, as described in RFC 2046 (e.g. `application/json`).
`deprecated` | *Optional*. A boolean. If true, this concept is deprecated.
`context` | *Optional*. the IRI of a JSON-LD context for this document resource
`schema` | *Optional*. the IRI for accessing a JSON Schema for this document resource.
`inlineSchema` | *Optional*. An alternate way to include a JSON Schema, as a string.

Profiles MUST use at most one of `schema` and `inlineSchema` for Document Resources

Learning Record Store Clients sending Document Resources
* MUST use the @id as the stateId or profileId (as appropriate) when interacting with the corresponding resource.
* MUST use the contentType given in the Content-Type header, including any parameters as given.
* MAY add additional parameters to the Content-Type header that are not specified in the Concept.

Profile Validators receiving Document Resources MUST validate Learning Record Store Clients follow the requirements for Document Resources.


### Activities

These Concepts are just literal xAPI Activity definitions the profile wants to provide for use. This is the profile's canonical version of the Activity.


Name | Values
---- | ------
`@id` | The IRI of the activity
`@type` | `Activity`
`inScheme` | The IRI of the specific profile version currently being described
`deprecated` | *Optional*. A boolean. If true, this concept is deprecated.
`activityDefinition` | An Activity Definition as in xAPI, plus an `@context`, as in the table below.

Name | Values
---- | ------
`@context` | SHOULD be `http://example.org/host/somewhere/activity-context.jsonld` and MUST contain this URI if array-valued.
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

Except for `@context`, the activityDefinition in this Concept MUST be a legal xAPI Activity Definition.

Profile Authors:
* MUST include a JSON-LD `@context` in all top-level objects of extensions, or in every top-level object if array-valued. This is due to restrictions in JSON-LD, and is not applicable to extensions with primitive values (string, number, boolean, null, or arrays thereof).
* MUST ensure every extension `@context` is sufficient to guarantee all properties in the extension expand to absolute IRIs during JSON-LD processing.


Learning Record Providers using the Activity in Statements:
* MUST use the `@id` for the Activity `id`, and MUST NOT include `@context` in the Activity Definition.
* SHOULD either not include the definition or include all properties given here in the definition.
* if included, the properties SHOULD be exactly as given in the Profile, except for `name` and `description` and other Language Maps.
* Language Maps SHOULD only include languages appropriate to the situation.
* Language Maps MAY include languages not present in the profile yet.


## Statement Templates

A Statement Template describes one way statements following the profile may be structured.


Name | Values
---- | ------
`@id` | A URI for this Statement Template.
`@type` | `StatementTemplate`
`inScheme` | The IRI of the specific profile version currently being described
`prefLabel` | a language map of descriptive names for the Statement Template
`definition` | A language map of descriptions of the purpose and usage of the Statement Template
`deprecated` | *Optional*. A boolean, default false. If true, this Statement Template is deprecated.
`verb` | *Optional*. Verb IRI
`objectActivityType` | *Optional*. Object activity type IRI
`contextGroupingActivityType` | *Optional*. Array of contextActivities grouping activity type IRIs
`contextParentActivityType` | *Optional*. Array of contextActivities parent activity type IRIs
`contextOtherActivityType` | *Optional*. Array of contextActivities other activity type IRIs
`contextCategoryActivityType` | *Optional*. Array of contextActivities category activity type IRIs
`attachmentUsageType` | *Optional*. Array of attachment usage type IRIs
`objectStatementRefTemplate` | *Optional*. An array of Statement Template identifiers from this profile version.
`contextStatementRefTemplate`. | *Optional*. An array of Statement Template identifiers from this profile version.
`rules` | *Optional*. Array of Statement Template Rules

A Statement Template MUST NOT have both `objectStatementRefTemplate` and `objectActivityType`.

The verb, object activity type, attachment usage types, and context activity types listed are called Determining Properties.

A Learning Record Provider authoring a Statement following a Statement Template:
* MUST include all the Determining Properties in the Statement Template.
* MUST follow all rules in the Statement Template.
* MUST, if objectStatementRefTemplate is specified, set the Statement object to a StatementRef with the `id` of a Statement matching at least one of the specified Statement Templates.
* MUST, if contextStatementRefTemplate is specified, set the Statement context statement property to a StatementRef with the `id` of a Statement matching at least one of the specified Statement Templates.

A Profile Validator validating a Statement MUST validate all the Learning Record Provider requirements for a Statement Template are followed.

### Statement Template Rules

Statement Template Rules describe a location or locations within statements using JSONPath, then describe the restrictions on that value, such as inclusion, exclusion, or specific values allowed or disallowed. For example, to require at least one grouping, the rules might be something like:

```
"rules": [
    {
        "location": "context.contextActivities.grouping[*].id",
        "presence": "included"
    }
]
```

They have these properties:

Name | Values
---- | ------
`location` | A JSONPath string. This is evaluated on a Statement to find the evaluated values to apply the requirements in this rule to. All evaluated values from `location` are matchable values.
`selector` | *Optional*. A JSONPath string. If specified, this JSONPath is evaluated on each member of the evaluated values resulting from the location selector, and the resulting values become the evaluated values instead. If it returns nothing on a location, that represents an unmatchable value for that location, meaning `all` will fail, as will a `presence` of `included`. All other values returned are matchable values.
`presence` | *Optional*. `included`, `excluded`, or `recommended`.
`any` | *Optional*. an array of values that needs to intersect with the matchable values.
`all` | *Optional*. an array of values which all the evaluated values need to be from.
`none` | *Optional*. an array of values that can't be in the matchable values.
`scopeNote` | *Optional*. A language map describing usage details for the parts of Statements addressed by this rule. For example, a profile with a rule requiring result.duration might provide guidance on how to calculate it.

A Statement Template Rule MUST include one or more of `presence`, `any`, `all`, or `none`.

A Profile Author MUST include the keys of any non-primitive objects in `any`, `all`, and `none` in additional `@context` beyond the ones provided by this specification.

A Learning Record Provider authoring a Statement for the Statement Template including this Statement Template Rule:
* MUST include at least one matchable value if `presence` is `included`
* MUST NOT include any unmatchable values if `presence` is `included`
* MUST NOT include any matchable values if `presence` is `excluded`
* MUST apply the following requirements if `presence` is missing, if `presence` is `included`, or if `presence` is `recommended` and any matchable values are in the Statement:
    * MUST, if `any` is provided, include at least one value in `any` as one of the matchable values
    * MUST, if `all` is provided, only include values in `all` as matchable values
    * MUST NOT, if `all` is provided, include any unmatchable values
    * MUST NOT, if `none` is provided, include any values in `none` as matchable values

A Profile Validator validating Statements MUST validate the Statement Template Rule requirements for Learning Record Providers are followed. See the Communication document for further details on how to do so.


When validating a Statement for Statement Template Rules, contextActivities normalization MUST have already been performed as described in the Experience API specification. That is, singleton objects MUST be replaced by arrays of length one.

The syntax and behavior of JSONPath is described at http://goessner.net/articles/JsonPath/index.html#e2. In addition, the following requirements and clarifications apply:
* Filter and script expressions MUST NOT be used.
* The union operator (a comma) may be used inside array or child expressions, so the result is the union on each expression being used separately.
* The legal values in an array or child expression are: strings (child expressions), non-negative integers (array expressions), the star character `*` representing all children/members, and unions of these as described above.

## Patterns

Patterns describe groups of statements matching particular statement templates, ordered in certain ways. For example, an allowed pattern in a video profile might start with a statement about playing a video and then be followed by statements about pausing, skipping, playing again, and so forth.

Patterns have these properties:


Name | Values
---- | ------
`@id` | A URI for the template.
`@type` | `Pattern`
`primary` | *Optional*. Boolean. Default false. Only primary patterns are checked for matching sequences of statements.
`inScheme` | The IRI of the specific profile version currently being described
`prefLabel` | *Optional*. A language map of descriptive names for the pattern
`definition` | *Optional*. A language map of descriptions of the purpose and usage of the pattern
`deprecated` | *Optional*. A boolean. If true, this pattern is deprecated.
`alternates` | *Optional*. An array of pattern or statement template identifiers. An alternates pattern matches if any member of the array matches
`optional` | *Optional*. A single pattern or statement template identifier. An optional pattern matches if the identified thing matches once, or is not present at all
`oneOrMore` | *Optional*. A single pattern or statement template identifier. A oneOrMore pattern matches if the identified thing matches once, or any number of times more than once
`sequence` | *Optional*. An array of pattern or statement template identifiers. A sequence pattern matches if the identified things match in the order specified.
`zeroOrMore` | *Optional*. A single pattern or statement template identifier. A zeroOrMore pattern matches if the identified thing is not present or is present one or more times


A primary pattern MUST include prefLabel and definition. They are optional otherwise.

A pattern MUST contain exactly one of `alternates`, `optional`, `oneOrMore`, `sequence`, and `zeroOrMore`.



Profile Authors:
* MUST make sure their primary patterns behave appropriately given the greedy matching rules in the algorithms section.
* MUST NOT put optional or zeroOrMore directly inside alternates.
* MUST NOT include any pattern within itself, or within any pattern within itself, or at any depth.
* MUST include at least two members in `alternates`.
* MUST include at least two members in `sequence`, unless `sequence` is in a primary Pattern that is not used elsewhere and the member of `sequence` is a single Statement Template.

Learning Record Providers:
* MUST follow a Pattern from a Profile for every Statement that has the Profile in the category context activities.
* MUST send Statements following a Pattern ordered by Statement timestamp.
* MUST give Statements following a Pattern different timestamps if they are in different batches.
* SHOULD give all Statements following a Pattern different timestamps.
* MUST order Statements following a Pattern within the same batch with the same timestamp so ones intended to match earlier in the Pattern are earlier in the array than ones intended to match later in the Pattern
* MUST follow the rules given for a primary Pattern within a registration and possibly subregistration (a new extension). Specifically,
    * all statements following a primary Pattern MUST use the same registration.
    * when only one profile or only one pattern occurrence of each profile will be used, in a given registration, subregistrations SHOULD NOT be used.
    * if any Statements following a primary Pattern do not contain a subregistration, all statements with the same registration and profile version in category MUST follow that primary Pattern.
    * if any Statements with a given registration contain the subregistration extension, then all statements with that registration with the same subregistration identifier for a given profile version MUST follow the same primary Pattern.
    * the extension key of the subregistration extension is https://TODO/REPLACE/WITH/REAL/ID (a value in the w3id xAPI space will be used for this).
    * the subregistration extension MUST only be present in Statements with a registration.
    * the subregistration extension is an array-valued context extension. The array MUST NOT be empty. Each value of the array MUST be an object with the properties in the table below.

Profile Validators validating Statements MUST validate all the requirements for Learning Record Providers for Patterns have been followed. See the Communication document for further details on how to do so.


Name | Values
---- | ------
`profile` | The URI of a profile present in the category context activities that this is a subregistration for.
`subregistration` | A variant 2 UUID as specified in RFC 4122. This is the subregistration identifier in the requirements above.

Some Profiles may contain Patterns very similar to Statement data sent by previously existing Learning Record Providers, not strictly following this specification. It may be very close, but not follow it in all particulars, such as by missing a registration. While the details of how to handle this are outside the scope of this specification, Profiles aware of such existing data SHOULD make note of this and include descriptive language covering the degree of adherence.

## The Context

The way JSON-LD documents are mapped onto semantics is through what's called a context, which is specified with `@context`. Most of the time Profile authors and consumers do not need to worry about this at all -- this specification says what needs to go where, and provides the values to put in `@context` in the necessary places. In addition to being hosted at the given URLs, the contexts used are also in the repository this specification is developed in.
