from nltk.corpus import conll2000
from nltk.classify import MaxentClassifier
from Chunker import *

def train_chunker():
    train_sents = conll2000.chunked_sents('train.txt')
    chunker = ClassifierChunker(train_sents)
    return chunker

