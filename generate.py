# Copyright (c) 2023 - for information on the respective copyright owner
# see the NOTICE file and/or the repository
# https://github.com/catenax-eV/cx-odrl-profile
#
# SPDX-License-Identifier: Apache-2.0

import rdflib
from string import Template

TABLE_DEF ="""
<pre class='simpledef'>
Definition: $definition
Label: $label
Identifier: $identifier
Note: $note
Class: $myclass
</pre>
"""

def generate(fn: str, out_fn: str):

    data = None
    with open(fn, 'rt') as f:
        data = f.read()

    g = rdflib.Graph()
    g.parse(data=data, format='turtle')

    query = """
    prefix : <http://www.catena-x.net/ns/policy/>
    prefix odrl: <http://www.w3.org/ns/odrl/2/>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?x ?label ?definition ?note ?scopeNote
    WHERE {
        ?x a odrl:leftOperand .
        ?x rdfs:label ?label .
        ?x skos:definition ?definition .
        ?x skos:note ?note .
        ?x skos:scopeNote ?scopeNote
    }
    """

    qres = g.query(query)
    data = ""
    for row in qres:
        print(f"{row.x} {row.label}")
        item = Template(TABLE_DEF).substitute(
            definition = row.definition,
            label = row.label,
            identifier = row.x,
            note = row.note,
            myclass = 'odrl.leftOperand',
        )
        data = data + item + "\n"
    with open(out_fn, 'wt') as f:
        f.write(data)


if __name__ == '__main__':
    generate('policy.ttl', 'ttl_generated_content.md')