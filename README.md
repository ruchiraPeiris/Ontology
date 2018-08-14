# Ontology

In this implementation we have used Protege 5.2 implement owl about the smart mobile ontology. Other implementation has
done by Python libraries and SPARQL queries.
When selecting Query type from the user interface, User can select different SPARQL query for the different data retreve
and user can assign values for the relevent variable by text fields and dropdonws.
# Example Host
[http://34.239.133.194:4000/](http://34.239.133.194:4000/)  
Note : This link only for development and demonstration purposes not for the other purposes. This host will be automatically 
shutdown within few months (Aug-14-2018 to Sep-13-2018)
## Prerequisites 
* Python 3.6 or above
* Owlready2
* Flask
* rdflib

## Python Interpreter
* System Interpreter
* Anaconda
* Virtual Interpreter

## Java path prerequisite for Owlready2
When using Owlready2, You should define Java path when there error happened by faild to find java path. For the errror
see below,

[Owlready2 * Running HermiT...
    java -Xmx2000M -cp C:\Python35\lib\site-packages\owlready2\hermit;C:\Python35\lib\site-packages\owlready2\hermit\HermiT.jar org.semanticweb.HermiT.cli.CommandLine -c -O -D -I file:///C:/Users/R/AppData/Local/Temp/tmpeb47lx3l
Traceback (most recent call last): ](http://owlready.8326.n8.nabble.com/Error-using-sync-reasoner-td19.html)

