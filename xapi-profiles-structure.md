Part Two:	[xAPI Profiles Document Structure Specification](./xapi-profiles-structure.md#parttwo)  
   *	1.0.	[Reference Specifications](./xapi-profiles-structure#1.0)
   *	2.0.	[Technical Foundations](./xapi-profiles-structure#2.0)
   *  3.0.  [Structure](./xapi-profiles-structure#3.0)
   *  4.0.  [Document Interpretation and General Restrictions](./xapi-profiles-structure.md#4.0)
   *  5.0.  [Using Profiles in Statements](./xapi-profiles-structure.md#5.0)
   *  6.0.  [Profile Properties](./xapi-profiles-structure.md#6.0)
      *  6.1.  [Profile Version Objects](./xapi-profiles-structure.md#6.1)
      *  6.2.  [Organizations and Persons](./xapi-profiles-structure.md#6.2)
   *  7.0.  [Concepts](./xapi-profiles-structure.md#7.0)
      *  7.1.  [Verbs, Activity Types, and Attachment Usage Types](./xapi-profiles-structure.md#7.1)
      *  7.2.  [Extensions](./xapi-profiles-structure.md#7.2)
      *  7.3.  [Document Resources](./xapi-profiles-structure.md#7.3)
      *  7.4.  [Activities](./xapi-profiles-structure.md#7.4)
   *  8.0.  [Statement Templates](./xapi-profiles-structure.md#8.0)
      *  8.1.  [Statement Template Rules](./xapi-profiles-structure.md#8.1)
   *  9.0.  [Patterns](./xapi-profiles-structure.md#9.0)
   *  10.0. [The Context](./xapi-profiles-structure.md#10.0)



<a name="parttwo"></a>
# Part Two: xAPI Profiles Document Structure Specification

## <a name="1.0">1.0</a> Reference Specifications

* [http://json-ld.org](http://json-ld.org/)
* [https://www.w3.org/TR/skos-reference/](https://www.w3.org/TR/skos-reference/)
* [https://www.w3.org/TR/2013/REC-prov-dm-20130430/](https://www.w3.org/TR/2013/REC-prov-dm-20130430/)
* [https://www.w3.org/TR/activitystreams-core/](https://www.w3.org/TR/activitystreams-core/)
* [https://www.w3.org/TR/rdf-sparql-query/](https://www.w3.org/TR/rdf-sparql-query/)

## <a name="2.0">2.0</a> Technical Foundations

This specification describes how to author an xAPI Profile. It describes a set of rules for authoring JSON, specifically JSON-LD. Since JSON-LD is a syntax for RDF, the resulting Profile is really a set of triples—subject, predicate, object—creating a semantic data set. However, for authoring, all that matters is following the rules given for JSON, which will lead to the richer semantic data naturally. Because of this, no JSON-LD processing is required by systems consuming xAPI Profiles, though there will be advantages to doing so for some purposes.

When a Profile is serialized into JSON, it MUST be consistent with what would be produced by the standard JSON-LD 1.1 Processing Algorithms and API Compaction Algorithm. The compaction must use, at least, the normative JSON-LD contexts provided with this specification. Following all the rules given in this document is sufficient to ensure that.

Under the hood, xAPI Profiles will use several well-established semantic web technologies: SKOS, to connect xAPI Concepts together, and PROV, to describe the provenance (most notably the versioning) of Profiles. Several properties in xAPI Profiles use names of properties from SKOS and PROV.

## <a name="3.0">3.0</a> Structure

Profiles serve two primary technical goals. First, they contain metadata about xAPI Concepts intended for reuse within Statements, such as verbs and activity types. The metadata includes connections between Concepts, not just within the current Profile, but also as used in other Profiles, supporting a rich ecosystem of related terms. An xAPI Concept is any building block for use in Statements, and new versions of the Profile specification may introduce new Concepts that can be described. The basis for xAPI Concepts is the SKOS Concept, a flexible way to refer to "specific ideas or meanings established within a knowledge organization system."

Second, they contain specific rules about using those Concepts properly in specific situations, both on how to form individual Statements containing specific Concepts, and how to group those Statements together in Patterns of multiple Statements. These rules allow Profile authors to require specific elements, describe precise orderings, and many other options.

To assist in accomplishing these two primary goals, Profiles also contain metadata about themselves—descriptions, authorship, versioning, and so forth.

## <a name="4.0">4.0</a> Document Interpretation and General Restrictions

* All properties in tables are required in all cases unless marked optional.
* Properties marked optional may be required in some situations. If no additional information is provided on the usage of an optional property, including it or not is entirely up to the Profile author.
* All properties that are not JSON-LD keywords (or aliases thereof) MUST expand to absolute IRIs during processing as defined in the JSON-LD specification.
* All properties that are not JSON-LD keywords (or aliases thereof) and not described by this specification MUST be expressed using compact IRIs or full IRIs.
* JSON-LD keywords (or aliases thereof) that are not specified as properties in this document MAY be included anywhere they are legal in JSON-LD.
* Values in a Profile MUST NOT be: empty objects, null, empty strings, or empty arrays.
* All requirements on the structure of Profiles MUST be followed by Profile Authors.
* All requirements on Statements following Profiles MUST be followed by Learning Record Providers when authoring Statements and by Profile Validators when validating Statements.

## <a name="5.0">5.0</a> Using Profiles in Statements

Using an introduced Concept, such as an activity type, verb, attachment usage type, extension, activity, or document resource, can be done freely, provided the defined usage and meaning are adhered to. But a Learning Record Provider can go further, and make sure to adhere to Profile-described Statement Templates and Patterns. Learning Record Providers authoring Statements that conform to matching Profile-described Statement Templates and Patterns SHOULD include the most up-to-date conformant Profile version as a category context activity with id equal to the version's `id` in those Statements, and Statements containing a Profile version as a category context activity MUST conform to any matching Statement Templates and Patterns that Profile version describes.

## <a name="6.0">6.0</a> Profile Properties

A Profile includes a variety of metadata, both natural language text for humans to understand the Profile, and structured data about versions and who created it. In addition to the metadata, there are properties for describing the Concepts, Statement Templates, and Patterns of the Profile.

Property | Type | Description | Required
-------- | ---- | ----------- | --------
`id` | IRI | The IRI of the Profile overall (not a specific version) | Required
`@context` | URI | SHOULD be `http://example.org/figure/out/where/this/goes/profile-context.jsonld` and MUST contain this URI if array-valued. | Required
`type` | String | MUST be `Profile`. | Required
`conformsTo` | URI | Canonical URI of the Profile specification version conformed to. The Profile specification version of this document is https://github.com/DataInteroperability/xapi-profiles/tree/master#1.0-development, and it is a development version that may undergo incompatible changes without updating the version URI. | Required
`prefLabel` | Object | Language map of names for this Profile. | Required
`definition` | Object | Language map of descriptions for this Profile. If there are additional rules for the Profile as a whole that cannot be expressed using this specification, include them here, or at the seeAlso URL. | Required
`seeAlso` | URL | A URL containing information about the Profile. Recommended instead of especially long definitions. | Optional
`versions` | Array | An array of all Profile version objects for this Profile, see below. | Required
`author` | Object | An Organization or Person, see below. | Required
`concepts` | Array | An array of Concepts that make up this Profile, see the Concepts section. | Optional
`templates` | Array | An array of Statement Templates for this Profile, see that section. | Optional
`patterns` | Array | An array of Patterns for this Profile, see that section. | Optional

When `seeAlso` is provided `definition` SHOULD only include a short description of the Profile to aid in discovery and display.

### <a name="6.1">6.1</a> Profile Version Objects


Profile version objects make it convenient to track version history for Profiles, following recommendations
for SKOS concept schemes and PROV version tracking generally. By using versions this way, it is possible to
answer precise questions such as “what version of this Profile was current on the 3rd of January last year?”.
Lack of robust versioning is frequently identified as an issue with RDF data.

Property | Type | Description | Required
-------- | ---- | ----------- | --------
`id` | IRI | The IRI of the version ID | Required
`wasRevisionOf` | Array | An array, usually of length one, of IRIs of all Profile versions this version was written as a revision of | Optional
`generatedAtTime` | Timestamp | The date this version was created on | Required

`wasRevisionOf` MUST be used with all versions that succeed other Profile versions.

`wasRevisionOf` may sometimes contain multiple Profile versions to support the scenario where a Profile subsumes another. In this case, a new Profile version would be defined with the two (or more) contributing Profiles listed within the `wasRevisionOf` array.

### <a name="6.2">6.2</a> Organizations and Persons

Use one of these in the `author` property to indicate the author of this Profile version.

Property | Type | Description | Required
-------- | ---- | ----------- | --------
`type` | Object | `Organization` or `Person` | Required
`name` | String | A string with the name of the organization or person | Required
`url` | URL | A URL for the Person or Group. | Optional

## <a name="7.0">7.0</a> Concepts

Concepts are building blocks for use and reuse in xAPI data and other Profiles. In the case of Verbs, Activity Types,  Attachment Usage Types, and Activities, the Concept is "the thing", and when you use that Concept in xAPI you're using it directly. In the case of Document Resources and Extensions, the Concept is "the shape of the thing" that the identifier can be used to point at, and will be used with many different values xAPI data.

A Profile MUST NOT define a Concept that is defined in another Profile unless it supersedes all versions of the other Profile containing the Concept and indicates that in with `wasRevisionOf`.

All Concepts in a Profile MUST follow the rules of one of the subsections within this section. Since the types listed in each subsection are exclusive and required, that will always distinguish which section applies.

### <a name="7.1">7.1</a> Verbs, Activity Types, and Attachment Usage Types

Verb, Activity Type, and Attachment Usage Type Concepts share the same properties. They're all Concepts that make sense to relate semantically to others of the same type, such as indicating one is a narrower form of another.

Property | Type | Description | Required
-------- | ---- | ----------- | --------
`id` | IRI | The IRI of this Concept | Required
`type` | String | `Verb`, `ActivityType`, or `AttachmentUsageType` | Required
`inScheme` | IRI | The IRI of the specific Profile version currently being described | Required
`prefLabel` | Object | A language map of the preferred names in each language | Required
`definition` | Object | A language map of the precise definition, including how to use the Concept properly in Statements | Required
`deprecated` | Boolean | A boolean. If true, this Concept is deprecated. | Optional
`broader` | Array | An array of IRIs of Concepts of the same `type` from this Profile version that have a broader meaning. | Optional
`broadMatch` | Array | An array of IRIs of Concepts of the same `type` from a different Profile that have a broader meaning. | Optional
`narrower` | Array | An array of IRIs of Concepts of the same `type` from this Profile version that have a narrower meaning. | Optional
`narrowMatch` | Array | An array of IRIs of Concepts of the same `type` from different Profiles that have narrower meanings. | Optional
`related` | Array | An array of IRIs of Concepts of the same `type` from this Profile version that are close conceptual matches to this Concept's meaning. | Optional
`relatedMatch` | Array | An array of IRIs of Concepts of the same `type` from a different Profile or a different version of the same Profile that has a related meaning that is not clearly narrower or broader. Useful to establish conceptual links between Profiles that can be used for discovery. | Optional
`exactMatch` | Array | An array of IRIs of Concepts of the same `type` from a different Profile or a different version of the same Profile that have exactly the same meaning. | Optional

* `related` MUST only be used on Concepts that are deprecated to indicate possible replacement Concepts in the same Profile, if there are any.
* `relatedMatch` SHOULD be used to connect possible replacement Concepts to removed Concepts from previous versions of the same Profile, and for possible replacement Concepts in other Profiles of deprecated Concepts, as well as other loose relations.
* `exactMatch` SHOULD be used rarely, mostly to describe connections to vocabularies that are no longer managed and do not use good URLs.

### <a name="7.2">7.2</a> Extensions


Property | Type | Description | Required
-------- | ---- | ----------- | --------
`id` | IRI | The IRI of the extension, used as the extension key in xAPI | Required
`type` | String | `ContextExtension`, `ResultExtension`, or `ActivityExtension` | Required
`inScheme` | IRI | The IRI of the specific Profile version currently being described | Required
`prefLabel` | Object | A language map of descriptive names for the extension | Required
`definition` | Object | A language map of descriptions of the purpose and usage of the extension | Required
`deprecated` | Boolean | A boolean. If true, this Concept is deprecated. | Optional
`recommendedActivityTypes` | Array | Only allowed on `ActivityExtension`s. An array of activity type URIs that this extension is recommended for use with (extending to narrower of the same). | Optional
`recommendedVerbs` | Array | Only allowed on `ContextExtension`s and `ResultExtension`s. An array of verb URIs that this extension is recommended for use with (extending to narrower of the same). | Optional
`context` | IRI | the IRI of a JSON-LD context for this extension |  Optional
`schema` | IRI | the IRI for accessing a JSON Schema for this extension. The JSON Schema can be used to constrain the extension to a single type. | Optional
`inlineSchema` | Object | An alternate way to include a JSON Schema, as a string. | Optional

Profiles MUST use at most one of `schema` and `inlineSchema` for Extensions.

Statements including extensions defined in a Profile MUST:
* only use a ContextExtension in context
* only use a ResultExtension in result
* only use an ActivityExtension in an Activity Definition.

### <a name="7.3">7.3</a> Document Resources

Property | Type | Description | Required
-------- | ---- | ----------- | --------
`id` | IRI | The IRI of the document resource, used as the stateId/profileId in xAPI | Required
`type` | String | One of: `StateResource`, `AgentProfileResource`, `ActivityProfileResource` | Required
`inScheme` | IRI | The IRI of the specific Profile version currently being described | Required
`prefLabel` | Object | A language map of descriptive names for the document resource | Required
`definition` | Object | A language map of descriptions of the purpose and usage of the document resource | Required
`contentType` | String | The media type for the resource, as described in RFC 2046 (e.g. `application/json`). | Required
`deprecated` | Boolean | A boolean. If true, this Concept is deprecated. | Optional
`context` | IRI | The IRI of a JSON-LD context for this document resource. | Optional
`schema` | IRI | the IRI for accessing a JSON Schema for this document resource. | Optional
`inlineSchema` | String | An alternate way to include a JSON Schema, as a string. | Optional

Profiles MUST use at most one of `schema` and `inlineSchema` for Document Resources

Learning Record Store Clients sending Document Resources
* MUST use the `id` as the stateId or profileId (as appropriate) when interacting with the corresponding resource.
* MUST use the contentType given in the Content-Type header, including any parameters as given.
* MAY add additional parameters to the Content-Type header that are not specified in the Concept.
* MUST
    * only send a StateResource to a State Resource location
    * only send an AgentProfileResource to an Agent Profile Resource location
    * only send an ActivityProfileResource to an Activity Profile Resource location

Profile Validators receiving Document Resources MUST validate Learning Record Store Clients follow the requirements for Document Resources.


### <a name="7.4">7.4</a> Activities

These Concepts are just literal xAPI Activity definitions the Profile wants to provide for use. This is the Profile's canonical version of the Activity.


Property | Type | Description | Required
-------- | ---- | ----------- | --------
`id` | IRI | The IRI of the activity | Required
`type` | String | `Activity` | Required
`inScheme` | IRI | The IRI of the specific Profile version currently being described | Required
`deprecated` | Boolean | A boolean. If true, this Concept is deprecated. | Optional
`activityDefinition` | Object | An Activity Definition as in xAPI, plus a `@context`, as in the table below. | Required

Name | Values
---- | ------
`@context` | SHOULD be `http://example.org/host/somewhere/activity-context.jsonld` and MUST contain this URI if array-valued.
*other properties* | All as in xAPI 1.0.x Activity Definitions, defined at https://github.com/adlnet/xAPI-Spec/blob/master/xAPI-Data.md#activity-definition

Except for `@context`, the activityDefinition in this Concept MUST be a legal xAPI Activity Definition.

Profile Authors:
* MUST include a JSON-LD `@context` in all top-level objects of extensions, or in every top-level object if array-valued. This is due to restrictions in JSON-LD, and is not applicable to extensions with primitive values (string, number, boolean, null, or arrays thereof).
* MUST ensure every extension `@context` is sufficient to guarantee all properties in the extension expand to absolute IRIs during JSON-LD processing.


Learning Record Providers using the Activity in Statements:
* MUST use the `id` for the Activity `id`, and MUST NOT include `@context` in the Activity Definition.
* SHOULD either not include the definition or include all properties given here in the definition.
* if included, the properties SHOULD be exactly as given in the Profile, except for `name` and `description` and other Language Maps.
* Language Maps SHOULD only include languages appropriate to the situation.
* Language Maps MAY include languages not present in the Profile yet.


## <a name="8.0">8.0</a> Statement Templates

A Statement Template describes one way Statements following the Profile may be structured.


Property | Type | Description | Required
-------- | ---- | ----------- | --------
`id` | A URI for this Statement Template. | Required
`type` | `StatementTemplate` | Required
`inScheme` | The IRI of the specific Profile version currently being described | Required
`prefLabel` | Object |A language map of descriptive names for the Statement Template | Required
`definition` | Object |A language map of descriptions of the purpose and usage of the Statement Template | Required
`deprecated` | Boolean | A boolean, default false. If true, this Statement Template is deprecated. | Optional
`verb` | IRI | Verb IRI | Optional
`objectActivityType` | Object | Object activity type IRI | Optional
`contextGroupingActivityType` | Array | Array of contextActivities grouping activity type IRIs | Optional
`contextParentActivityType` | Array | Array of contextActivities parent activity type IRIs | Optional
`contextOtherActivityType` | Array | Array of contextActivities other activity type IRIs | Optional
`contextCategoryActivityType` | Array | Array of contextActivities category activity type IRIs | Optional
`attachmentUsageType` | Array | Array of attachment usage type IRIs | Optional
`objectStatementRefTemplate` | Array | An array of Statement Template identifiers from this Profile version. | Optional
`contextStatementRefTemplate`. | Array | An array of Statement Template identifiers from this Profile version. | Optional
`rules` | Array | Array of Statement Template Rules | Optional

A Statement Template MUST NOT have both `objectStatementRefTemplate` and `objectActivityType`.

The verb, object activity type, attachment usage types, and context activity types listed are called Determining Properties.

A Profile Author MUST change a Statement Template's `id` between versions if any of the Determining Properties, StatementRef properties, or rules change. Changes of `scopeNote` are not considered changes in rules.

A Learning Record Provider authoring a Statement following a Statement Template:
* MUST include all the Determining Properties in the Statement Template.
* MUST follow all rules in the Statement Template.
* MUST, if objectStatementRefTemplate is specified, set the Statement object to a StatementRef with the `id` of a Statement matching at least one of the specified Statement Templates.
* MUST, if contextStatementRefTemplate is specified, set the Statement context Statement property to a StatementRef with the `id` of a Statement matching at least one of the specified Statement Templates.

A Profile Validator validating a Statement MUST validate all the Learning Record Provider requirements for a Statement Template are followed.

### <a name="8.1">8.1</a> Statement Template Rules

Statement Template Rules describe a location or locations within Statements using JSONPath, then describe the restrictions on that value, such as inclusion, exclusion, or specific values allowed or disallowed. For example, to require at least one grouping, the rules might be something like:

```
"rules": [
    {
        "location": "context.contextActivities.grouping[*].id",
        "presence": "included"
    }
]
```

They have these properties:

Property | Type | Description | Required
-------- | ---- | ----------- | --------
`location` | String | A JSONPath string. This is evaluated on a Statement to find the evaluated values to apply the requirements in this rule to. All evaluated values from `location` are matchable values. | Required
`selector` | String | A JSONPath string. If specified, this JSONPath is evaluated on each member of the evaluated values resulting from the location selector, and the resulting values become the evaluated values instead. If it returns nothing on a location, that represents an unmatchable value for that location, meaning `all` will fail, as will a `presence` of `included`. All other values returned are matchable values. | Optional
`presence` | String | `included`, `excluded`, or `recommended`. | Optional
`any` | Array | An array of values that needs to intersect with the matchable values. | Optional
`all` | Array | An array of values which all the evaluated values need to be from. | Optional
`none` | Array | An array of values that can't be in the matchable values. | Optional
`scopeNote` | Object | A language map describing usage details for the parts of Statements addressed by this rule. For example, a Profile with a rule requiring result.duration might provide guidance on how to calculate it. | Optional

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

The syntax and behavior of JSONPath is described at http://goessner.net/articles/JsonPath/index.html#e2. In addition, the following requirements, clarifications, and additions apply:
* Filter and script expressions MUST NOT be used.
* The union operator (a comma) may be used inside array or child expressions, so the result is the union on each expression being used separately.
* The legal values in an array or child expression are: strings (child expressions), non-negative integers (array expressions), the star character `*` representing all children/members, and unions of these as described above.
* Any two or more legal JSONPath expressions, joined together by the pipe character `|`, optionally with whitespace around the pipe, are also considered a legal JSONPath expression. The value of this expression is all the values returned by each expression individually, flattened (that is, if one expression returns N values and another returns a single value, the combination returns N+1 values, not two values).

## <a name="9.0">9.0</a> Patterns

Patterns describe groups of Statements matching particular Statement Templates, ordered in certain ways. For example, a Pattern in a video Profile might start with a Statement about playing a video and then be followed by Statements about pausing, skipping, playing again, and so forth.

Patterns have these properties:


Property | Type | Description | Required
-------- | ---- | ----------- | --------
`id` | URI | A URI for the Statement Template. | Required
`type` | String | `Pattern` | Required
`primary` | Boolean | Default false. Only primary Patterns are checked for matching sequences of Statements. | Optional
`inScheme` | IRI | The IRI of the specific Profile version currently being described | Optional
`prefLabel` | Object | A language map of descriptive names for the Pattern | Optional
`definition` | Object | A language map of descriptions of the purpose and usage of the Pattern | Optional
`deprecated` | Boolean | A boolean. If true, this Pattern is deprecated. | Optional
`alternates` | Array | An array of Pattern or Statement Template identifiers. An alternates Pattern matches if any member of the array matches | Optional
`optional` | Object | A single Pattern or Statement Template identifier. An optional Pattern matches if the identified thing matches once, or is not present at all | Optional
`oneOrMore` | Object | A single Pattern or Statement Template identifier. A oneOrMore Pattern matches if the identified thing matches once, or any number of times more than once | Optional
`sequence` | Array | An array of Pattern or Statement Template identifiers. A sequence Pattern matches if the identified things match in the order specified. | Optional
`zeroOrMore` | Object | A single Pattern or Statement Template identifier. A zeroOrMore Pattern matches if the identified thing is not present or is present one or more times | Optional


A primary Pattern MUST include prefLabel and definition. They are optional otherwise.

A Pattern MUST contain exactly one of `alternates`, `optional`, `oneOrMore`, `sequence`, and `zeroOrMore`.

A Profile Author MUST change a Pattern's `id` between versions if any of `alternates`, `optional`, `oneOrMore`, `sequence`, or `zeroOrMore` change. Note that if a Pattern used within another Pattern changes, the change will "bubble up" as each `id` gets changed.

Profile Authors:
* MUST make sure their primary Patterns behave appropriately given the greedy matching rules in the algorithms section.
* MUST NOT put optional or zeroOrMore directly inside alternates.
* MUST NOT include any Pattern within itself, or within any Pattern within itself, or at any depth.
* MUST include at least two members in `alternates`.
* MUST include at least two members in `sequence`, unless `sequence` is in a primary Pattern that is not used elsewhere and the member of `sequence` is a single Statement Template.
* MAY re-use Statement Templates from other Profiles in Patterns. In this case, validating is done as if the Statement Template were present in this Profile.

Learning Record Providers:
* MUST follow a Pattern from a Profile for every Statement that has the Profile in the category context activities.
* MUST send Statements following a Pattern ordered by Statement timestamp.
* MUST give Statements following a Pattern different timestamps if they are in different batches.
* SHOULD give all Statements following a Pattern different timestamps.
* MUST order Statements following a Pattern within the same batch with the same timestamp so ones intended to match earlier in the Pattern are earlier in the array than ones intended to match later in the Pattern
* MUST follow the rules given for a primary Pattern within a registration and possibly subregistration (a new extension). Specifically,
    * all Statements following a primary Pattern MUST use the same registration.
    * when only one Profile or only one Pattern occurrence of each Profile will be used, in a given registration, subregistrations SHOULD NOT be used.
    * if any Statements following a primary Pattern do not contain a subregistration, all Statements with the same registration and Profile version in category MUST follow that primary Pattern.
    * if any Statements with a given registration contain the subregistration extension, then all Statements with that registration with the same subregistration identifier for a given Profile version MUST follow the same primary Pattern.
    * the extension key of the subregistration extension is https://TODO/REPLACE/WITH/REAL/ID (a value in the w3id xAPI space will be used for this).
    * the subregistration extension MUST only be present in Statements with a registration.
    * the subregistration extension is an array-valued context extension. The array MUST NOT be empty. Each value of the array MUST be an object with the properties in the table below.

Profile Validators validating Statements MUST validate all the requirements for Learning Record Providers for Patterns have been followed. See the Communication document for further details on how to do so.


Name | Values
---- | ------
`profile` | The URI of a Profile present in the category context activities that this is a subregistration for.
`subregistration` | A variant 2 UUID as specified in RFC 4122. This is the subregistration identifier in the requirements above.

Some Profiles may contain Patterns very similar to Statement data sent by previously existing Learning Record Providers, not strictly following this specification. It may be very close, but not follow it in all particulars, such as by missing a registration. While the details of how to handle this are outside the scope of this specification, Profiles aware of such existing data SHOULD make note of this and include descriptive language covering the degree of adherence.

## <a name="10.0">10.0</a> The Context

The way JSON-LD documents are mapped onto semantics is through what's called a context, which is specified with `@context`. Most of the time Profile authors and consumers do not need to worry about this at all -- this specification says what needs to go where, and provides the values to put in `@context` in the necessary places. In addition to being hosted at the given URLs, the contexts used are also in the repository this specification is developed in.
