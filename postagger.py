from nltk.tag.sequential import ClassifierBasedPOSTagger
from nltk.corpus import treebank

def making_tagger():
    train=treebank.tagged_sents()[:3000]
    tagger = ClassifierBasedPOSTagger(train=train)
    return tagger

