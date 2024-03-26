# Introduction
This repository contains the technical definition of the Catena-X ODRL Profile and in the future, the legal definitions of the terms used in the Catena-X Dataspace during the *Dataspace Protocol Negotiation process* and its resulting agreements.

Contributions are made to the ODRL profile itself [profile.ttl](./profile.ttl)

The human readable version is generated from the *.ttl file and stored under [profile.md](./profile.md)

# Contributions
The contribution process to this repository is organized via **Catena-X Automotive Network e.V. -> Data Space Operations Comitee -> Regulatory Framework Expert Group** and via its lead, currently: Hanno Focken

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
