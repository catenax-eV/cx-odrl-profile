import json
import pytest
from pyld import jsonld

context_test = {
    "@context": {
        "policy":   "http://localhost/",
        "odrl":     "http://www.w3.org/ns/odrl/2/",
        
        "@version": 1.1,
        "id": "@id",
        "type": "@type",
        "Action":                "odrl:Action",
        "action":                {"@type": "@vocab", "@id": "odrl:Action"},
        "use":                  "odrl:use",
        "actionTest":           "odrl:Action",
    }
}

def file_document_loader(*args, **kwargs):
    def loader(url, options={}):
        data = ""
        fn = ""
        if url == "http://www.w3.org/ns/odrl/2/":
            fn = "ODRL22.jsonld"
        if url == "https://w3id.org/catenax/policy/":
            fn = "policy.jsonld"
        if url == "https://w3id.org/tractusx/v0.0.1/ns/":
            fn = "tx_terms.json"
        assert fn
        with open(fn, 'rt') as f:
            data = f.read()
        cx = json.loads(data)
        context = {
                'contentType': "application/ld+json",
                'contextUrl': None,
                'documentUrl': url,
                'document': cx,
            }

        return context
    return loader

jsonld.set_document_loader(file_document_loader())

def test_value():
    policy =   {
        "@context": [
            {"odrl": "http://www.w3.org/ns/odrl/2/"},
            #{"cx-policy": "https://w3id.org/catenax/policy/"},
            "https://w3id.org/catenax/policy/",
            #"https://w3id.org/tractusx/v0.0.1/ns/",
        ],

        "@type": "odrl:Policy",
        "odrl:permission": [
        {
            "odrl:action": "use",
            # "odrl:target": "",
            "odrl:constraint": [
            {
                "odrl:leftOperand": "cx-policy:FrameworkAgreement.traceability",
                "odrl:operator": {
                "@id": "odrl:eq"
                },
                "odrl:rightOperand": "active[1.0]"
            }
            # {
            #     "odrl:leftOperand": "contractReference",
            #     "odrl:operator": {
            #     "@id": "odrl:eq"
            #     },
            #     "odrl:rightOperand": "12345"
            # },
            # {
            #     "odrl:leftOperand": "cx-policy:whyPurpose",
            #     "odrl:operator": {
            #     "@id": "odrl:eq"
            #     },
            #     "odrl:rightOperand": "cx-policy:whyLegalRequirementForThirdparty.v1"
            # },
            # {
            #     "odrl:leftOperand": "cx-policy:whyPpurpose",
            #     "odrl:operator": {
            #     "@id": "odrl:eq"
            #     },
            #     "odrl:rightOperand": "cx-policy:whyQualityanalysis.v1"
            # }
            ]
        }
        ]

    }

    #print(json.dumps(doc, indent=True))
    #jsonld.get_document_loader
    doc_expanded = jsonld.expand(policy)
    out = json.dumps(doc_expanded, indent=True)
    print(out)
    with open('debug_expanded.json', 'wt') as f:
        f.write(out)

if __name__ == '__main__':
    #pytest.main([__file__, "-s"])
    test_value()
