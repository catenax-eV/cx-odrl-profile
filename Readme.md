
# Introduction to the Catena-X ODRL Profile and this Repository

This repository represents the official **Catena-X Open Digital Rights Language (ODRL) profile**

The primary aim of the **Catena-X ODRL Profile** is to provide standardized contractual modules such as permissions, prohibitions and obligations in a manner such that they can be checked automatically, in a machine-readable format. In short: the ODRL profile enables **automatating contractual negotiations** on the Catena-X Data Space as by default, contract negotiations happen electronically via a registered connector. This repository contains the technical definition of the Catena-X ODRL Profile and the legal definitions of the terms used in the Catena-X Data Space during the *Dataspace Protocol Negotiation process* and its resulting agreements.

All standardized contractual modules referenced in the Catena-X ODRL profile have a legal description, a technical term to reference them ("leftOperand") and in some cases a defined list of possible or allowed or standardized values ("rightOperand").

The Catena-X ODRL profile has an initial focus on providing **standardized data usage policies "purposes"** for the Catena-X Use Cases as a mutual foundation that all data space participants can rely on to ensure trust, interoperability, and scalability. These policies represent the Catena-X value proposition of **data sovereignty** in its purest form.

Below we list out an example for such a standardized usage policy based on the official Catena-X ODRL profile:

- **Example Catena-X leftOperand** for a standardized Catena-X usage policy: cx-policy:UsagePurpose
- **Example Catena-X rightOperand** for a standardized Catena-X usage policy: cx.circular.dpp:1
- **Example legally binding purpose description** of standardized Catena-X RightOperand: "Exchange and use of data according to the applicable public legal regulation directly requiring digital product passports or affecting the contents or handling of digital product passports."

Additional standardized contractual modules will follow in future Catena-X Releases.

Contributions are made to the ODRL profile itself [profile.ttl](./profile.ttl)

The human readable version is generated from the *.ttl file and stored under [profile.md](./profile.md)

# Context on the Open Digital Rights Language (ODRL)

The Open Digital Rights Language (ODRL) is a policy expression language that provides a flexible and interoperable information model, vocabulary, and encoding mechanisms for representing statements about the usage of content and services. The ODRL Information Model describes the underlying concepts, entities, and relationships that form the foundational basis for the semantics of the ODRL policies. Besides Catena-X, ODRL is used by the DSP ([Dataspace Protocol](https://docs.internationaldataspaces.org/dataspace-protocol/)), another core component of the Catena-X architecture

Policies are used to represent permitted and prohibited actions over a certain asset, as well as the obligations required to be meet by stakeholders. In addition, policies may be limited by constraints (e.g., temporal or spatial constraints) and duties may be imposed on permissions.

*Source and more information on ODRL:* [w3.org](https://www.w3.org/TR/odrl-model/)

# Contributions

The **Catena-X Automotive Network e.V.'s** Data Space Operations Commitee and its Regulatory Expert Group organizes the contribution process to this repository in accordance with the Catena-X Operating Model and its process for standardizing non-technical requirements.

# License

This repository contains 2 licenses. The primary license is `CC-BY-4.0` which can be found in the [LICENSE](./LICENSE) file. This is for the main part of this repository, which is the definition of the ODRL terms - The Catena-X ODRL Profile.

Additionally, a small part of this repository is source code to generate the human readable documents and to test the definitions. Those parts are under `Apache-2.0` and can be found in [LICENSE_CODE](./LICENSE_CODE). Each file needs to explicitly state that it is under this secondary license.

# Examples

An example can be found in [example_usage_policy.json](./example_usage_policy.json) and its jsonld expanded version [example_usage_policy_expanded.json](./example_usage_policy_expanded.json)

# Testing

```
# sudo npm install -g jsonld-cli

jsonld expand example_usage_policy.json > example_usage_policy_expanded.json
```
