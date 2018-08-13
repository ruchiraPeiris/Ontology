from owlready2 import *
import numpy as np
from rdflib import *
import os.path

root_path = os.path.normpath(os.getcwd() + os.sep + os.pardir)
os.chdir(root_path)
my_world = World()
onto_path.append(root_path)
onto = my_world.get_ontology('file:../MobileClassesComplete.owl').load()
# onto = get_ontology('https://www.gsmarena.com/ontologies/Mobile_V1.3.owl')


classes = list(())
properties = list(())
annot_properties = list(())

for item in onto.classes():
    classes.append(item)
for item in onto.properties():
    properties.append(item)
for item in onto.annotation_properties():
    annot_properties.append(item)

# print(classes)
# print("No of classes :", len(classes))
# print("Base URI :", onto.base_iri)
# print("Instances :", onto.instances)
# print("Properties :", properties)
# print("Annotation properties :", annot_properties)
# print("Disjoints :", onto.all_disjoints)
#SSS
#
# print(onto.search(hasPrice = 30000))
# print(onto.search(iri = "*TouchScreen"))

sync_reasoner(my_world)
graph = my_world.as_rdflib_graph()

def SampleQuery():
    r = list(graph.query("""
                SELECT DISTINCT ?s ?p
                WHERE {
                ?s <https://www.gsmarena.com/ontologies/mobile.owl#hasPrice> ?p
                }"""))

    r = np.asarray(r)

    for item in r[:, 1]:
        if float(item) > 50000.0:
            print(item)


def recommendPhone(brand, os):
    uri = '<https://www.gsmarena.com/ontologies/mobile.owl#'
    r = list(graph.query("""PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                            PREFIX owl: <http://www.w3.org/2002/07/owl#>
                            SELECT ?model
                            WHERE {
                            ?model rdfs:subClassOf <https://www.gsmarena.com/ontologies/mobile.owl#SmartPhone>.
                            ?mi a ?model.
                            ?b a """ + uri+brand + """>.
                            ?o a """ + uri+os + """>.
                            ?mi <https://www.gsmarena.com/ontologies/mobile.owl#hasBrand> ?b.
                            ?mi <https://www.gsmarena.com/ontologies/mobile.owl#hasOS> ?o.
                            }"""))
    r = np.asarray(r)
    recommend = []
    for i in r:
        recommend.append(np.char.split(i, sep = '#')[0][1])

    recommend = np.asarray(recommend)
    print(recommend)
    return recommend

# SampleQuery()

br = 'Huawei'
oss = 'Oreo'
recommendPhone(br, oss)