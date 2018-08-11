from owlready2 import *

onto_path.append("D:/UOM/L04S01/semantic/project/Ontology")
onto = get_ontology("D:/UOM/L04S01/semantic/project/Ontology/Mobile.owl").load()

print(list(onto.classes()))
# print(onto.classes().__next__())
