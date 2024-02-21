# Copyright (c) 2023 - for information on the respective copyright owner
# see the NOTICE file and/or the repository
# https://github.com/catenax-eV/cx-odrl-profile
#
# SPDX-License-Identifier: Apache-2.0

import rdflib
import json
from string import Template
import chevron

TABLE_DEF ="""
### $title
<pre class='simpledef'>
Identifier: <a href="$identifier">$identifier</a>
Definition: $definition
Label: $label
Note: $note
Class: $myclass
SubClassOf: <a href="$subclassOf">$subclassOf</a>
</pre>
"""

def query_prepare(query_for: str = 'odrl:LeftOperand'):
    query_template = """
    prefix : <https://w3id.org/catenax/policy/#>
    prefix odrl: <http://www.w3.org/ns/odrl/2/>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?x ?label ?definition ?note ?scopeNote ?subclassOf ?xnoprefix
    WHERE {
        ?x a $query_for .
        OPTIONAL { ?x rdfs:label ?label . }
        OPTIONAL { ?x skos:definition ?definition . }
        OPTIONAL { ?x skos:note ?note . }
        OPTIONAL { ?x skos:scopeNote ?scopeNote . }
        OPTIONAL { ?x rdfs:subClassOf ?subclassOf . }
        bind(strafter(str(?x),str(:)) as ?xnoprefix)
    }
    """
    query = Template(query_template).substitute(
        query_for = query_for,
    )
    return query

def generate(fn: str, out_fn: str):

    data = None
    with open(fn, 'rt') as f:
        data = f.read()

    g = rdflib.Graph()
    g.parse(data=data, format='turtle')

    data = ""
    mustache_data = {}
    for q in [
            'odrl:LeftOperand', 'odrl:RightOperand', ':usecaseFrameworkRightOperand', ':contractPurposeRightOperand']:
        query = query_prepare(query_for=q)
        qres = g.query(query)
        data = data + f"{q} classes\n======================================"

        for row in qres:
            # mustache Readme approach
            if not q in mustache_data:
                mustache_data[q] = []
            mustache_data[q].append({
                'title': str(row.xnoprefix),
                'definition': str(row.definition),
                'label': str(row.label),
                'identifier': str(row.x),
                'note': str(row.note),
                'myclass': str(q),
                'subclassOf': str(row.subclassOf) or '',
            })

            print(f"{row.x} {row.label}")
            print(f"{row.xnoprefix}")

            # generate a file to integrate with 'bikeshed'
            item = Template(TABLE_DEF).substitute(
                title = row.xnoprefix,
                definition = row.definition,
                label = row.label,
                identifier = row.x,
                note = row.note,
                myclass = q,
                subclassOf = row.subclassOf or '',
            )
            data = data + item + "\n"

    with open(out_fn, 'wt') as f:
        f.write(data)

    # now the mustache version of it
    profile_template = ''
    with open('profile_template.md', 'rt') as f:
        profile_template = f.read()
    args = {
        'template': profile_template,
        'data': mustache_data
    }
    rendered_profile = chevron.render(**args)
    with open('profile.md', 'wt') as f:
        f.write(rendered_profile)


if __name__ == '__main__':
    generate('profile.ttl', 'ttl_generated_content.md')