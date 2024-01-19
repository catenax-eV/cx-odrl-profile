odrl:LeftOperand classes
======================================
### usecaseFramework
<pre class='simpledef'>
Identifier: <a href="https://w3id.org/catenax/policy/#usecaseFramework">https://w3id.org/catenax/policy/#usecaseFramework</a>
Definition: Legally binding definition goes here. Only predefined values are allowed.
Label: The framework the negotiation is based on. Also known as Use Case Agreement.
Note: None
Class: odrl:LeftOperand
SubClassOf: <a href=""></a>
</pre>


### individualFrameContractReference
<pre class='simpledef'>
Identifier: <a href="https://w3id.org/catenax/policy/#individualFrameContractReference">https://w3id.org/catenax/policy/#individualFrameContractReference</a>
Definition: TODO: LEGAL: A generic / *frame contract* referenced. Both parties are able to identify such a contract by the given identifier value.
Label: An individual Contract as a basis for the exchange
Note: The value for this is a free to choose reference under which both parties are able to identify their contract.
Class: odrl:LeftOperand
SubClassOf: <a href=""></a>
</pre>


### individualContractReference
<pre class='simpledef'>
Identifier: <a href="https://w3id.org/catenax/policy/#individualContractReference">https://w3id.org/catenax/policy/#individualContractReference</a>
Definition: TODO: LEGAL: A very specific data exchange / data usage contract between the parties.
		In consequence the referenced contract is the legal basis instead of a newly created contract during the DSP protocol negotiation.
		The DSP negotiation is NOT considered a a contract negotiation, but only acts as a tool.
Label: An individual Contract as a basis for the exchange
Note: The value for this is a free to choose reference under which both parties are able to identify their contract.
Class: odrl:LeftOperand
SubClassOf: <a href=""></a>
</pre>


### contractPurpose
<pre class='simpledef'>
Identifier: <a href="https://w3id.org/catenax/policy/#contractPurpose">https://w3id.org/catenax/policy/#contractPurpose</a>
Definition: TODO: LEGAL: The provider grants permissions to the transferred data in the described manner.
Label: The purpose of the contract. For what the data is allowed to be used.
Note: Allowed are standardized RightOperands and free text values
Class: odrl:LeftOperand
SubClassOf: <a href=""></a>
</pre>

odrl:RightOperand classes
======================================
### usecaseFrameworkRightOperand
<pre class='simpledef'>
Identifier: <a href="https://w3id.org/catenax/policy/#usecaseFrameworkRightOperand">https://w3id.org/catenax/policy/#usecaseFrameworkRightOperand</a>
Definition: 
Label: Abstract RightOperand class
Note: 
Class: odrl:RightOperand
SubClassOf: <a href=""></a>
</pre>


### contractPurposeRightOperand
<pre class='simpledef'>
Identifier: <a href="https://w3id.org/catenax/policy/#contractPurposeRightOperand">https://w3id.org/catenax/policy/#contractPurposeRightOperand</a>
Definition: 
Label: Abstract RightOperand class
Note: 
Class: odrl:RightOperand
SubClassOf: <a href=""></a>
</pre>

:usecaseFrameworkRightOperand classes
======================================
### frameworkTraceability
<pre class='simpledef'>
Identifier: <a href="https://w3id.org/catenax/policy/#frameworkTraceability">https://w3id.org/catenax/policy/#frameworkTraceability</a>
Definition: TODO: Legal: Both parties accept to use the Traceability Framework as their basis.
Label: Traceability Framework
Note: 
Class: :usecaseFrameworkRightOperand
SubClassOf: <a href="https://w3id.org/catenax/policy/#UsecaseFrameworkRightOperand">https://w3id.org/catenax/policy/#UsecaseFrameworkRightOperand</a>
</pre>


### frameworkPcf
<pre class='simpledef'>
Identifier: <a href="https://w3id.org/catenax/policy/#frameworkPcf">https://w3id.org/catenax/policy/#frameworkPcf</a>
Definition: TODO: Legal: Both parties accept to use the PCF Framework as their basis.
Label: PCF Framework
Note: 
Class: :usecaseFrameworkRightOperand
SubClassOf: <a href="https://w3id.org/catenax/policy/#UsecaseFrameworkRightOperand">https://w3id.org/catenax/policy/#UsecaseFrameworkRightOperand</a>
</pre>


### frameworkQuality
<pre class='simpledef'>
Identifier: <a href="https://w3id.org/catenax/policy/#frameworkQuality">https://w3id.org/catenax/policy/#frameworkQuality</a>
Definition: TODO: Legal: Both parties accept to use the Quality Framework as their basis.
Label: Quality Framework
Note: 
Class: :usecaseFrameworkRightOperand
SubClassOf: <a href="https://w3id.org/catenax/policy/#UsecaseFrameworkRightOperand">https://w3id.org/catenax/policy/#UsecaseFrameworkRightOperand</a>
</pre>

:contractPurposeRightOperand classes
======================================
### legalRequirementForThirdparty
<pre class='simpledef'>
Identifier: <a href="https://w3id.org/catenax/policy/#legalRequirementForThirdparty">https://w3id.org/catenax/policy/#legalRequirementForThirdparty</a>
Definition: TODO: Legal: (from battery traction): Facilitating compliance with mandatory regulatory requirements for tracking and reporting battery cells, modules & high-voltage batteries.
Label: 
Note: 
Class: :contractPurposeRightOperand
SubClassOf: <a href=""></a>
</pre>


### qualityNotifications
<pre class='simpledef'>
Identifier: <a href="https://w3id.org/catenax/policy/#qualityNotifications">https://w3id.org/catenax/policy/#qualityNotifications</a>
Definition: The data can be used for quality analysis to identify and select affected components and to send quality notifications to affected customers or suppliers.
Label: 
Note: 
Class: :contractPurposeRightOperand
SubClassOf: <a href=""></a>
</pre>

