from rdflib import URIRef, BNode, Literal, Namespace, Graph
from rdflib.namespace import FOAF, DCTERMS, XSD, RDF, SDO

"""knowledge base with RDFLib"""

# create subjects and objects
mona_lisa = URIRef('http://www.wikidata.org/entity/Q12418')
davinci = URIRef('http://dbpedia.org/resource/Leonardo_da_Vinci')
lajoconde = URIRef('http://data.europeana.eu/item/04802/243FA8618938F4117025F17A8B813C5F9AA4D619')

# use namespace to shorten URIs
EX = Namespace('http://example.org/')
bob = EX['Bob']
alice = EX['Alice']

birth_date = Literal("1990-07-04", datatype=XSD['date'])
title = Literal('Mona Lisa', lang='en')

g = Graph()

# Bind prefix to namespace
g.bind('ex', EX)
g.bind('foaf', FOAF)
g.bind('schema', SDO)
g.bind('dcterms', DCTERMS)

# add triples
g.add((bob, RDF.type, FOAF.Person))
g.add((bob, FOAF.knows, alice))
g.add((bob, FOAF['topic_interest'], mona_lisa))
g.add((bob, SDO['birthDate'], birth_date))
g.add((mona_lisa, DCTERMS['creator'], davinci))
g.add((mona_lisa, DCTERMS['title'], title))
g.add((lajoconde, DCTERMS['subject'], mona_lisa))

# print graph
print(g.serialize(format='ttl'))

# Replace Literal value
g.set((bob, SDO['birthDate'], Literal('1990-01-01', datatype=XSD.date)))
g.set((mona_lisa, DCTERMS['title'], Literal('La Joconde', lang='fr')))

# Remove triples from graph
g.remove((mona_lisa, None, None))

# print graph
print(g.serialize(format='ttl'))
