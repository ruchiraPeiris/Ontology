from owlready import *
import os.path

root_path = os.path.normpath(os.getcwd() + os.sep + os.pardir)
os.chdir(root_path)

onto_path.append(root_path)
onto = get_ontology('file:../MobileOX.owl').load()
# onto = get_ontology('https://www.gsmarena.com/ontologies/MobileOX.owl')

print("No of classes :", len(onto.classes))

print("Base URI :", onto.base_iri)
print("Instances :", onto.instances)
print("Properties :", onto.properties)
print("Annotation properties :", onto.annotation_properties)
print("Disjoints :", onto.all_disjoints)

