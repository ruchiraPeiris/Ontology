from owlready2 import *
import numpy as np


root_path = os.path.normpath(os.getcwd() + os.sep + os.pardir) + '/Ontology'
os.chdir(root_path)
print(root_path)
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
# SSS
#
# print(onto.search(hasPrice = 30000))
# print(onto.search(iri = "*TouchScreen"))

sync_reasoner(my_world)
graph = my_world.as_rdflib_graph()


# find users who have phones that cost more than the given price
def findUsersByPrice(price):
    r = list(graph.query("""
                SELECT ?u ?p
                WHERE {
                ?s <https://www.gsmarena.com/ontologies/mobile.owl#hasPrice> ?p.
                ?u <https://www.gsmarena.com/ontologies/mobile.owl#uses> ?s.
                }"""))
    r = np.asarray(r)
    users_list = list(())

    for item in r:
        if int(item[1]) > int(price):
            users_list.append((item[0].split('#')[1], item[1]))
    print(users_list)
    return users_list


# recommend phones to users based on brand and OS
def recommendPhone(brand, os):
    uri = '<https://www.gsmarena.com/ontologies/mobile.owl#'
    r = list(graph.query("""PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
                            SELECT ?model
                            WHERE {
                            ?model rdfs:subClassOf <https://www.gsmarena.com/ontologies/mobile.owl#SmartPhone>.
                            ?mi a ?model.
                            ?b a """ + uri + brand + """>.
                            ?o a """ + uri + os + """>.
                            ?mi <https://www.gsmarena.com/ontologies/mobile.owl#hasBrand> ?b.
                            ?mi <https://www.gsmarena.com/ontologies/mobile.owl#hasOS> ?o.
                            }"""))
    r = np.asarray(r)
    recommend = []
    for i in r:
        recommend.append(np.char.split(i, sep='#')[0][1])

    recommend = np.asarray(recommend)
    return recommend


# recommend phones based on chipset
def RecommendOnChipset(chipset):
    uri = '<https://www.gsmarena.com/ontologies/mobile.owl#'
    r = list(graph.query("""PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
                            SELECT ?model
                            WHERE {
                            ?model rdfs:subClassOf <https://www.gsmarena.com/ontologies/mobile.owl#SmartPhone>.
                            ?mi a ?model.
                            ?b a """ + uri + chipset + """>.
                            ?mi <https://www.gsmarena.com/ontologies/mobile.owl#hasChipset> ?b.
                            }"""))
    r = np.asarray(r)
    recommend = []
    for i in r:
        recommend.append(np.char.split(i, sep='#')[0][1])
        # print(np.char.split(i, sep = '#'))

    recommend = np.asarray(recommend)
    return recommend


def teenPhone(ageGroup):
    uri = '<https://www.gsmarena.com/ontologies/mobile.owl#'
    r = list(graph.query("""PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
                            SELECT ?brand
                            WHERE {
                            ?user a """ + uri + ageGroup + """>.
                            ?model rdfs:subClassOf <https://www.gsmarena.com/ontologies/mobile.owl#SmartPhone>.
                            ?phone a ?model.
                            ?user <https://www.gsmarena.com/ontologies/mobile.owl#uses> ?phone.
                            ?phone <https://www.gsmarena.com/ontologies/mobile.owl#hasBrand> ?b.
                            ?b a ?brand.
                            }"""))

    r = np.asarray(r)
    # r = r.flatten()
    b = []
    for i in r:
        b.append(np.char.split(i, sep='#')[0][1])
    b = np.asarray(b)
    brands = []
    for i in b:
        if i != 'NamedIndividual':
            brands.append(i)

    unique, pos = np.unique(brands, return_inverse=True)
    counts = np.bincount(pos)
    maxpos = counts.argmax()

    return brands[maxpos]


