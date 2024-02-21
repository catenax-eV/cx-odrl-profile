# Introduction
This repository contains the legal definition of the terms used in Catena-X Dataspace Protocol (DSP). This is the Catena-X ODRL Profile.

# Contributions
Contributions are made to the ODRL profile itself `profile.ttl`.

Human readable versions are generated out of this file and are released via specific versioned directories, e.g. `v1.0.0`

The process to contribute is setup via the *Catena-X Automotive Network e.V.* and is described here <TODO>.

The `Regulatory Framework Expert Group` operates under the `Data Space Operations Comitee`.


# License
This repository contains 2 licenses. The primary license is `CC-BY-4.0` which can be found in the [LICENSE](./LICENSE) file. This is for the main part of this repository, which is the legal definition of the ODRL terms - The Catena-X ODRL Profile.

Additionally, a tiny part of this repository is source code to generate the human readable documents and to test the definitions. Those parts are under `Apache-2.0` and can be found in [LICENSE_CODE](./LICENSE_CODE). Each file needs to explicitly state that it is under this secondary license.


# Testing

```
# sudo npm install -g jsonld-cli

jsonld expand -a file test_policy.json > test_policy_expanded.json
```
