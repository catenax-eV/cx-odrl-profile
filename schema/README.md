# Catena-X Policy Profile

Catena-X has for multiple years defined certain policies as well-known in the Dataspace. These definitions were
partly in text and partly in TTL. With the Dataspace Protocol JSON Schemas
gaining [normativitiy](https://eclipse-dataspace-protocol-base.github.io/DataspaceProtocol/2025-1-RC1/#schemas-contexts)
in Release 2025-1,there is a clearer extension point in place for Dataspaces to define their own profiles.

The `Constraint` object is an essential extension point for the Dataspace Protocol. It is embedded in a variety of DSP-
messages that are foundational for the legally-binding contract negotiation between business partners in a Dataspace.
This folder contains the relevant JSON schemas, a JSON-LD context and examples for the commonplace policies.

CX-015x Policy Constraints For Data Exchange describes how the constraints should be used in Access Policies and Usage Policies and refers to this schema.