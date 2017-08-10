# xAPI Profiles

* Part One: [About xAPI Profiles](#partone)
   *  1.0. [Introduction](#introduction-partone)
   *  2.0. [How to Use This Document](#how-to-use-partone)
      *  2.1. [MUST / SHOULD / MAY](./xapi-profiles.md#def-must-should-may)
      *  2.2. [Guidelines for Interpreting Descriptive Text and Tables](./xapi-profiles.md#interpret-text-table)
   *  3.0. [Definitions](./xapi-profiles.md#definitions)
* Part Two:	[xAPI Profiles Document Structure Specification](./xapi-profiles.md#parttwo)  
   *	1.0.	[Reference Specifications](./xapi-profiles.md#1.0)
   *	2.0.	[Technical Foundations](./xapi-profiles.md#2.0)
   *  3.0.  [Structure](./xapi-profiles.md#3.0)
   *  4.0.  [Document Interpretation and General Restrictions](./xapi-profiles.md#4.0)
   *  5.0.  [Using Profiles in Statements](./xapi-profiles.md#5.0)
   *  6.0.  [Profile Properties](./xapi-profiles.md#6.0)
      *  6.1.  [Profile Version Objects](./xapi-profiles.md#6.1)
      *  6.2.  [Organizations and Persons](./xapi-profiles.md#6.2)
   *  7.0.  [Concepts](./xapi-profiles.md#7.0)
      *  7.1.  [Verbs, Activity Types, and Attachment Usage Types](./xapi-profiles.md#7.1)
      *  7.2.  [Extensions](./xapi-profiles.md#7.2)
      *  7.3.  [Document Resources](./xapi-profiles.md#7.3)
      *  7.4.  [Activities](./xapi-profiles.md#7.4)
   *  8.0.  [Statement Templates](./xapi-profiles.md#8.0)
      *  8.1.  [Statement Template Rules](./xapi-profiles.md#8.1)
   *  9.0.  [Patterns](./xapi-profiles.md#9.0)
   *  10.0. [The Context](./xapi-profiles.md#10.0)
* Part Three:	[xAPI Profiles Communication and Processing Specification](./xapi-profiles.md#partthree)  
   * 1.0. [Profile Server](./xapi-profiles.md#1.0)
      * 1.1. [Profile Versions](./xapi-profiles.md#profile_versions)
      * 1.2. [Best Practices](xapi-profiles.md#profile_server_best_practices)
      * 1.3. [Example SPARQL Queries](xapi-profiles.md#1.3)
   * 2.0. [Algorithms](./xapi-profiles.md#2.0)
      * 2.1. [Statement Template Validation](./xapi-profiles.md#2.1)
      * 2.2. [Pattern Validation](./xapi-profiles.md#2.2)
  * 3.0. [Libraries](./xapi-profiles.md#libraries)

>#### License
>
>"Copyright 2017 Advanced Distributed Learning (ADL) Initiative, U.S. Department of Defense
>
>Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except
>in compliance with the License. You may obtain a copy of the License at
>http://www.apache.org/licenses/LICENSE-2.0
>
>Unless required by applicable law or agreed to in writing, software distributed under the License
>is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
>or implied. See the License for the specific language governing permissions and limitations under
>the License."
>
>This document was authored by the Data Interoperability Standards Consortium (DISC) under contract with ADL,
>reviewed and vetted by members of the xAPI Profiles Working Group in support of the Office of the
>Deputy Assistant Secretary of Defense (Readiness) Advanced Distributed Learning (ADL) Initiative. Please
>send all feedback and inquiries to helpdesk@adlnet.gov  

## Table of Contents

<a name="partone"></a>
# Part One: About xAPI Profiles

<a name="introduction-partone"></a>
## 1.0 Introduction

The Experience API (xAPI) Profiles Specification is a technical document that aims to
improve practices for creating Profiles as defined in the xAPI Specification. The xAPI
Profiles Specification lays out a structure that describes profiles uniformly, describes
how profiles can be discovered and reused, and how profiles can be published and managed.

Since the release of xAPI Version 1.0, institutions across industries employed xAPI to
track learning experiences of individuals beyond formal, structured computer-based training.
Now, as adoption of the xAPI specification expands, concerns about how adopters work with
profiles to support semantic interoperability are apparent. How semantic interoperability
has been addressed (and sometimes not) in practice, to-date, illustrates the set of challenges
this documents aims to address. The challenges are assumed as follows:

1. **Data meant to reflect the same activity often doesn’t match.** As xAPI champions data alignment
from multiple sources, in practice many products create activity statements that are intended to
reflect the same human activity, but are formatted different enough as to prove difficult to
analyze correctly. This is because these varying learning activity providers don’t communicate
effectively about how they express human activities with xAPI.

2. **Communities of Practice lack shared practices in their definitions of human activity,
performance and outcomes.** Communities of Practice at the scale of industry verticals (e.g.
military, medical, compliance, trade groups, etc.) have historically approached measurement,
even observation, of human activity in subjective, human-based terms. Our xAPI CoPs are often
defining and storing their profiles in different ways and at different levels of granularity.
Without consistency in how they are written and stored, it is challenging to make use of the
profile data.

Therefore, the goals of the xAPI Profiles Specification are to

* Offer a common way to express controlled vocabularies.
* Provide instruction on xAPI Statement formation.
* Describe patterns of xAPI Statements which are meaningful in some way to a profile.

xAPI Profiles rely on linked data technologies to achieve these goals. If you are
unfamiliar with linked data, the following article is recommended for all audiences (technical
and not-as-technical):

[Linked Data Explained: You’re No Dummy (2015)](https://www.lib.umich.edu/blogs/library-tech-talk/linked-data-explained-you’re-no-dummy)

>“Linked data has been a hot topic lately for both web developers and librarians.
>But unless you are highly technical, many of the online definitions for linked data might
>make your eyes glaze over and wonder just what exactly is this thing everyone is talking about.
>Don’t worry - you are not a dummy. But computers definitely are, which is exactly why we need
>linked data on the web...”

<a name="how-to-use-partone">## 2.0</a> How to Use This Document 


This is a definitive document which describes how the xAPI Profiles are to be implemented.
It is a technical document authored specifically for individuals and organizations implementing this
technology with the intent of such individuals developing interoperable tools, systems and services that
are independent of each other and interoperable with each other.

Whenever possible, the language and formatting used in this document is intended to be
_considerate_ of non-technical readers because various tools, systems and services
are based on the specification set described below. For this reason, sections that provide a
_high-level overview_ of a given facet of the Experience API are labeled **description** or
**rationale**. Items in this document labeled as **requirements**, **details** or **examples** are more technical.

This specification is split into three parts. Part one is this introduction. It offers some background,
high-level summaries and direction on how to read the rest of the specification.

Part two of this specification defines a structure for the data objects used in this specification.
This part helps to ensure that services implementing this specification follow a consistent data structure.

Part three of this specification sets out the communication methods that can be used when seeking information
about xAPI Profiles among services that adhere to the specification.


### <a name="def-must-should-may">2.1</a> MUST / SHOULD / MAY
There are three levels of obligation with regards to conformance to the xAPI specification identified by the terms
MUST, SHOULD and MAY. A service or system that fails to implement a MUST (or a MUST NOT) requirement is non-conformant.
Failing to meet a SHOULD requirement is not a violation of conformity, but goes against the recommendations of the specification.
MAY indicates an option, to be decided by the developer with no consequences for conformity. Usage
of these terms outside of requirement language does not designate a requirement and is avoided whenever possible.
Complete definitions of MUST, SHOULD, MAY, MUST NOT and SHOULD NOT are found in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

The use of an asterisk* following SHOULD indicates a very strong recommendation. It is planned that these
recommendations will become MUST requirements in a future version. Not following these recommendations could
risk interoperability and and/or lead to various other issues depending on the specifics of the recommendation.
These recommendations cannot be MUST requirements within this version as these would be breaking changes.
The xAPI Working Group strongly encourages adopters to implement these requirements as though they were MUST
requirements, while continuing to support other adopters that might not do so.


### <a name="interpret-text-table">2.2</a> Guidelines for Interpreting Descriptive Text and Tables
As a rule of thumb, if the guideline appears technical or seems to be a requirement, interpret it
as such. This is especially true of longer, more, detailed explanations and of tables, each of which would
be unintuitive and/or lengthy to dissect into a list of requirements.

Tables are used throughout this specification to define requirements for lists of properties, parameters, etc.
The tables define which properties are required, recommended and optional. Generally, the notion of "optional" relates to
the service creating the object, while services receiving and interpreting the object need to be able to interpret all
properties of that object. Often, properties are optional because the data may not be relevant in every context;
if the data is relevant in a particular context, then it is expected the property will be populated.

If an optional property or parameter contains an object with properties that are recommended or required, then
these properties are only recommended/required if the property or parameter containing them is used.

Examples are provided throughout the specification and in appendices to illustrate implementation. The content of these
examples is fictional in order to illustrate the requirements of the specification and may not always
illustrate the best practice approach to tracking the particular learning experience used in the example. Examples
can be used to inform interpretation of requirements, but are not intended to take precedence over requirements.

Where the specification does not include requirements relating to a particular facet of implementation,
that detail can be considered to be outside of the scope of this specification. It is up to the implementer
to determine a sensible approach. This specification tries to avoid vagueness and will usually give a rationale
even if there no requirement in a given area.

## <a name="definitions">3.0</a> Definitions


* [Absolute IRI](#absoluteiri)
* [Activity](#activity)
* [Activity Definition](#activitydefinition)
* [Activity Type](#activitytype)
* [Attachment Usage Type](#attachmentusagetype)
* [Compact IRI](#compactiri)
* [Concept](#concept)
* [Context](#context)
* [Document Resource](#documentresource)
* [Experience API (xAPI)](#xapi)
* [Extension](#extension)
* [IRI](#iri)
* [JSON](#json)
* [JSON Schema](#jsonschema)
* [JSON-LD](#jsonld)
* [JSONPath](#jsonpath)
* [Language Map](#languagemap)
* [Learning Record Provider](#learningrecordprovider)
* [Media Type](#mediatype)
* [Pattern](#pattern)
* [Profile](#profile)
* [Profile Author](#profileauthor)
* [Profile Server](#profileserver)
* [Profile Validator](#profilevalidator)
* [Profile version](#profileversion)
* [PROV](#prov)
* [RDF](#rdf)
* [Registration](#registration)
* [SKOS](#skos)
* [SPARQL](#sparql)
* [Statement](#statement)
* [Statement Template](#statementtemplate)
* [StatementRef](#statementref)
* [Subregistration](#subregistration)
* [Verb](#verb)
* [xAPI Profile Processor Library](#library)

<a name="absoluteiri"></a>**Absolute IRI**: an IRI. [Used in the JSON-LD specification](https://www.w3.org/TR/json-ld/#dfn-absolute-iri) to contrast with compact IRIs and relative IRIs.

<a name="activity"></a>**Activity**: an [Experience API Activity](https://github.com/adlnet/xAPI-Spec/blob/master/xAPI-Data.md#2441-when-the-objecttype-is-activity). This specification helps Profile Authors mint canonical Activities.

<a name="activitydefinition"></a>**Activity Definition**: an [Experience API Activity Definition](https://github.com/adlnet/xAPI-Spec/blob/master/xAPI-Data.md#activity-definition).

<a name="activitytype"></a>**Activity Type**: an [Experience API Activity Type](https://github.com/adlnet/xAPI-Spec/blob/master/xAPI-Data.md#activity-definition). This specification helps Profile Authors provide additional metadata for Activity Types they control.

<a name="attachmentusagetype"></a>**Attachment Usage Type**: an [Experience API Attachment Usage Type](https://github.com/adlnet/xAPI-Spec/blob/master/xAPI-Data.md#2411-attachments). This specification helps Profile Authors provide additional metadata for Attachment Usage Types they control.

<a name="compactiri"></a>**Compact IRI**: A shortened IRI in the form `prefix:name` that becomes expanded on processing to an absolute IRI. [Described in the JSON-LD specification](https://www.w3.org/TR/json-ld/#compact-iris).

<a name=concept""></a>**Concept**: In SKOS, any unit of thought. In this specification, any of a particular list of possible things a Profile might describe.

<a name="context"></a>**Context**: In xAPI this refers to a part of a Statement, but in this specification it usually means a [JSON-LD `@context`](https://www.w3.org/TR/json-ld/#the-context), which is a way of mapping JSON onto semantic terms and RDF.

<a name="documentresource"></a>**Document Resource**: An [Experience API Document Resource](https://github.com/adlnet/xAPI-Spec/blob/master/xAPI-Communication.md#22-document-resources). This specification helps Profile Authors describe what Document Resources in particular locations need to look like.

<a name="xapi"></a>**Experience API (xAPI)**: The [Experience API Specification](https://github.com/adlnet/xAPI-Spec). For this specification, any 1.0.x version is relevant. Describes data structures for describing experiences and APIs for communicating them.

<a name="extension"></a>**Extension**: An [Experience API Extension](https://github.com/adlnet/xAPI-Spec/blob/master/xAPI-Data.md#miscext). This specification helps Profile Authors describe what Extensions with specific identifiers need to look like.

<a name="iri"></a>**IRI**: An [Internationalized Resource Identifier](https://www.ietf.org/rfc/rfc3987.txt). Like a URL, but more general. A distributed, structured, persistent identifier.

<a name="json"></a>**JSON**: [JavaScript Object Notation](http://www.json.org). A simple way to represent data structures for computers that humans don't have too hard a time writing or reading. The way Profiles are represented in this specification.

<a name="jsonschema"></a>**JSON Schema**: [JSON Schema](http://json-schema.org) are a way to describe and constrain the form of JSON documents.

<a name="jsonld"></a>**JSON-LD**: [JSON-LD](https://json-ld.org) turns JSON into Linked Data, making it easy to use with Linked Data tools and integrate with other datasets.

<a name="jsonpath"></a>**JSONPath**: [JSONPath](http://goessner.net/articles/JsonPath/index.html#e2) provides a way to address parts of JSON documents using a `JSONPath expression`.

<a name="languagemap"></a>**Language Map**: A Language Map expresses multiple language-specific values at once. While used in the xAPI specification essentially identically, the controlling specification is [JSON-LD Language Maps](https://www.w3.org/TR/json-ld/#language-maps).

<a name="learningrecordprovider"></a>**Learning Record Provider**: As in the Experience API specification, anything creating Learning Records (xAPI Statements and Document Resources).

<a name="mediatype"></a>**Media Type**: A [media type](https://www.iana.org/assignments/media-types/media-types.xhtml) is a simple, structured way to refer to particular types of content. Also known as MIME Type or Content Type.

<a name="pattern"></a>**Pattern**: One way a series of Statements following a Profile could look. Defined by this specification.

<a name="profile"></a>**Profile**: What this specification focuses on. A profile is a way to talk about Concepts, Statement Templates, and Patterns for Experience API data in a particular context, and in particular to describe them so machines can do some processing automatically.

<a name="profileauthor"></a>**Profile Author**: Some person or group writing a Profile.

<a name="profileserver"></a>**Profile Server**: A place to find and browse Profiles.

<a name="profilevalidator"></a>**Profile Validator**: Any person or machine attempting to verify if the rules in a Profile are followed for a particular set of data.

<a name="profileversion"></a>**Profile version**: A Profile at a particular point in time.

<a name="prov"></a>**PROV**: [PROV](https://www.w3.org/TR/prov-overview/) models the provenance of things. In this specification, PROV is used to provide rich versioning support.

<a name="rdf"></a>**RDF**: The [Resource Description Framework](https://www.w3.org/RDF/) standardizes the exchange of semantic data by describing an information model of subject, predicate, and object.

<a name="registration"></a>**Registration**: An [Experience API Registration](https://github.com/adlnet/xAPI-Spec/blob/master/xAPI-Data.md#2461-registration-property). This specification uses registration to connect Statements that are following the same Pattern or Patterns.

<a name="skos"></a>**SKOS**: The [Simple Knowledge Organization System](https://www.w3.org/TR/2009/REC-skos-reference-20090818/) provides the building blocks to describe and relate Concepts.

<a name="sparql"></a>**SPARQL**: [SPARQL](https://www.w3.org/TR/sparql11-overview/) is a query language for RDF data.

<a name="statement"></a>**Statement**: An [Experience API Statement](https://github.com/adlnet/xAPI-Spec/blob/master/xAPI-Data.md#statements). The core unit of recorded data in the Experience API.

<a name="statementtemplate"></a>**Statement Template**: A set of rules for how Statements using certain Concepts should look. Defined by this specification.

<a name="statementref"></a>**StatementRef**: An [Experience API Statement Reference](https://github.com/adlnet/xAPI-Spec/blob/master/xAPI-Data.md#statement-references). Used for pointing at a second Statement from a first.

<a name="subregistration"></a>**Subregistration**: When multiple Patterns are being followed within a registration, subregistration is an extension specific to this specification to distinguish between them.

<a name="verb"></a>**Verb**: An [Experience API Verb](https://github.com/adlnet/xAPI-Spec/blob/master/xAPI-Data.md#verb). This specification helps Profile Authors provide additional metadata about verbs they control.

<a name="library"></a>**xAPI Profile Processor Library**: A programming library implementing the algorithms described in this specification.

<a name="parttwo"></a>
# Part Two: xAPI Profiles Document Structure Specification

## <a name="1.0">1.0</a> Reference Specifications

* [http://json-ld.org](http://json-ld.org/)
* [https://www.w3.org/TR/skos-reference/](https://www.w3.org/TR/skos-reference/)
* [https://www.w3.org/TR/2013/REC-prov-dm-20130430/](https://www.w3.org/TR/2013/REC-prov-dm-20130430/)
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
* All properties that are not JSON-LD keywords (or aliases thereof) and not described by this specification MUST be expressed using compact IRIs or absolute IRIs.
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
`@context` | URI | SHOULD be `https://w3id.org/xapi/profiles/context` and MUST contain this URI if array-valued. | Required
`type` | String | MUST be `Profile`. | Required
`conformsTo` | URI | Canonical URI of the Profile specification version conformed to. The Profile specification version of this document is https://w3id.org/xapi/profiles#1.0. | Required
`prefLabel` | Object | Language map of names for this Profile. | Required
`definition` | Object | Language map of descriptions for this Profile. If there are additional rules for the Profile as a whole that cannot be expressed using this specification, include them here, or at the seeAlso URL. | Required
`seeAlso` | URL | A URL containing information about the Profile. Recommended instead of especially long definitions. | Optional
`versions` | Array | An array of all [Profile version](#6.1) objects for this Profile. | Required
`author` | Object | An [Organization or Person](#6.2). | Required
`concepts` | Array | An array of [Concepts](#7.0) that make up this Profile. | Optional
`templates` | Array | An array of [Statement Templates](#8.0) for this Profile. | Optional
`patterns` | Array | An array of [Patterns](#9.0) for this Profile. | Optional

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

#### Examples

A Profile that's been revised twice will have an array of Profile versions that looks something like:

```javascript
[
    {
        "id": "http://example.com/profiles/superheroes/v3",
        "wasRevisionOf": ["http://example.com/profiles/superheroes/v2"],
        "generatedAtTime": "2020-02-20T20:20:20Z"
    },
    {
        "id": "http://example.com/profiles/superheroes/v2",
        "wasRevisionOf": ["http://example.com/profiles/superheroes/v1"],
        "generatedAtTime": "2010-01-15T03:14:15Z"
    },
    {
        "id": "http://example.com/profiles/superheroes/v1",
        "generatedAtTime": "2010-01-14T12:13:14Z"
    }
]
```

Note: there is nothing special about the URI structure, such as the use of "v#" on the end. Any URIs are legal, so long as every Profile version `id` is unique and different from the overall Profile URI. Using a predictable URI structure is  a good idea, though.


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
`prefLabel` | Object | A Language Map of the preferred names in each language | Required
`definition` | Object | A Language Map of the precise definition, including how to use the Concept properly in Statements | Required
`deprecated` | Boolean | A boolean. If true, this Concept is deprecated. | Optional
`broader` | Array | An array of IRIs of Concepts of the same `type` from this Profile version that have a broader meaning. | Optional
`broadMatch` | Array | An array of IRIs of Concepts of the same `type` from a different Profile that have a broader meaning. | Optional
`narrower` | Array | An array of IRIs of Concepts of the same `type` from this Profile version that have a narrower meaning. | Optional
`narrowMatch` | Array | An array of IRIs of Concepts of the same `type` from different Profiles that have narrower meanings. | Optional
`related` | Array | An array of IRIs of Concepts of the same `type` from this Profile version that are close to this Concept's meaning. | Optional
`relatedMatch` | Array | An array of IRIs of Concepts of the same `type` from a different Profile or a different version of the same Profile that has a related meaning that is not clearly narrower or broader. Useful to establish conceptual links between Profiles that can be used for discovery. | Optional
`exactMatch` | Array | An array of IRIs of Concepts of the same `type` from a different Profile or a different version of the same Profile that have exactly the same meaning. | Optional

* `related` MUST only be used on Concepts that are deprecated to indicate possible replacement Concepts in the same Profile, if there are any.
* `relatedMatch` SHOULD be used to connect possible replacement Concepts to removed Concepts from previous versions of the same Profile, and for possible replacement Concepts in other Profiles of deprecated Concepts, as well as other loose relations.
* `exactMatch` SHOULD be used rarely, mostly to describe connections to vocabularies that are no longer managed and do not use good URLs.

#### Examples

A Profile for competitive events might have verbs in it such as:

```javascript
{
    "id": "http://example.org/profiles/sports/verbs/placed",
    "type": "Verb",
    "inScheme": "http://example.org/profiles/sports/v2",
    "prefLabel": {
        "en": "placed"
    },
    "definition": {
        "en": "Indicates a person finished the event in a ranked order. \
        Use with the 'placement' extension."
    },
    "broadMatch": ["http://adlnet.gov/expapi/verbs/completed"]
}
```

The use of `broadMatch` means that the ADL's `completed` verb is a more general term than `placed`.

```javascript
{
    "id": "http://example.org/profiles/sports/verbs/medaled",
    "type": "Verb",
    "inScheme": "http://example.org/profiles/sports/v2",
    "prefLabel": {
        "en": "medaled"
    },
    "definition": {
        "en": "Indicates a person received a medal in a particular event. \
        Use with the 'placement' extension."
    },
    "broader": ["http://example.org/profiles/sports/verbs/placed"]
}
```

`broader` here works like `broadMatch` did above, but is used instead because the two verbs are in the same Profile.


```javascript
{
    "id": "http://example.org/profiles/sports/verbs/qualified",
    "type": "Verb",
    "inScheme": "http://example.org/profiles/sports/v2",
    "prefLabel": {
        "en": "qualified"
    },
    "definition": {
        "en": "Indicates a person is eligible for the event in the object."
    },
    "relatedMatch": ["https://w3id.org/xapi/adl/verbs/satisfied"]
}
```

Qualifying for an event isn't the same as (or broader or narrower than) satisfying it's requirements in the way meant in the ADL profile, but they're related concepts. By creating `relatedMatch` links a Profile makes it easier for people using Profiles to discover appropriate terms.


### <a name="7.2">7.2</a> Extensions


Property | Type | Description | Required
-------- | ---- | ----------- | --------
`id` | IRI | The IRI of the extension, used as the extension key in xAPI | Required
`type` | String | `ContextExtension`, `ResultExtension`, or `ActivityExtension` | Required
`inScheme` | IRI | The IRI of the specific Profile version currently being described | Required
`prefLabel` | Object | A Language Map of descriptive names for the extension | Required
`definition` | Object | A Language Map of descriptions of the purpose and usage of the extension | Required
`deprecated` | Boolean | A boolean. If true, this Concept is deprecated. | Optional
`recommendedActivityTypes` | Array | Only allowed on an `ActivityExtension`. An array of activity type URIs that this extension is recommended for use with (extending to narrower of the same). | Optional
`recommendedVerbs` | Array | Only allowed on a `ContextExtension` or a `ResultExtension`. An array of verb URIs that this extension is recommended for use with (extending to narrower of the same). | Optional
`context` | IRI | the IRI of a JSON-LD context for this extension |  Optional
`schema` | IRI | the IRI for accessing a JSON Schema for this extension. The JSON Schema can be used to constrain the extension to a single type. | Optional
`inlineSchema` | Object | An alternate way to include a JSON Schema, as a string. | Optional

Profiles MUST use at most one of `schema` and `inlineSchema` for Extensions.

Statements including extensions defined in a Profile MUST:
* only use a ContextExtension in context
* only use a ResultExtension in result
* only use an ActivityExtension in an Activity Definition.

#### Example

A Profile for competitive events might define an extension to represent placing, such as

```javascript
{
    "id": "http://example.org/profiles/sports/extensions/place",
    "type": "ResultExtension",
    "inScheme": "http://example.org/profiles/sports/v2",
    "prefLabel": {
        "en": "placement"
    },
    "definition": {
        "en": "Defines the place a person received in an event. \
        The value is an object with a required numerical rank \
        and an optional medal as a string"
    },
    "recommendedVerbs": [
        "http://example.org/profiles/sports/verbs/placed"
    ],
    "inlineSchema": "{ \"type\": \"object\", \"properties\":{ \
        \"rank\": {\"type\": \"number\", \"required\": true}, \
        \"medal\": {\"type\": \"string\"}}}"
}
```

This extension includes a JSON Schema that systems handling Statements with it can use to validate the structure of extension values. Also, it recommends a verb to use it with. While it only mentions the `placed` verb, if the `medaled` verb is defined as given above, it is narrower than `placed` and is recommended as well.



### <a name="7.3">7.3</a> Document Resources

Property | Type | Description | Required
-------- | ---- | ----------- | --------
`id` | IRI | The IRI of the document resource, used as the stateId/profileId in xAPI | Required
`type` | String | One of: `StateResource`, `AgentProfileResource`, `ActivityProfileResource` | Required
`inScheme` | IRI | The IRI of the specific Profile version currently being described | Required
`prefLabel` | Object | A Language Map of descriptive names for the document resource | Required
`definition` | Object | A Language Map of descriptions of the purpose and usage of the document resource | Required
`contentType` | String | The media type for the resource, as described in RFC 2046 (e.g. `application/json`). | Required
`deprecated` | Boolean | A boolean. If true, this Concept is deprecated. | Optional
`context` | IRI | The IRI of a JSON-LD context for this document resource. | Optional
`schema` | IRI | the IRI for accessing a JSON Schema for this document resource. | Optional
`inlineSchema` | String | An alternate way to include a JSON Schema, as a string. | Optional

Profiles MUST use at most one of `schema` and `inlineSchema` for Document Resources

Learning Record Store Clients sending Document Resources
* MUST use the `id` as the `stateId` or `profileId` (as appropriate) when interacting with the corresponding resource.
* MUST use the `contentType` given in the Content-Type header, including any parameters as given.
* MAY add additional parameters to the Content-Type header that are not specified in the Concept.
* MUST
    * only send a StateResource to a State Resource location
    * only send an AgentProfileResource to an Agent Profile Resource location
    * only send an ActivityProfileResource to an Activity Profile Resource location

Profile Validators receiving Document Resources MUST validate Learning Record Store Clients follow the requirements for Document Resources.

#### Example

A Profile for competitive events might include a way to store preferred t-shirt sizes for competitors, to help in prefilling race forms.

```javascript
{
    "id": "http://example.org/profiles/sports/resources/tshirt",
    "type": "AgentProfileResource",
    "inScheme": "http://example.org/profiles/sports/v2",
    "prefLabel": {
        "en": "T-Shirt Preference"
    },
    "definition": {
        "en": "Stores a t-shirt preference for prefilling race registrations."
    },
    "contentType": "application/json",
    "inlineSchema": "{ \"type\": \"object\", \"properties\": { \
        \"cut\": {\"enum\": [\"straight\", \"fitted\"], \"required\": true}, \
        \"size\": {\"enum\": [\"x-small\", \"small\", \"medium\", \"large\", \
            \"x-large\", \"2x-large\", \"3x-large\"], \"required\": true}}}"
}
```

This looks much like the `placement` extension, with the addition of `contentType` and without any recommended verbs.


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
`@context` | SHOULD be `https://w3id.org/xapi/profiles/activity-context` and MUST contain this URI if array-valued.
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


#### Examples

A Profile for competitive events might define Activities to represent standardized events, such as the 100 meter dash:

```javascript
{
    "id": "http://example.org/profiles/sports/activities/100mdash",
    "type": "Activity",
    "inScheme": "http://example.org/profiles/sports/v2",
    "activityDefinition": {
        "@context": "https://w3id.org/xapi/profiles/activity-context"
        "type": "http://example.org/profiles/sports/activitytypes/event"
        "name": {
            "en": "100 Meter Dash"
        },
        "description": {
            "en": "Represents the 100 meter dash as a general category of race. \
            When this is in the 'grouping' contextActivities of a Statement, \
            that means the Statement is about a particular 100 meter dash \
            that is the object Activity."
        }
    }
}
```

The `description` includes guidance on how to interpret this Activity's use in Statements, which also serves as guidance on how to use it.

## <a name="8.0">8.0</a> Statement Templates

A Statement Template describes one way Statements following the Profile may be structured.


Property | Type | Description | Required
-------- | ---- | ----------- | --------
`id` | A URI for this Statement Template. | Required
`type` | `StatementTemplate` | Required
`inScheme` | The IRI of the specific Profile version currently being described | Required
`prefLabel` | Object |A Language Map of descriptive names for the Statement Template | Required
`definition` | Object |A Language Map of descriptions of the purpose and usage of the Statement Template | Required
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
* MUST, if `objectStatementRefTemplate` is specified, set the Statement object to a StatementRef with the `id` of a Statement matching at least one of the specified Statement Templates.
* MUST, if `contextStatementRefTemplate` is specified, set the Statement context Statement property to a StatementRef with the `id` of a Statement matching at least one of the specified Statement Templates.

A Profile Validator validating a Statement MUST validate all the Learning Record Provider requirements for a Statement Template are followed.

### <a name="8.1">8.1</a> Statement Template Rules

Statement Template Rules describe a location or locations within Statements using JSONPath, then describe the restrictions on the value(s) there, such as inclusion, exclusion, or specific values allowed or disallowed. For example, to require at least one grouping, the rules might be something like:

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
`scopeNote` | Object | A Language Map describing usage details for the parts of Statements addressed by this rule. For example, a Profile with a rule requiring result.duration might provide guidance on how to calculate it. | Optional

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


When validating a Statement for Statement Template Rules, `contextActivities` normalization MUST have already been performed as described in the Experience API specification. That is, singleton objects MUST be replaced by arrays of length one.

The syntax and behavior of JSONPath is described at http://goessner.net/articles/JsonPath/index.html#e2. In addition, the following requirements, clarifications, and additions apply:
* Filter and script expressions MUST NOT be used.
* The union operator (a comma) may be used inside array or child expressions, so the result is the union on each expression being used separately.
* The legal values in an array or child expression are: strings (child expressions), non-negative integers (array expressions), the star character `*` representing all children/members, and unions of these as described above.
* Any two or more legal JSONPath expressions, joined together by the pipe character `|`, optionally with whitespace around the pipe, are also considered a legal JSONPath expression. The value of this expression is all the values returned by each expression individually, flattened (that is, if one expression returns N values and another returns a single value, the combination returns N+1 values, not two values).

#### Example

A Profile for competitive events might define a Statement Template for recording the outcomes of events:

```javascript
{
    "id": "http://example.org/profiles/sports/templates/placing",
    "type": "StatementTemplate",
    "inScheme": "http://example.org/profiles/sports/v2",
    "prefLabel": {
        "en": "Placing"
    },
    "definition": {
        "en": "Records the actor placing in a particular event. \
        The object is the specific event participated in, and an Activity \
        representing the general type of event goes in grouping \
        contextActivities."
    },
    "verb": "http://example.org/profiles/sports/verbs/placed",
    "objectActivityType":
        "http://example.org/profiles/sports/activitytypes/event",
    "contextGroupingActivityType": [
        "http://example.org/profiles/sports/activitytypes/event"],
    "rules": [
        {
            "location":
                "$.result.extensions['http://example.org/profiles/sports/extensions/place']",
            "presence": "included"
        }
    ]
}
```



## <a name="9.0">9.0</a> Patterns

Patterns describe groups of Statements matching particular Statement Templates, ordered in certain ways. For example, a Pattern in a video Profile might start with a Statement about playing a video and then be followed by Statements about pausing, skipping, playing again, and so forth.

Patterns have these properties:


Property | Type | Description | Required
-------- | ---- | ----------- | --------
`id` | URI | A URI for the Statement Template. | Required
`type` | String | `Pattern` | Required
`primary` | Boolean | Default false. Only primary Patterns are checked for matching sequences of Statements. | Optional
`inScheme` | IRI | The IRI of the specific Profile version currently being described | Optional
`prefLabel` | Object | A Language Map of descriptive names for the Pattern | Optional
`definition` | Object | A Language Map of descriptions of the purpose and usage of the Pattern | Optional
`deprecated` | Boolean | A boolean. If true, this Pattern is deprecated. | Optional
`alternates` | Array | An array of Pattern or Statement Template identifiers. An `alternates` Pattern matches if any member of the array matches | Optional
`optional` | Object | A single Pattern or Statement Template identifier. An `optional` Pattern matches if the identified thing matches once, or is not present at all | Optional
`oneOrMore` | Object | A single Pattern or Statement Template identifier. A `oneOrMore` Pattern matches if the identified thing matches once, or any number of times more than once | Optional
`sequence` | Array | An array of Pattern or Statement Template identifiers. A `sequence` Pattern matches if the identified things match in the order specified. | Optional
`zeroOrMore` | Object | A single Pattern or Statement Template identifier. A `zeroOrMore` Pattern matches if the identified thing is not present or is present one or more times | Optional


A primary Pattern MUST include `prefLabel` and `definition`. They are optional otherwise.

A Pattern MUST contain exactly one of `alternates`, `optional`, `oneOrMore`, `sequence`, and `zeroOrMore`.

A Profile Author MUST change a Pattern's `id` between versions if any of `alternates`, `optional`, `oneOrMore`, `sequence`, or `zeroOrMore` change. Note that if a Pattern used within another Pattern changes, the change will "bubble up" as each `id` gets changed.

Profile Authors:
* MUST make sure their primary Patterns behave appropriately given the [greedy matching rules in the algorithms section](./xapi-profiles-communication.md#2.2).
* MUST NOT put `optional` or `zeroOrMore` directly inside alternates.
* MUST NOT include any Pattern within itself, or within any Pattern within itself, or at any depth.
* MUST include at least two members in `alternates`.
* MUST include at least two members in `sequence`, unless `sequence` is in a primary Pattern that is not used elsewhere and the member of `sequence` is a single Statement Template.
* MAY re-use Statement Templates from other Profiles in Patterns. In this case, validating is done as if the Statement Template were present in this Profile.
* MAY re-use Patterns from other Profiles in Patterns. In this case, validating is done as if the Pattern were present in this Profile.

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
    * the extension key of the subregistration extension is https://w3id.org/xapi/profiles/extensions/subregistration.
    * the subregistration extension MUST only be present in Statements with a registration.
    * the subregistration extension is an array-valued context extension. The array MUST NOT be empty. Each value of the array MUST be an object with the properties in the table below.

Profile Validators validating Statements MUST validate all the requirements for Learning Record Providers for Patterns have been followed. See the Communication document for further details on how to do so.


Name | Values
---- | ------
`profile` | The URI of a Profile present in the category context activities that this is a subregistration for.
`subregistration` | A variant 2 UUID as specified in RFC 4122. This is the subregistration identifier in the requirements above.

Some Profiles may contain Patterns very similar to Statement data sent by previously existing Learning Record Providers, not strictly following this specification. It may be very close, but not follow it in all particulars, such as by missing a registration. While the details of how to handle this are outside the scope of this specification, Profiles aware of such existing data SHOULD make note of this and include descriptive language covering the degree of adherence.

#### Examples

A Profile for competitive events could define a primary Pattern and other associated Patterns for recording the running of a relay race.

```javascript
{
    "id": "http://example.org/profiles/sports/patterns/relay",
    "type": "Pattern",
    "primary": true,
    "inScheme": "http://example.org/profiles/sports/v2",
    "prefLabel": {
        "en": "Relay Race"
    },
    "definition": {
        "en": "A detailed recording of a relay race by a team in track and \
        field. The actor of the `start` Statement should be the single runner \
        who starts, and the actor of the `placed` Statement \
        should be a Group of the entire team."
    },
    "sequence": [
        "http://example.org/profiles/sports/templates/start",
        "http://example.org/profiles/sports/patterns/handoffs",
        "http://example.org/profiles/sports/templates/placing"
    ]
}
```

The primary Pattern for a relay race, it says a sequence of things happens: first, there's a Statement matching the `start` template (not defined in the examples), then there's a Pattern of `handoffs`, as defined next, and then there's a Statement matching the `placing` template (defined in an earlier example).

```javascript
{
    "id": "http://example.org/profiles/sports/patterns/handoffs",
    "type": "Pattern",
    "inScheme": "http://example.org/profiles/sports/v2",
    "definition": "The actor of each `handoff` Statement should be the runner \
    receiving the baton, as described in that Statement Template.",
    "oneOrMore": "http://example.org/profiles/sports/templates/handoff"
}
```

The Pattern for `handoffs` is pretty simple--there's one or more of Statements matching the `handoff` template. There's a definition on this Pattern even though it isn't required since it isn't primary, to aid people in using it.

In a real Profile these Patterns would be more complicated, accounting for various disqualifications, for example.

A common sort of occurrence will be the possibility of someone taking a "redo" of some section of an experience. For example, a Profile for a game supporting "redo" of levels after doing them the first time might have a Pattern like the following:

```javascript
{
    "id": "http://example.org/profiles/examplegame/patterns/levels",
    "type": "Pattern",
    "inScheme": "http://example.org/profiles/examplegame/v1",
    "sequence": [
        "http://example.org/profiles/examplegame/patterns/level1",
        "http://example.org/profiles/examplegame/patterns/level1redos",
        "http://example.org/profiles/examplegame/patterns/level2",
        "http://example.org/profiles/examplegame/patterns/uptolevel2redos",
        "http://example.org/profiles/examplegame/patterns/level3",
        "http://example.org/profiles/examplegame/patterns/uptolevel3redos"
    ]
}
```

The `levels` Pattern shows both the progression of levels and the possible redos between levels.

```javascript
{
    "id": "http://example.org/profiles/examplegame/patterns/level1redos",
    "type": "Pattern",
    "inScheme": "http://example.org/profiles/examplegame/v1",
    "zeroOrMore": "http://example.org/profiles/examplegame/patterns/level1"
}
```

Level 1 redos are simple--the only level that can be redone is level 1.

```javascript
{
    "id": "http://example.org/profiles/examplegame/patterns/uptolevel2redos",
    "type": "Pattern",
    "inScheme": "http://example.org/profiles/examplegame/v1",
    "zeroOrMore": "http://example.org/profiles/examplegame/patterns/uptolevel2"
}
```

For level 2, redos get more complicated, since someone can redo either level 1 or level 2.

```javascript
{
    "id": "http://example.org/profiles/examplegame/patterns/uptolevel2",
    "type": "Pattern",
    "inScheme": "http://example.org/profiles/examplegame/v1",
    "alternates": [
        "http://example.org/profiles/examplegame/patterns/level1",
        "http://example.org/profiles/examplegame/patterns/level2"
    ]
}
```

The option of doing level 1 or level 2 with each redo is encapsulated in an `alternates` Pattern.



## <a name="10.0">10.0</a> The Context

The way JSON-LD documents are mapped onto semantics is through what's called a context, which is specified with `@context`. Most of the time Profile authors and consumers do not need to worry about this at all -- this specification says what needs to go where, and provides the values to put in `@context` in the necessary places. In addition to being hosted at the given URLs, the contexts used are also in the repository this specification is developed in.


<a name="partthree"></a>
# Part Three: Communication and Processing

In addition to the ability to host Profiles as documents, there will be infrastructure
for querying and manipulating Profiles. This document describes the algorithms for
processing Profiles, including the exact rules by which Statement Templates and Patterns
are validated against Statements. It also describes a “Profile Server” to make it easier
to manage and answer questions about Profiles from a centralized location, including
implementing the algorithms.

## <a name="1.0">1.0</a> Profile Server

A Profile Server manages xAPI Profiles from a centralized location. [An RDF triple store](https://en.wikipedia.org/wiki/Triplestore) is responsible for the storage of Profiles.
A Profile Server will allow administrators to add Profiles by their contents or by URI to the Profile Server

A Profile Server will host a SPARQL endpoint containing the RDF information from the
contained Profiles at the path /sparql. This enables xAPI Profiles to be queried. SPARQL
servers have the ability to divide information into multiple datasets, or graphs, and
offer separate querying on them. One of these is the default graph, which is queried
when no other graph is specified. The default graph at this SPARQL endpoint will
contain all the current versions of Profiles.

A Profile Server will include inference logic for the following, at minimum: all SKOS predicate relationships, and `profile:concepts`, `profile:templates`, and `profile:patterns` being subproperties of the inverse of `skos:inScheme`.

### <a name="profile_versions">1.1</a> Profile Versions

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

### <a name="profile_server_best_practices">1.2</a> Best Practices

Some best practices are recomended when adding a Profile to a Profile Server. A technical
review process is warranted to check Profiles for following the specification. As well,
analysis is recommended to ensure the contents of a Profile are of the highest quality.
Upon following these practices, a Profile should be added to a Profile server.

As Profiles support localizations to multiple languages and localities, it is advisable to
provide mechanisms to encourage contribution of xAPI Profile translations. To promote and
to protect the use of an xAPI Profile made publicly available, it is strongly encouraged
that any xAPI Profile provided through a Profile Server be open-licensed.

### <a name="1.3">1.3</a> Example SPARQL Queries

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

## <a name="2.0">2.0</a> Algorithms

This section specifies two primary algorithms. The first, given a Statement and a set of
Statement Templates, validates the Statement against all applicable Statement Templates in
those provided and returns the Statement Templates that match, or an error if any of the
matching Statement Templates does not validate against the Statement. The second, given a
collection of Statements and a set of Patterns, validates if the Statements follows any of
the Patterns.

### <a name="2.1">2.1</a> Statement Template Validation

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


### <a name="2.2">2.2</a> Pattern Validation

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

## <a name="3.0">3.0</a> Libraries

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
