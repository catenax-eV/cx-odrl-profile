# Catena-X ODRL Profile
This is the Catena-X ODRL Profile.

The machine readable details can be found in the `*.ttl` file.

## Legally binding term definitions
NO LEGAL DEFINITION YET


# LeftOperand
## FrameworkAgreement
### Identifier
https://w3id.org/catenax/policy/FrameworkAgreement

### Description (not binding)
The framework the negotiation is based on. Also known as Usecase Framework.
Please find the legal definitions from the published Usecase Frameworks here:

https://catena-x.net/en/catena-x-introduce-implement/governance-framework-for-data-space-operations

Version numbers depend on the document and are typically 2 digit (e.g. 1.0).

*FrameworkAgreement* as a leftOperand allows the following **DRAFT VERSION (depends on the release of the legal documents)** *rightOperand* values

**Traceability:1.0**

**Pcf:1.0**

**Quality:1.0**

**CircularEconomy:1.0**

**DemandCapacity:1.0**

**Puris:1.0**

**BusinessPartner:1.0**

**BehavioralTwin:1.0**



### Definition (legally binding)
NO LEGAL DEFINITION YET.

## Membership
### Identifier
https://w3id.org/catenax/policy/Membership

### Description (not binding)
Membership in the Dataspace

### Definition (legally binding)
NO LEGAL DEFINITION YET.

## ContractReference
### Identifier
https://w3id.org/catenax/policy/ContractReference

### Description (not binding)
A reference to an existing, individual contract as a basis for the negotiation. This can be a frame contract or a very specific contract.

The rightOperand value for this is a free to choose reference under which both parties are able to identify their contract. Typically no version numbers are used.



### Definition (legally binding)
NO LEGAL DEFINITION YET.

## UsagePurpose
### Identifier
https://w3id.org/catenax/policy/UsagePurpose

### Description (not binding)
Legally binding purpose description. Allowed are standardized rightOperand values and free text values.

LEGALLY BINDING MEANING for version 1.x is defined in the corresponding Usecase Framework documents that are referenced via the **FrameworkAgreement**

The following list is NOT complete and a (not legally binding) summary of the relevant parts from the FrameworkAgreements:

Version numbers are typically 1 digit.

#### Version 1.0 of the Traceability FrameworkAgreement (deprecated)

purpose.trace.v1.TraceBattery : **Deprecated.** Use instead: cx.core.legalRequirementForThirdparty:1 **or** cx.core.tractionbattery:1 (**under clarification**)

purpose.trace.v1.aspects : **Deprecated.** Use instead: cx.core.industrycore:1

purpose.trace.v1.qualityanalysis : **Deprecated.** Use instead: cx.core.qualityNotifications:1

ID 3.1 Trace : **Deprecated.** Not directly replaced. Use a more specific UsagePurpose.

#### Version 1.0 of the FrameworkAgreements released for 2405

cx.core.legalRequirementForThirdparty:1 **or** cx.core.tractionbattery:1
(**under clarification**)
&quot;Facilitating compliance with mandatory regulatory requirements for tracking and reporting battery cells, modules &amp; high-voltage batteries. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.core.industrycore:1**
&quot;Establishing a digital representation of the automotive supply chain to enable a component specific data exchange. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.core.qualityNotifications:1**
&quot;The data can be used for quality analysis to identify and select affected components and to send quality notifications to affected customers or suppliers. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.pcf.base:1**

**cx.quality.base:1**

**cx.dcm.base:1**

**cx.puris.base:1**
&quot;Optimising processes, conducting plausibility checks and/or collecting information to facilitate sound decision making, each in the context of predictive unit realtime information relating to production and/or logistics. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.circular.dpp:1**
&quot;Exchange and use of data according to the applicable public legal regulation directly requiring digital product passports or affecting the contents or handling of digital product passports. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.circular.smc:1**
&quot;Exchanging information about secondary material content (SMC) to optimize SMC-usage. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.circular.marketplace:1**
&quot;Buy, sell and/or procure  parts and material. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.circular.materialaccounting:1**
&quot;Display, process, analysis, correlate, modify and amend data. Use of data for (e.g. enablement of) chain of custody processes and commercial transaction related thereto and allocation of material to parts to the supply chain. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.bpdm.gate.upload:1**
&quot;Verifying, curating and enriching data to create a record of basic information about all entities with a BPN in the CX Data Space accessible to all Participants (&quot;Golden Record&quot;) and for early warning services (value-added services, &quot;VASs&quot;). As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.bpdm.gate.download:1**
&quot;Providing basic information about entities with a BPN in the CX Data Space for Data Consumer to identify counterparty and/or for VASs. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.bpdm.pool:1**
&quot;Identifying Participants within the CX Data Space for Data Consumer's internal counterparty identification and information processes and/or for VASs. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.bpdm.vas.dataquality.upload:1**
&quot;Screening Data Provider's data (i) to assess Data Provider's data quality and (ii) to create benchmarks for future screenings of other Participants' data by Data Consumer to fulfill the goals of the DQD application. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.bpdm.vas.dataquality.download:1**
&quot;Data Consumer assessing quality of own data. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.bpdm.vas.bdv.upload:1**
&quot;Screening relevant Data Provider's bank data to verify Data Provider's bank data. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.bpdm.vas.bdv.download:1**
&quot;Verifying Data Consumer's submitted bank data. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.bpdm.vas.fpd.upload:1**
&quot;Screening Data Provider's business partner data to assess fraud. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.bpdm.vas.fpd.download:1**
&quot;Data Consumer assessing fraud risks when transacting with another Participant. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.bpdm.vas.swd.upload:1**
&quot;Screening Data Provider's beneficial ownership data to assess trade compliance. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.bpdm.vas.swd.download:1**
&quot;Data Consumer assessing trade sanction risks when transacting with another Participant. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.bpdm.vas.nps.upload:1**
&quot;Verifying Data Provider's Business Partner Data against natural person data entries. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.bpdm.vas.nps.download:1**
&quot;Data Consumer verifying its own Business Partner Data. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.bpdm.vas.countryrisk:1**
&quot;Screening Participants’ business data to identify risks when collaborating with a new/existing business partner according to official or company-specific country risk assessments. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

**cx.behaviortwin.base:1**

**cx.core.digitalTwinRegistry:1** : **under clarification**




### Definition (legally binding)
NO LEGAL DEFINITION YET.

