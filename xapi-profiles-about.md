# xAPI Profiles

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

