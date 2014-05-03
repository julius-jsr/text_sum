
Requirements:
----------------------
python 2.7
nltk 2.0.4
Numpy 1.6.2
pyYAML 3.11

you also need to download nltk data to run the program
---------------------------------------------------------


the program will take a text document as an input and genrates a ER graph.

it identifies the entity and the relation between them.
----------------------------------------------------------




process.py is the main file.

you need to run process.py.

then

invoke :
ie_preprocess(document)

here document is the piece of code.

last list shows the list of nodes of the ER graph.

eg:
process.py

document="""The iPhone is a line of smartphones designed and marketed by Apple Inc. It runs Apple's iOS mobile operating system. The first generation iPhone was released on June 29, 2007. The most recent iPhones, the seventh-generation iPhone 5C and iPhone 5S, were introduced on September 10, 2013."""

ie_preprocess(document)



