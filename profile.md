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
The framework the negotiation is based on. Previously known as Usecase Framework, now, known as Data Exchange Governance:

https://catena-x.net/en/catena-x-introduce-implement/governance-framework-for-data-space-operations

Version numbers depend on the document and are typically 2 digit (e.g. 1.0).


**Traceability:1.0**

Valid from: 2024-06-20

Valid until: 2024-10-16

Status: deprecated

**Pcf:1.0**

Valid from: 2024-06-20

Valid until: 2024-10-16

Status: deprecated

**Quality:1.0**

Valid from: 2024-06-20

Valid until: 2024-10-16

Status: deprecated

**CircularEconomy:1.0**

Valid from: 2024-06-20

Valid until: 2024-10-16

Status: deprecated

**DemandCapacity:1.0**

Valid from: 2024-06-20

Valid until: 2024-10-16

Status: deprecated

**Puris:1.0**

Valid from: 2024-06-20

Valid until: 2024-10-16

Status: deprecated

**BusinessPartner:1.0**

Valid from: 2024-06-20

Valid until: 2024-10-16

Status: deprecated

**BehavioralTwin:1.0**

Valid from: 2024-06-20

Valid until: 2024-10-16

Status: deprecated

**DataExchangeGovernance:1.0**

Valid from: 2024-10-17

Valid until:

Status: published



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

Version numbers are typically 1 digit.



### Definition (legally binding)


**cx.core.legalRequirementForThirdparty:1**
&quot;Facilitating compliance with mandatory regulatory requirements for tracking and reporting battery cells, modules &amp; high-voltage batteries. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for: TractionBatteryCode

Valid from: 2024-06-20

Valid until:

Status: published

**cx.core.industrycore:1**
&quot;Establishing a digital representation of the automotive supply chain to enable a component specific data exchange. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for:
SerialPart,
Batch,
JustInSequencePart,
SingleLevelBomAsBuilt,
PartAsPlanned,
SingleLevelBomAsPlanned,
PartSiteInformationAsPlanned,
UniqueIDPushAPI

Valid from: 2024-06-20

Valid until:

Status: published

**cx.core.qualityNotifications:1**
&quot;The data can be used for quality analysis to identify and select affected components and to send quality notifications to affected customers or suppliers. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for: Notification API

Valid from: 2024-06-20

Valid until:

Status: published

**cx.pcf.base:1**
&quot;(i) sending and receiving product-specific CO2 data and related functionalities such as (but not limited to) certificate exchange and notifications, 
(ii) conducting plausibility checks and validation measures,
(iii) calculating aggregated PCFs of Data Consumer (including calculations operated by a technical service provider that (a) is certified for Catena-X, (b) is not authorized to evaluate data beyond such calculation and (c) provides calculations exclusively for Data Consumer's own purposes).

As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for:
PCF Model,
PCF Exchange API

Valid from: 2024-06-20

Valid until:

Status: published


**cx.quality.base:1**
&quot;(i) Early identification of anomalies in the use of the product,
(ii) collaborative root-cause analysis of a problem / error and determining corrective action, 
(iii) component tracing to optimize technical actions (in combination with use case Traceability),
(iv) confirming corrective action,
(v) preventive field observation to detect anomalies, 
(vi) processing notifications of quality alerts (&quot;&quot;supply chain bottom-up&quot;&quot;) and quality investigations (&quot;&quot;supply chain top-down&quot;&quot;) (possibly in combination with use case &quot;&quot;Traceability&quot;&quot;).

As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for:
Fleet Vehicles,
Quality Task,
QualityTaskAttachment,
PartsAnalysis,
ManufacturedPartsQInformation,
FleetDiagnosticData,
FleetClaim

Valid from: 2024-06-20

Valid until:

Status: published

**cx.dcm.base:1**
&quot;(i) Sending and receiving product-specific demand and capacity data, as well as the associated product functionalities 
(ii) early identification of imbalances resulting from demand and capacity comparison, 
(iii) messages and notifications related to imbalances and to exchanged demand and capacity data, 
(iv) initiate a collaborative approach to solve imbalances.

As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for:
Material Demand,
WeekBasedCapacityGroup,
IdBasedRequestForUpdate,
IdBasedComment

Valid from: 2024-06-20

Valid until:

Status: published

**cx.puris.base:1**
&quot;Optimizing processes, which includes, without limitation, regular exchange
of data to prevent and/or solve shortages in the supply chain, conducting
plausibility checks against other sources and/or collecting information to facilitate sound decision making, all of the above in the context of predictive
unit real-time information relating to production and/or logistics.

As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for:
Item Stock,
Short-Term Material Demand,
Planned Production Output,
Delivery Information

Valid from: 2024-06-20

Valid until:

Status: published

**cx.circular.dpp:1**
&quot;Exchange and use of data according to the applicable public legal regulation directly requiring digital product passports or affecting the contents or handling of digital product passports. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for:
Digital Product Pass,
Battery Pass

Valid from: 2024-06-20

Valid until:

Status: published

**cx.circular.smc:1**
&quot;Exchanging information about secondary material content (SMC) to optimize SMC-usage. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for:
SMC-Calculated,
SMC-Verifiable

Valid from: 2024-06-20

Valid until:

Status: published

**cx.circular.marketplace:1**
&quot;Buy, sell and/or procure  parts and material. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for: Market Place Offer

Valid from: 2024-06-20

Valid until:

Status: published

**cx.circular.materialaccounting:1**
&quot;Display, process, analysis, correlate, modify and amend data. Use of data for (e.g. enablement of) chain of custody processes and commercial transaction related thereto and allocation of material to parts to the supply chain. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for:

Valid from: 2024-06-20

Valid until:

Status: published

**cx.bpdm.gate.upload:1**
&quot;Verifying, curating and enriching data to create a record of basic information about all entities with a BPN in the CX Data Space accessible to all Participants (&quot;Golden Record&quot;) and for early warning services (value-added services, &quot;VASs&quot;). As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for: Gate Data Model

Valid from: 2024-06-20

Valid until:

Status: published

**cx.bpdm.gate.download:1**
&quot;Providing basic information about entities with a BPN in the CX Data Space for Data Consumer to identify counterparty and/or for VASs. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for: Gate Data Model

Valid from: 2024-06-20

Valid until:

Status: published

**cx.bpdm.pool:1**
&quot;Identifying Participants within the CX Data Space for Data Consumer's internal counterparty identification and information processes and/or for VASs. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for: Pool Data Models

Valid from: 2024-06-20

Valid until:

Status: published

**cx.bpdm.vas.dataquality.upload:1**
&quot;Screening Data Provider's data (i) to assess Data Provider's data quality and (ii) to create benchmarks for future screenings of other Participants' data by Data Consumer to fulfill the goals of the DQD application. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for: BP Data Model

Valid from: 2024-06-20

Valid until:

Status: published

**cx.bpdm.vas.dataquality.download:1**
&quot;Data Consumer assessing quality of own data. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for: DQD data Model

Valid from: 2024-06-20

Valid until:

Status: published

**cx.bpdm.vas.bdv.upload:1**
&quot;Screening relevant Data Provider's bank data to verify Data Provider's bank data. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for:
Gate Data Model,
BDV Data Model

Valid from: 2024-06-20

Valid until:

Status: published

**cx.bpdm.vas.bdv.download:1**
&quot;Verifying Data Consumer's submitted bank data. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for: BDV Data Model

Valid from: 2024-06-20

Valid until:

Status: published

**cx.bpdm.vas.fpd.upload:1**
&quot;Screening Data Provider's business partner data to assess fraud. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for: FP Data Model

Valid from: 2024-06-20

Valid until:

Status: published

**cx.bpdm.vas.fpd.download:1**
&quot;Data Consumer assessing fraud risks when transacting with another Participant. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for: FP Data Model

Valid from: 2024-06-20

Valid until:

Status: published

**cx.bpdm.vas.swd.upload:1**
&quot;Screening Data Provider's beneficial ownership data to assess trade compliance. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for: Gate Data Model

Valid from: 2024-06-20

Valid until:

Status: published

**cx.bpdm.vas.swd.download:1**
&quot;Data Consumer assessing trade sanction risks when transacting with another Participant. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for: SWD Data Model

Valid from: 2024-06-20

Valid until:

Status: published

**cx.bpdm.vas.nps.upload:1**
&quot;Verifying Data Provider's Business Partner Data against natural person data entries. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for: Gate Data Model

Valid from: 2024-06-20

Valid until:

Status: published

**cx.bpdm.vas.nps.download:1**
&quot;Data Consumer verifying its own Business Partner Data. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for: NPS Data Model

Valid from: 2024-06-20

Valid until:

Status: published

**cx.bpdm.vas.countryrisk:1**
&quot;Screening Participants’ business data to identify risks when collaborating with a new/existing business partner according to official or company-specific country risk assessments. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for:
Country Risk Data Model,
Gate Data Model,
Pool Data Models

Valid from: 2024-06-20

Valid until:

Status: published

**cx.core.digitalTwinRegistry:1**
&quot;Identifying data offers of submodels within the Catena-X ecosystem. As a purpose-specific requirement, the duration of (i) contract, (ii) data provision and (iii) usage right(s) as a default are all specified as 1 year.&quot;

Typically used for: DTR Asset

Valid from: 2024-06-20

Valid until:

Status: published



