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

<a name="part-one"></a>
# Part One: About xAPI Profiles

<a name="introduction"></a>
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

<a name="how-to-use-this-doc"></a>
## 2.0 How to Use This Document 

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


<a name="def-must-should-may"></a>
### 2.1 MUST / SHOULD / MAY

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


<a name="interpret-text-table"></a>
### 2.2 Guidelines for Interpreting Descriptive Text and Tables

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

<a name="definitions"></a>
## 3.0 Definitions


* [Absolute IRI](#absoluteiri)
* [Activity](#activity)
* [Activity Definition](#activitydefinition)
* [Activity Type](#activitytype)
* [Attachment Usage Type](#attachmentusagetype)
* [Compact IRI](#compactiri)
* [Concept](#concept)
* [Context](#def-context)
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

<a name="concept"></a>**Concept**: In SKOS, any unit of thought. In this specification, any of a particular list of possible things a Profile might describe.

<a name="def-context"></a>**Context**: In xAPI this refers to a part of a Statement, but in this specification it usually means a [JSON-LD `@context`](https://www.w3.org/TR/json-ld/#the-context), which is a way of mapping JSON onto semantic terms and RDF.

<a name="documentresource"></a>**Document Resource**: An [Experience API Document Resource](https://github.com/adlnet/xAPI-Spec/blob/master/xAPI-Communication.md#22-document-resources). This specification helps Profile Authors describe what Document Resources in particular locations need to look like.

<a name="xapi"></a>**Experience API (xAPI)**: The [Experience API Specification](https://github.com/adlnet/xAPI-Spec). For this specification, any 1.0.x version is relevant. Describes data structures for describing experiences and APIs for communicating them.

<a name="extension"></a>**Extension**: An [Experience API Extension](https://github.com/adlnet/xAPI-Spec/blob/master/xAPI-Data.md#miscext). This specification helps Profile Authors describe what Extensions with specific identifiers need to look like.

<a name="iri"></a>**IRI**: An [Internationalized Resource Identifier](https://www.ietf.org/rfc/rfc3987.txt). Like a URL, but more general. A distributed, structured, persistent identifier.

<a name="json"></a>**JSON**: [JavaScript Object Notation](http://www.json.org). A simple way to represent data structures for computers that humans don't have too hard a time writing or reading. The way Profiles are represented in this specification.

<a name="jsonschema"></a>**JSON Schema**: [JSON Schema](http://json-schema.org) are a way to describe and constrain the form of JSON documents. This specification adheres to [Draft-07](https://json-schema.org/specification-links.html#draft-7) version of the JSON Schema specification.

<a name="jsonld"></a>**JSON-LD**: [JSON-LD](https://json-ld.org) turns JSON into Linked Data, making it easy to use with Linked Data tools and integrate with other datasets.

<a name="jsonpath"></a>**JSONPath**: [JSONPath](http://goessner.net/articles/JsonPath/index.html#e2) provides a way to address parts of JSON documents using a `JSONPath expression`.

<a name="languagemap"></a>**Language Map**: A Language Map expresses multiple language-specific values at once. While used in the xAPI specification essentially identically, the controlling specification is [JSON-LD Language Maps](https://www.w3.org/TR/json-ld/#language-maps).

<a name="learningrecordprovider"></a>**Learning Record Provider**: As in the Experience API specification, anything creating Learning Records (xAPI Statements and Document Resources).

<a name="mediatype"></a>**Media Type**: A [media type](https://www.iana.org/assignments/media-types/media-types.xhtml) is a simple, structured way to refer to particular types of content. Also known as MIME Type or Content Type.

<a name="pattern"></a>**Pattern**: One way a series of Statements following a Profile could look. Defined by this specification.

<a name="profile"></a>**Profile**: A profile is the human and/or machine-readable documentation of application-specific concepts, statement patterns, extensions, and statement templates used when implementing xAPI in a particular context. A profile is a way to talk about Concepts, Statement Templates, and Patterns for Experience API data in a particular context, and in particular to describe them so machines can do some processing automatically.

<a name="profileauthor"></a>**Profile Author**: Some person or group writing a Profile.

<a name="profileserver"></a>**Profile Server**: A place to find, browse, and query Profiles, vocabulary concepts, and other profile metadata.

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
