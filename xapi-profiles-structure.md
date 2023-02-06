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



<a name="part-two"></a>
# Part Two: xAPI Profiles Document Structure Specification

<a name="ref-spec"></a>
## 1.0 Reference Specifications

* [http://json-ld.org](http://json-ld.org/)
* [https://www.w3.org/TR/skos-reference/](https://www.w3.org/TR/skos-reference/)
* [https://www.w3.org/TR/2013/REC-prov-dm-20130430/](https://www.w3.org/TR/2013/REC-prov-dm-20130430/)
* [https://www.w3.org/TR/rdf-sparql-query/](https://www.w3.org/TR/rdf-sparql-query/)

<a name="tech-foundations"></a>
## 2.0 Technical Foundations

This specification describes how to author an xAPI Profile. It describes a set of rules for authoring JSON, specifically JSON-LD. Since JSON-LD is a syntax for RDF, the resulting Profile is really a set of triples—subject, predicate, object—creating a semantic data set. However, for authoring, all that matters is following the rules given for JSON, which will lead to the richer semantic data naturally. Because of this, no JSON-LD processing is required by systems consuming xAPI Profiles, though there will be advantages to doing so for some purposes.

When a Profile is serialized into JSON, it MUST be consistent with what would be produced by the standard JSON-LD 1.1 Processing Algorithms and API Compaction Algorithm. The compaction must use, at least, the normative JSON-LD contexts provided with this specification. Following all the rules given in this document is sufficient to ensure that.

Under the hood, xAPI Profiles will use several well-established semantic web technologies: SKOS, to connect xAPI Concepts together, and PROV, to describe the provenance (most notably the versioning) of Profiles. Several properties in xAPI Profiles use names of properties from SKOS and PROV.

<a name="structure"></a>
## 3.0 Structure

Profiles serve two primary technical goals. First, they contain metadata about xAPI Concepts intended for reuse within Statements, such as verbs and activity types. The metadata includes connections between Concepts, not just within the current Profile, but also as used in other Profiles, supporting a rich ecosystem of related terms. An xAPI Concept is any building block for use in Statements, and new versions of the Profile specification may introduce new Concepts that can be described. The basis for xAPI Concepts is the SKOS Concept, a flexible way to refer to "specific ideas or meanings established within a knowledge organization system."

Second, they contain specific rules about using those Concepts properly in specific situations, both on how to form individual Statements containing specific Concepts, and how to group those Statements together in Patterns of multiple Statements. These rules allow Profile authors to require specific elements, describe precise orderings, and many other options.

To assist in accomplishing these two primary goals, Profiles also contain metadata about themselves—descriptions, authorship, versioning, and so forth.

<a name="doc-interp-gen-restrict"></a>
## 4.0 Document Interpretation and General Restrictions

* All properties in tables are required in all cases unless marked optional.
* Properties marked optional may be required in some situations. If no additional information is provided on the usage of an optional property, including it or not is entirely up to the Profile author.
* All properties that are not JSON-LD keywords (or aliases thereof) MUST expand to absolute IRIs during processing as defined in the JSON-LD specification.
* All properties that are not JSON-LD keywords (or aliases thereof) and not described by this specification MUST be expressed using compact IRIs or absolute IRIs.
* JSON-LD keywords (or aliases thereof) that are not specified as properties in this document MAY be included anywhere they are legal in JSON-LD.
* Values in a Profile MUST NOT be: empty objects, null, empty strings, or empty arrays.
* All requirements on the structure of Profiles MUST be followed by Profile Authors.
* All requirements on Statements following Profiles MUST be followed by Learning Record Providers when authoring Statements and by Profile Validators when validating Statements.

<a name="using-prof-statements"></a>
## 5.0 Using Profiles in Statements

[//]: <> (This section may need to be moved to after the Profile Component sections)
[//]: <> (I think this section can move to after section 10.0, post defintion of profile data model)
[//]: <> (OR this section + Profile Processing Libraries get their own Part; Part 3 or 4 Profile : Statements; Part 3 or 4 Profile Server)

Using an introduced Concept, such as an activity type, verb, attachment usage type, extension, activity, or document resource, can be done freely, provided the defined usage and meaning are adhered to. But a Learning Record Provider can go further, and make sure to adhere to Profile-described Statement Templates and Patterns. Learning Record Providers authoring Statements from Statement Templates or Patterns MUST include a reference to the Profile within said Statements and MAY include reference(s) to the corresponding Statement Template(s) and/or Pattern(s). In other words, when a Statement is authored to satisfy the constraints defined within a Statement Template, that Statement will include a reference to the Profile the Statement Template is defined within; additionally, that Statement can include a reference to the Statement Template. The same logic applies to Patterns. When a Statement is authored to be part of a Pattern, that xAPI Statement will include a reference to the xAPI Profile and can include a reference to the Pattern. When a Statement does not successfully reference an xAPI Profile, it has no recognizable relationship to any xAPI Profile which prevents conformance testing of the Statement.

### 5.1 Reference Activities

xAPI Profile references are Activities found within a Statements' Category contextActivities field. In order to distinguish a Profile reference Activity from an arbitrary Category Context Activity, the following Activity Types are introduced:

- `https://w3id.org/xapi/profiles/reference/version`
- `https://w3id.org/xapi/profiles/reference/template`
- `https://w3id.org/xapi/profiles/reference/pattern`

There is no other mechanism defined in this document that links a Statement to a particular xAPI Profile. See Part 3 for additional information on how conformance is determined.

The following subsections describe each type of reference in more detail but in general:

- Multiple Reference Activities MAY be found in a single xAPI Statement
- Multiple Profiles MAY be referenced within a single xAPI Statement
- Statement Authors SHOULD ensure any and all Reference Activities included within Statements are accurate.

#### 5.1.1 Profile Version Reference Activity

Including a reference to a Profile version indicates that the Statement MUST conform to at least one Statement Template in the referenced Profile version. The identity of those Statement Template(s) is untraceable from a Profile Version Reference alone. The id of the Profile Version Reference Activity is the id of the Profile Version being referenced.

The following is an example of a minimal Profile Version reference Activity.

``` javascript

{"id": "https://example.com/xapi/profile/version/0.0.1",
 "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}}

```

- A Profile Version Reference Activity MUST be a valid Activity
- A Profile Version Reference Activity MUST use `"https://w3id.org/xapi/profiles/reference/version"` as the Activity Type
- A Profile Version Reference Activity MUST only be found within Category contextActivities
- A Profile Version Reference Activity MAY be the only Profile Reference Activity within Category contextActivities

#### 5.1.2 Statement Template Reference Activity

Including a reference to a Statement Template indicates that the Statement SHOULD conform to the referenced Statement Template. This is an optional reference but including one within an xAPI Statement creates an explicit linkage to a Statement Template. The id of the Statement Template Reference Activity is the id of the Statement Template being referenced.

The following is an example of a minimal Statement Template reference Activity.

``` javascript

{"id": "https://example.com/xapi/profile/templates/example",
 "definition": {"type": "https://w3id.org/xapi/profiles/reference/template"}}

```

- A Statement Template Reference Activity MUST be a valid Activity
- A Statement Template Reference Activity MUST use `"https://w3id.org/xapi/profiles/reference/template"` as the Activity Type
- A Statement Template Reference Activity MUST only be found within Category contextActivities
- A Statement Template Reference Activity MUST NOT be the only Profile Reference Activity within Category contextActivities
- A Statement Template Reference Activity MUST NOT be included in a Statement when that Statement doesn't contain a Profile Version Reference Activity for the Profile Version the referenced Statement Template is found within

#### 5.1.3 Pattern Reference Activity

Including a reference to a Pattern indicates that the Statement SHOULD conform to a Statement Template used within the referenced Pattern. This is an optional reference but including one within an xAPI Statement creates an transparent linkage to a Pattern. The id of the Pattern Reference Activity is the id of the Pattern being referenced.

The following is an example of a minimal Pattern reference Activity.

``` javascript

{"id": "https://example.com/xapi/profile/patterns/example",
 "definition": {"type": "https://w3id.org/xapi/profiles/reference/pattern"}}

```

- A Pattern Reference Activity MUST be a valid Activity
- A Pattern Reference Activity MUST use `"https://w3id.org/xapi/profiles/reference/pattern"` as the Activity Type
- A Pattern Reference Activity MUST only be found within Category contextActivities
- A Pattern Reference Activity MUST NOT be the only Profile Reference Activity within Category contextActivities
- A Pattern Reference Activity MUST NOT be included in a Statement when that Statement doesn't contain a Profile Version Reference Activity for the Profile Version the referenced Pattern is found within

### 5.2 Examples

[//]: <> (These examples may be better in an Appendix)

In order to illustrate usage of Profile Reference Activities within xAPI Statements, two example xAPI Profiles (A and B) are introduced and their relevant components summarized in the following table:

Profile | Component          | Name          | ID
--------| ------------------ | ------------- | --
A       | Version            | `version_a`   | `https://example.com/profile/a/version/1.0.0`
A       | Statement Template | `template_a1` | `https://example.com/profile/a/templates/a1`
A       | Statement Template | `template_a2` | `https://example.com/profile/a/templates/a2`
A       | Pattern            | `pattern_a`   | `https://example.com/profile/a/pattern/a1`
B       | Version            | `version_b`   | `https://example.com/profile/b/version/1.0.0`
B       | Statement Template | `template_b1` | `https://example.com/profile/b/templates/b1`
B       | Pattern            | `pattern_b`   | `https://example.com/profile/b/pattern/b`


- Profile A has a single Version `version_A`
- Profile A has two Statement Templates `template_a1` and `template_a2`
- Profile A has a single Pattern `pattern_a`
- Profile B has a single Version `version_b`
- Profile B has a single Statement Template `template_b1`
- Profile B has a single Pattern `pattern_b`

The following subsections demonstrate the way Category contextActivities can be used to reference Profile(s) and their components.

#### 5.2.1 Referencing a Single Profile

References to a Profile connect the Data Generating Process (Learning Record Producer) to the schema describing the domain.

##### 5.2.1.1 Profile Version Reference Activity Usage

A reference to a Profile Version is the broadest link between a Statement and a Profile.

```javascript
{
...
"context": {"contextActivities":
             {"category": [{"id": "https://example.com/profile/a/version/1.0.0",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}}]}}
...
}

```

The above Statement MUST conform to any Statement Template (`template_a1` and/or `template_a2`) within the referenced Profile Version.

##### 5.2.1.2 Statement Template Reference Activity Usage

A reference to a Statement Template is the most explicit link between a Statement and a Profile.

```javascript
{
...
"context": {"contextActivities":
              {"category": [{"id": "https://example.com/profile/a/version/1.0.0",
                             "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}},
                            {"id": "https://example.com/profile/a/templates/a1",
                             "definition": {"type": "https://w3id.org/xapi/profiles/reference/template"}}]}}
...
}

```

The above Statement MUST conform to any Statement Template (`template_a1` and/or `template_a2`) within the referenced Profile Version but inclusion of the Statement Template Reference Activity indicates the Statement Authors intended the Statement to conform to `template_a1` without saying anything about conformance to `template_a2`. The next example does the same thing but switches `template_a2` and `template_a1`.

```javascript
{
...
"context": {"contextActivities":
              {"category": [{"id": "https://example.com/profile/a/version/1.0.0",
                             "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}},
                            {"id": "https://example.com/profile/a/templates/a2",
                             "definition": {"type": "https://w3id.org/xapi/profiles/reference/template"}}]}}
...
}

```

In both cases, the Profile Version Reference Activity and the Statement Template Reference Activity are found within the Statement.

##### 5.2.1.3 Pattern Reference Activity Usage

A reference to a Pattern is the middle ground for linking a Statement and a Profile. Referencing the Pattern indicates that the Statement Authors intended the Statement to conform to one of the Statement Templates within the Pattern opposed to any Statement Template defined within the referenced Profile Version.

```javascript
{
...
"context": {"contextActivities":
              {"category": [{"id": "https://example.com/profile/a/version/1.0.0",
                             "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}},
                            {"id": "https://example.com/profile/a/pattern/a1",
                             "definition": {"type": "https://w3id.org/xapi/profiles/reference/pattern"}}]}}
...
}

```

The above Statement MUST conform to any Statement Template (`template_a1` and/or `template_a2`) within the referenced Profile Version but inclusion of the Pattern Reference Activity indicates the Statement Authors intended the Statement to conform to one of the templates within `pattern_a`. If `pattern_a` contained `template_a1` but not `template_a2`, then it can be concluded that the Authors intended the Statement to conform to `template_a1`. If `pattern_a` contained both `template_a1` and `template_a2`, then the Authors intention for the statement can not be reduced down to a single Statement Template from the provided information.

In order to address that ambiguity, Statement authors can include both Statement Template and Pattern Reference Activities.

```javascript
{
...
"context": {"contextActivities":
              {"category": [{"id": "https://example.com/profile/a/version/1.0.0",
                             "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}},
                            {"id": "https://example.com/profile/a/templates/a2",
                             "definition": {"type": "https://w3id.org/xapi/profiles/reference/template"}},
                            {"id": "https://example.com/profile/a/pattern/a1",
                             "definition": {"type": "https://w3id.org/xapi/profiles/reference/pattern"}}]}}
...
}

```

The above Statement MUST conform to any Statement Template (`template_a1` and/or `template_a2`) within the referenced Profile Version but inclusion of Statement Template and Pattern Reference Activities narrows the intention. The Pattern Reference Activity indicates the Statement should conform to a template within `pattern_a` and the Statement Template reference narrows that template down to `template_a2`.

Note that even though the Statement contains a Profile Version, Statement Template and Pattern Reference Activity, the only conformance requirements for this Statement are due to the Profile Version Reference Activity. The Statement Template and Pattern Reference Activities are purely informative.

#### 5.2.2 Referencing Multiple Profiles

Due to the flexibility of Statement Templates and Patterns, an xAPI Statement may be conformant to multiple xAPI Profiles at once. An xAPI Statement is not expected to contain a reference to every xAPI Profile it conforms to but Statement Authors SHOULD determine which xAPI Profiles are relevant to, and should be referenced within, an xAPI Statement.

##### 5.2.2.1 Multiple Profile Version Reference Activity Usage

References to multiple Profile Versions can span a single xAPI Profile or across xAPI Profiles.

###### Within Single Profile

For example, if we created a new version within Profile A (`version_a2`, `"https://example.com/profile/a/version/2.0.0"`) that builds on `version_a` by adding a new Statement Template (`template_a3`) and then reference `version_a2` within an xAPI Statement:

```javascript
{
...
"context": {"contextActivities":
             {"category": [{"id": "https://example.com/profile/a/version/2.0.0",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}}]}}
...
}

```

The above Statement MUST conform to any Statement Template (`template_a1` and/or `template_a2` and/or `template_a3`) within `version_a2`. The following example Statement has the same conformance requirements:

```javascript
{
...
"context": {"contextActivities":
             {"category": [{"id": "https://example.com/profile/a/version/1.0.0",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}},
                           {"id": "https://example.com/profile/a/version/2.0.0",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}}]}}
...
}

```

`version_a` doesn't contain any Statement Templates not found in `version_a2` so while its valid to include both Profile Version Reference Activities, Statement Authors SHOULD only include Profile Version Reference Activities that reference the most up to date version of an xAPI Profile. An xAPI Profile SHOULD only need to be referenced once via its most recent Profile Version but in cases where incremental Profile Versions are not purely additive, many versions of a single xAPI Profile MAY be referenced. For example, instead of `version_a2` being purely additive, instead it removes `template_a1` from the xAPI Profile and adds `template_a3`. Now, the above Statement MUST conform to either `template_a1` and/or `template_a2` from `version_a` or `template_a2` and/or `template_a3` from `version_a2`.

###### Across Many Profiles

When an xAPI Statements' conformance to multiple Profiles needs to be indicated within the Statement, this is done via Profile Version Reference Activities.

```javascript
{
...
"context": {"contextActivities":
             {"category": [{"id": "https://example.com/profile/a/version/1.0.0",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}},
                           {"id": "https://example.com/profile/b/version/1.0.0",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}}]}}
...
}

```

The above Statement MUST conform to at least one Statement Template (`template_a1` and/or `template_a2`) within `version_a` and MUST conform to at least one Statement Template (`template_b1`) within `version_b`

##### 5.2.2.2 Multiple Statement Template Reference Activity Usage

Like references to Profile Versions, references to Statement Templates can span a single xAPI Profile or across xAPI Profiles.

###### Within Single Profile

The flexibility of Statement Templates allows for an xAPI Profile to contain a Statement Template whose constraints are a super/sub set of constraints found in other Statement Template(s) within the xAPI Profile. This allows Profile authors to create Statement Templates for a single event with varying levels of fidelity. For example, `template_a1` may specify general requirements where as `template_a2` adds specific constraints. That means a Statement that conforms to `template_a2` also conforms to `template_a1` but the inverse is not necessarily true.

```javascript
{
...
"context": {"contextActivities":
             {"category": [{"id": "https://example.com/profile/a/version/1.0.0",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}},
                           {"id": "https://example.com/profile/a/templates/a1",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/template"}},
                           {"id": "https://example.com/profile/a/templates/a2",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/template"}}]}}
...
}

```

The above Statement MUST conform to any Statement Template (`template_a1` and/or `template_a2`) within the referenced Profile Version. Inclusion of the Statement Template Reference Activities narrows the Authors intention down to the specific Statement Templates the Statement SHOULD conform to.

###### Across Many Profiles

Due to the flexibility of xAPI, a single xAPI Statement may represent a category of event that's found across domains. For example, a "started" xAPI Statement could conform to requirements defined within multiple xAPI Profiles.


```javascript
{
...
"context": {"contextActivities":
             {"category": [{"id": "https://example.com/profile/a/version/1.0.0",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}},
                           {"id": "https://example.com/profile/a/templates/a1",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/template"}},
                           {"id": "https://example.com/profile/b/version/1.0.0",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}},
                            {"id": "https://example.com/profile/b/templates/b1",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/template"}}]}}
...
}

```

The above Statement MUST conform to any Statement Template (`template_a1` and/or `template_a2`) within `version_a` and MUST conform to any Statement Template (`template_b1`) within `version_b`. The inclusion of the Statement Template Reference Activities indicates `template_a1` and `template_b1` are the expected matching Statement Templates within `version_a` and `version_b` respectively.

```javascript
{
...
"context": {"contextActivities":
             {"category": [{"id": "https://example.com/profile/a/version/1.0.0",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}},
                           {"id": "https://example.com/profile/a/templates/a1",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/template",
                                           "moreInfo": "https://example.com/profile/a/version/1.0.0"}},
                           {"id": "https://example.com/profile/b/version/1.0.0",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}},
                           {"id": "https://example.com/profile/b/templates/b1",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/template",
                                           "moreInfo": "https://example.com/profile/b/version/1.0.0"}}]}}
...
}

```

When Statement Template Reference Activities span xAPI Profiles, Statement Authors MAY include the referenced Statement Templates' `inScheme` as `moreInfo`. This disambiguates which Statement Template is found in which Profile Version. The resolution of such is possible without using `moreInfo` but its usage makes the association explicit instead of implicit.

##### 5.2.2.3 Multiple Pattern Reference Activity Usage

References to Patterns can also span a single xAPI Profile or across xAPI Profiles.

###### Within Single Profile

Patterns can be defined in terms of Statement Templates or Patterns. Because of this, its possible that an xAPI Statement is authored to satisfy a step within a sub-pattern. To demonstrate, `pattern_i` and `pattern_j` are introduced as `sequence` Patterns within `version_c`. Here `template_x`, `template_y` and `template_z` are arbitrary Statement Templates within `version_c`. The id of `version_c` is `"https://example.com/profile/c/version/1.0.0"`.

`pattern_i = template_x then template_y`

`pattern_j = pattern_j then template_z`

A Statement that contains a Pattern Reference Activity for `pattern_i` indicates the Statement SHOULD conform to `template_x` and/or `template_y`.

```javascript
{
...
"context": {"contextActivities":
             {"category": [{"id": "https://example.com/profile/c/version/1.0.0",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}},
                           {"id": "https://example.com/profile/c/patterns/i",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/pattern"}}]}}
...
}

```

A Statement that contains a Pattern Reference Activity for `pattern_j` indicates the Statement SHOULD conform to `template_x` and/or `template_y` and/or `template_z`.

```javascript
{
...
"context": {"contextActivities":
             {"category": [{"id": "https://example.com/profile/c/version/1.0.0",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}},
                           {"id": "https://example.com/profile/c/patterns/j",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/pattern"}}]}}
...
}

```

A Statement that contains Pattern Reference Activities for both `pattern_i` and `pattern_j` indicates the Statement SHOULD conform to `template_x` and/or `template_y` because both templates are steps within both `pattern_i` and `pattern_j`. Effectively, inclusion of both patterns indicates that the Statement was authored as part of `pattern_i` which in turn was part of `pattern_j`.

```javascript
{
...
"context": {"contextActivities":
             {"category": [{"id": "https://example.com/profile/c/version/1.0.0",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}},
                           {"id": "https://example.com/profile/c/patterns/i",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/pattern"}},
                           {"id": "https://example.com/profile/c/patterns/j",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/pattern"}}]}}
...
}

```

If `pattern_j` was not defined in terms of `pattern_i`, then the intention of above changes. To demonstrate this, lets redefine `pattern_j` to be an Alternative Pattern and leave `pattern_i` unchanged.

`pattern_i = template_x then template_y`

`pattern_j = template_x or template_y`

The above Statement would indicate that the Statement was authored with respect to `pattern_i` and `pattern_j` without changing the conformance expectations. The Statement SHOULD conform to `template_x` and/or `template_y` for both `pattern_i` and `pattern_j`.

When a Statement contains multiple Pattern Reference Activities from the same Profile Version, the relationship between those Patterns and the corresponding intention within the xAPI Statement is determined by what's defined in the Profile Version.

- When `pattern_i` is a sub-pattern of `pattern_j`, including both references indicates Pattern nesting.
- When `pattern_i` is distinct from `pattern_j`, including both references indicates contribution to multiple, independent Patterns

###### Across Many Profiles

Due to the flexibility of xAPI, a single xAPI Statement may represent a category of event that's found across domains. For example, multiple Profiles may contain a Pattern that begins with or contains a "started" Statement Template.

For example, lets say `template_a1` and `template_b1` both have the same `verb` determining property and that's the only constraint within both templates. Additionally, `pattern_a` is `zeroOrMore` of `template_a1` and `pattern_b` is `oneOrMore` of `tempalte_b1`.


```javascript
{
...
"context": {"contextActivities":
             {"category": [{"id": "https://example.com/profile/a/version/1.0.0",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}},
                           {"id": "https://example.com/profile/a/pattern/a1",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/pattern"}},
                           {"id": "https://example.com/profile/b/version/1.0.0",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}},
                           {"id": "https://example.com/profile/b/pattern/b",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/pattern"}}]}}
...
}

```

The above Statement MUST conform to any Statement Template (`template_a1` and/or `template_a2`) within `version_a` and and MUST conform to any Statement Template (`template_b1`) within `version_b`. The inclusion of the Pattern Reference Activities indicates the xAPI Statement should conform to a Statement Template within each pattern. In other words, the Statement SHOULD conform to `template_a1` and SHOULD conform to `template_b1` given the definitions of `pattern_a` and `pattern_b` respectively.


```javascript
{
...
"context": {"contextActivities":
             {"category": [{"id": "https://example.com/profile/a/version/1.0.0",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}},
                           {"id": "https://example.com/profile/a/pattern/a1",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/pattern",
                                           "moreInfo": "https://example.com/profile/a/version/1.0.0"}},
                           {"id": "https://example.com/profile/b/version/1.0.0",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/version"}},
                           {"id": "https://example.com/profile/b/pattern/b",
                            "definition": {"type": "https://w3id.org/xapi/profiles/reference/pattern",
                                           "moreInfo": "https://example.com/profile/b/version/1.0.0"}}]}}
...
}

```

When Pattern Reference Activities span xAPI Profiles, Statement Authors MAY include the referenced Patterns' `inScheme` as `moreInfo`. This disambiguates which Pattern is found in which Profile Version. The resolution of such is possible without using `moreInfo` but its usage makes the association explicit instead of implicit.

<a name="prof-props"></a>
## 6.0 Profile Properties

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
`versions` | Array | An array of all [Profile version](#prof-ver-obj) objects for this Profile. | Required
`author` | Object | An [Organization or Person](#orgs-persons). | Required
`concepts` | Array | An array of [Concepts](#concepts) that make up this Profile. | Optional
`templates` | Array | An array of [Statement Templates](#statment-templates) for this Profile. | Optional
`patterns` | Array | An array of [Patterns](#patterns) for this Profile. | Optional

When `seeAlso` is provided `definition` SHOULD only include a short description of the Profile to aid in discovery and display.

<a name="prof-ver-obj"></a>
### 6.1 Profile Version Objects


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


<a name="orgs-persons"></a>
### 6.2 Organizations and Persons

Use one of these in the `author` property to indicate the author of this Profile version.

Property | Type | Description | Required
-------- | ---- | ----------- | --------
`type` | Object | `Organization` or `Person` | Required
`name` | String | A string with the name of the organization or person | Required
`url` | URL | A URL for the Person or Group. | Optional

<a name="concepts"></a>
## 7.0 Concepts

Concepts are building blocks for use and reuse in xAPI data and other Profiles. In the case of Verbs, Activity Types,  Attachment Usage Types, and Activities, the Concept is "the thing", and when you use that Concept in xAPI you're using it directly. In the case of Document Resources and Extensions, the Concept is "the shape of the thing" that the identifier can be used to point at, and will be used with many different values xAPI data.

A Profile MUST NOT define a Concept that is defined in another Profile unless it supersedes all versions of the other Profile containing the Concept and indicates that in with `wasRevisionOf`.

All Concepts in a Profile MUST follow the rules of one of the subsections within this section. Since the types listed in each subsection are exclusive and required, that will always distinguish which section applies.


<a name="verb-activity-attach"></a>
### 7.1 Verbs, Activity Types, and Attachment Usage Types

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


<a name="extensions"></a>
### 7.2 Extensions


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

Profiles MUST use at most one of `schema` and `inlineSchema` for Extensions. JSON Schema expressions SHOULD adhere to the [Draft-07](https://json-schema.org/specification-links.html#draft-7) version of the JSON Schema specification.

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


<a name="doc-resources"></a>
### 7.3 Document Resources


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

Profiles MUST use at most one of `schema` and `inlineSchema` for Document Resources. JSON Schema expressions SHOULD adhere to the [Draft-07](https://json-schema.org/specification-links.html#draft-7) version of the JSON Schema specification.

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


<a name="activities"></a>
### 7.4 Activities

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

<a name="statment-templates"></a>
## 8.0 Statement Templates

A Statement Template describes how Statements following the Profile MUST be structured.

Property | Type | Description | Required
-------- | ---- | ----------- | --------
`id` | A URI for this Statement Template. | Required
`type` | `StatementTemplate` | Required
`inScheme` | The IRI of the specific Profile version currently being described | Required
`prefLabel` | Object |A Language Map of descriptive names for the Statement Template | Required
`definition` | Object |A Language Map of descriptions of the purpose and usage of the Statement Template | Required
`deprecated` | Boolean | A boolean, default false. If true, this Statement Template is deprecated. | Optional
`verb` | IRI | Verb IRI | Optional
`objectActivityType` | IRI | Object activity type IRI | Optional
`homepage` | Array | Array of Account `homePage` IRLs found within a Statement | Optional
`activityDefinitionExtension` | Array | Array of Activity Extension IRIs found within a Statement | Optional
`resultExtension` | Array | Array of Result Extension IRIs found within the Result Object | Optional
`contextExtension` | Array | Array of Context Extension IRIs found within the Context Object | Optional
`contextGroupingActivityType` | Array | Array of contextActivities grouping activity type IRIs | Optional
`contextParentActivityType` | Array | Array of contextActivities parent activity type IRIs | Optional
`contextOtherActivityType` | Array | Array of contextActivities other activity type IRIs | Optional
`contextCategoryActivityType` | Array | Array of contextActivities category activity type IRIs | Optional
`contextAgentActivityType` | Array | Array of contextAgent activity type IRIs | Optional
`contextGroupActivityType` | Array | Array of contextGroup activity type IRIs | Optional
`attachmentUsageType` | Array | Array of attachment usage type IRIs | Optional
`objectStatementRefTemplate` | Array | An array of Statement Template identifiers from this Profile version. | Optional
`contextStatementRefTemplate`. | Array | An array of Statement Template identifiers from this Profile version. | Optional
`rules` | Array | Array of Statement Template Rules | Optional

A Statement Template MUST NOT have both `objectStatementRefTemplate` and `objectActivityType`.

The verb, object activity type, homepage, extensions, attachment usage types, and context activity types listed are called Determining Properties.

A Profile Author MUST change a Statement Template's `id` between versions if any of the Determining Properties, StatementRef properties, or rules change. Changes of `scopeNote` are not considered changes in rules.

A Learning Record Provider authoring a Statement following a Statement Template:
* MUST include all the Determining Properties in the Statement Template. A Statement Template using multiple Determining Properties is considered an "AND" operation.
* MUST follow all rules in the Statement Template.
* SHOULD include a reference to the Statement Template or the Profile as a Category Context Activity as described in [Using Profiles in Statements](./xapi-profiles-structure.md#using-prof-statements).
* MUST, if `objectStatementRefTemplate` is specified, set the Statement object to a StatementRef with the `id` of a Statement matching at least one of the specified Statement Templates.
* MUST, if `contextStatementRefTemplate` is specified, set the Statement context Statement property to a StatementRef with the `id` of a Statement matching at least one of the specified Statement Templates.
* MUST, if `homepage` is specified, ensure that for each IRL, there is at least one corresponding Agent or Group identified by an account IFI Object with a `homePage` value set to the IRL.
* MUST, if `activityDefinitionExtension` is specified, ensure that for each extension IRI key, there is at least one Activity in the Statement that includes the IRI key. A single Activity MAY contain multiple extension IRI keys.

A Profile Validator validating a Statement MUST validate all the Learning Record Provider requirements for a Statement Template are followed.


<a name="statement-template-rules"></a>
### 8.1 Statement Template Rules

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
    "contextAgentActivityType" : [
        "http://example.org/profiles/sport/activitytypes/contestant"],
    "rules": [
        {
            "location":
                "$.result.extensions['http://example.org/profiles/sports/extensions/place']",
            "presence": "included"
        }
    ]
}
```

<a name="patterns"></a>
## 9.0 Patterns

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



<a name="context"></a>
## 10.0 The Context

The way JSON-LD documents are mapped onto semantics is through what's called a context, which is specified with `@context`. Most of the time Profile authors and consumers do not need to worry about this at all -- this specification says what needs to go where, and provides the values to put in `@context` in the necessary places. In addition to being hosted at the given URLs, the contexts used are also in the repository this specification is developed in.
