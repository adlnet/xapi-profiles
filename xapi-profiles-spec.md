# Structure & Communication Draft

## Reference Specifications

[http://json-ld.org](http://json-ld.org/)
https://www.w3.org/TR/skos-reference/
https://www.w3.org/TR/2013/REC-prov-dm-20130430/
https://www.w3.org/TR/activitystreams-core/
https://www.w3.org/TR/rdf-sparql-query/


## Technical Foundations

This specification describes how to author an xAPI Profile. It describes a set of rules for authoring JSON, specifically JSON-LD. Since JSON-LD is a syntax for RDF, the resulting profile is really a set of triples—subject, predicate, object—creating a semantic data set. However, for authoring, all that matters is following the rules given for JSON, which will lead to the richer semantic data naturally. Because of this, no JSON-LD processing is required by systems consuming xAPI Profiles, though there will be advantages to doing so for some purposes.

The serialized JSON form of an xAPI Profiles 1.0 document must be consistent with what would be produced by the standard JSON-LD 1.1 Processing Algorithms and API Compaction Algorithm using, at least, the normative JSON-LD @context definition provided.

Under the hood, xAPI Profiles will use several well-established semantic web technologies: SKOS, to connect xAPI concepts together, and PROV, to describe the provenance (most notably the versioning) of profiles. Several properties in xAPI Profiles use names of properties from SKOS and PROV.

# Structure

Profiles serve two primary technical goals. First, they contain metadata about xAPI concepts intended for reuse within statements, such as verbs and activity types. The metadata includes connections between concepts, not just within the current profile, but also as used in other profiles, supporting a rich ecosystem of related terms. Some of the xAPI concepts a profile lists won't be original to this profile, either, but will be borrowed from other profiles.

Second, they contain specific rules about using those xAPI concepts properly, both on how to form individual statements containing specific concepts, and how to group those statements together in patterns of multiple statements. These rules allow profile authors to require specific elements, describe precise orderings, and many other options.

To assist in accomplishing these two primary goals, profiles also contain metadata about themselves—descriptions, authorship, versioning, and so forth.

## Using Profiles in Statements

Using an introduced Concept, such as an activity type, verb, attachment usage type, extension, activity, or document resource, should be done freely, provided the defined usage and meaning are adhered to. But a producer can go further, and make sure to adhere to profile-described statement templates and patterns. Producers creating statements that conform to matching profile-described statement templates and patterns SHOULD include the profile as a category context activity in those statements, and statements containing a profile as a category context activity MUST conform to any matching templates and patterns that profile describes.

## Profile Metadata

Name	Values
@id	The IRI of the profile overall (not a specific version)
@type	Must be Profile
name	language map of names for this profile
definition	language map of descriptions for this profile. If there are additional rules for the profile as a whole that cannot be expressed using this specification, include them here.
seeAlso	a URL containing information about the profile. Recommended instead of especially long definitions.
versions	an array of all profile version objects for this profile, see below
author	an Organization or Person, see below
concepts	The concepts that make up this Profile, see the Concepts section
templates	The Statement Templates for this profile, see that section
patterns	The Patterns for this profile, see that section



### Profile Version Objects

Name	Values
@id	the IRI of the version ID
wasRevisionOf	an array, usually of length one, of IRIs of all profile versions this version was written as a revision of
generatedAtTime	the date this version was created on

Profile version objects make it convenient to track version history for profiles, following recommendations for SKOS concept schemes and PROV version tracking generally. By using versions this way, it is possible to answer precise questions such as “what version of this profile was current on the 3rd of January last year?”. Lack of robust versioning is frequently identified as an issue with RDF data.

### Organizations and Persons

Name	Values
@type	Organization or Person
name	A string with the name of the organization or person



## Concepts

### Core Concepts: Verbs, Activity Types, and Attachment USage Types

When describing verbs, activity types, and attachment usage types, use the following terms:

Name	Values
@type	Verb, ActivityType, or AttachmentUsageType
inScheme	the IRI of the specific vocabulary version the current profile document is for
prefLabel	a language map of the preferred names in each language
altLabel	a language map of alternative names in each language
definition	a language map of the precise definition, including how to use the concept properly in statements
broader	the IRI of a concept of the same @type from this profile that has a broader meaning.
narrower	the IRI of a concept of the same @type from this profile that has a narrower meaning.
broadMatch	the IRI of a concept of the same @type from a different profile that has a broader meaning.
narrowMatch	the IRI of a concept of the same @type from a different profile that has a narrower meaning.
exactMatch	the IRI of a concept of the same @type from a different profile that has exactly the same meaning. This should be used rarely, mostly to describe connections to vocabularies that are no longer managed and do not use good URLs.
relatedMatch	the IRI of a concept of the same @type from a different profile that has a related meaning that is not clearly narrower or broader. Useful to establish conceptual links between profiles that can be used for discovery.



### Extensions

This is the trickiest bit, probably, along with the idea of constraining document resources. The below is intended to be very preliminary.

Name	Values
@id	the IRI of the extension, used as the extension key in xAPI
name	a language map of descriptive names for the extension
definition	a language map of descriptions of the purpose and usage of the extension
placement	an array of placement locations. Must contain at least one element, no elements may be repeated, and the only allowed elements are "context", "result", "activity" and IRIs (which must be Activity Type IRIs in this or other profiles).
context	optional. the IRI of a JSON-LD context for this extension
schema	optional. the IRI for accessing a JSON Schema for this extension. The JSON Schema may constrain the extension to a single type.
inlineSchema	A JSON Schema inline.



### Document Resources

Document resources similar properties to extensions. The @id MUST be used as the stateId or profileId (as appropriate) when interacting with the corresponding resource.


Name	Values
@id	the IRI of the document resource, used as the stateId/profileId in xAPI
@type	one of: StateResource, AgentProfileResource, ActivityProfileResource
name	a language map of descriptive names for the document resource
definition	a language map of descriptions of the purpose and usage of the document resource
context	optional. the IRI of a JSON-LD context for this document resource
schema	optional. the IRI for accessing a JSON Schema for this document resource.
inlineSchema	A JSON Schema inline.
contentType	the content-type for the resource



### Activities

These are just literal xAPI Activity definitions the profile wants to provide for use. Possibly will need some adjustment later as the JSON-LD context is fleshed out (there's some trickiness around defining the JSON-LD context for all the parts in xAPI activity definitions just right).

Name	Values
@id	the IRI of the activity
type	as in xAPI
name
description
moreInfo
extensions
interactionType
correctResponsesPattern
choices
scale
source
target
steps

## Statement Templates

A Statement Template describes one way statements following the profile may be structured. Which statement template applies is determined by the verb, object activity type, and attachment usage types in the statement. If the verb, object activity type, and all attachment usage type(s) are present and the profile is used as a category context activity, the rules in the Statement Template MUST be followed.


Name	Values
@id	the identifier or short name of the template, in the form :name
name	a language map of descriptive names for the statement template
definition	a language map of descriptions of the purpose and usage of the statement template
verb	optional. verb's IRI
objectActivityType	optional. activity type's IRI
attachmentUsageType	optional. array of attachment usage type IRIs
rules	array of statement template rules



### Statement Template Rules

Statement Template Rules describe a location or locations within statements using a JSONPath, then require that value either be excluded, included, or be a particular value. For example, to require at least one grouping, perhaps it might be something like:

```
"requirements": [
    {
        "location": "context.contextActivities.grouping[0]",
        "rule": "included"
    }
]
```

They have these properties:

Name	Values
location	A JSONPath string
selector	optional. A JSONPath string. This JSONPath is executed on the array of values resulting from the location selector, and the resulting values are what are used for matching. If it returns nothing on a location, that represents an unmatchable value for that location, meaning "all" will not be able to match and included will fail.
rule	included or excluded. Only one of rule or value may be used.
any	an array of values that are allowed in this location. Useful for constraining the presence of particular activities, for example. If the rule returns multiple values for a statement, then this Statement Template Rule is fulfilled if any one returned value matches any one specified value — that is, if the intersection is not empty.
all	an array of values, which all values returned by the JSONPath must match one of to fulfill this Statement Template Rule



### Alignments?

I propose we do not include alignments in the initial draft

### Statement References

I'm unsure enough how to do this I propose we do not include statement reference constraints in the initial draft. It would probably be included as a special case in the statement template rules, above. 

## Patterns

Patterns are statements matching particular statement templates, ordered in certain ways. For example, an allowed pattern in a video profile might start with a statement about playing a video and then be followed by statements about pausing, skipping, playing again, and so forth. A pattern is determined by a given registration — all statements within a Pattern MUST use the same registration, and statements not part of a Pattern MUST NOT use the same registration as any that are.

Patterns have these properties:


Name	Values
name	a language map of descriptive names for the pattern
definition	a language map of descriptions of the purpose and usage of the pattern
pattern	a single pattern element (see below), containing statement template identifiers and/or subpattern identifiers
subpatterns	optional, an array of pattern elements for the pattern above to refer to, which may each contain statement template identifiers and subpattern identifiers



### Pattern Elements

Name	Values
@id	the identifier or short name of the template, in the form :name
alternates	a two-or-more length array of pattern or statement template identifiers. An alt pattern matches if any member of the array matches
optional	a single pattern or statement template identifier. An opt pattern matches if the identified thing matches once, or not present at all
oneOrMore	a single pattern or statement template identifier. A plus pattern matches if the identified thing matches once, or any number of times more than once
sequence	an array of pattern or statement template identifiers. A seq pattern matches if the identified things match in the order specified.
zeroOrMore	a single pattern or statement template identifier. A star pattern matches if the identified thing is not present or is present one or more times


A single pattern element MUST contain exactly one of alt, opt, plus, seq, and star.


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
        "altLabel": {
            "@id": "skos:altLabel",
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

Administrators will be able to add profiles by their contents or by URI to the Profile Server. On the Public Profile Server run by... DISC? ADL? ... there will be a review process people desiring to add profiles can submit to. The review process will check profiles for following the specification and assist in helping them be of highest quality, after which they will be added to the server.

The Profile Server will host a sparql endpoint containing all the RDF information in contained profiles at the path /sparql. All these SPARQL queries can also be run locally by loading one or more profiles into an RDF library and running sparql queries against them directly.

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


# To Consider

* Do we want to allow inclusion of example statements, such as with verbs?
* I would like to get rid of closely related natural language term (which was in vocabularies). It provides two possible values: definition and a way to connect to other xAPI terms (going through natural language), but I feel the first is best met by people writing definitions, and the second is best met by explicit connections, especially as the closely related natural language term stuff is something people mess up *all the time*.
* Some elements are often multiply valued, and so it makes sense to require them to be arrays. Many other elements could be slightly useful with multiple values, but so little that requiring them, in practice, for now, be singly valued is not a big sacrifice and provides complexity savings. But some elements are usually singly valued, but deliver a lot of value if multiply valued — for example, imagine one profile *merging* multiple profiles and being able to maintain provenance information by using wasRevisionOf with multiple values! The question is: disallow despite disadvantage, allow both adding a little complexity, or require array despite almost always being singly valued. Note: if someone accidentally writes it as a bare value, when they run the compaction algorithm the @container @set will make compaction turn it into an array.
* Do we require extensions to be JSON-LD? Most common JSON formats can be easily (and often have been, such as GeoJSON) “LD-ified”, so there's very little we'd be outright excluding, and there's a lot of advantage to *allowing* it to be JSON-LD. Ultimately, of course, an extension won't be “anything that is legal by the JSON-LD context”, it will be “anything that makes sense according to the context and any other associated rules”.
* Hrrrrrmm if we use type for @type we can't use type in identified activities... I think in that case we want to make people type @id as well... even for activities.
* How do we enforce a profile on data “later” — easy in the sense of, it was sent with that profile but was never checked, but more difficult in the sense of, use a profile to extract meaningful sequences of statements that are otherwise profile-following but do not indicate their profileness... in fact, it is quite a hard problem in the general sense, but in many specific cases it won't be too bad, which might be good enough


