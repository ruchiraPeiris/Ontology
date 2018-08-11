from owlready2 import *
import os.path

root_path = os.path.normpath(os.getcwd() + os.sep + os.pardir)
os.chdir(root_path)

onto_path.append(root_path)
onto = get_ontology('file:../Mobile_V1.3.owl').load()
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

print(classes)
print("No of classes :", len(classes))
print("Base URI :", onto.base_iri)
print("Instances :", onto.instances)
print("Properties :", properties)
print("Annotation properties :", annot_properties)
print("Disjoints :", onto.all_disjoints)


print(onto.search(hasPrice = '*'))
print(onto.search(iri = "*TouchScreen"))
