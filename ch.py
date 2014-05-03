Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from Tagger import ClassifierTagger
>>> from Chuker import ClassifierChunker

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    from Chuker import ClassifierChunker
ImportError: No module named Chuker
>>> from Chunker import ClassifierChunker
>>> from nltk.corpus import conll2000
>>> from nltk.classify import MaxentClassifier
>>> train_sents = conll2000.chunked_sents('train.txt')
>>> def pos(sent, i, history):
    word, pos = sent[i]
    return {'pos': pos}

>>> chunker = ClassifierChunker(train_sents, featx, MaxentClassifier,
    min_lldelta=0.01, max_iter=10)

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    chunker = ClassifierChunker(train_sents, featx, MaxentClassifier,
NameError: name 'featx' is not defined
>>> chunker = ClassifierChunker(train_sents, pos, MaxentClassifier,
    min_lldelta=0.01, max_iter=10)

Traceback (most recent call last):
  File "<pyshell#9>", line 2, in <module>
    min_lldelta=0.01, max_iter=10)
  File "Chunker.py", line 9, in __init__
    self.tagger = ClassifierTagger.train(train_chunks, *args, **kwargs)
  File "Tagger.py", line 22, in train
    for tagged_sent in untag(tagged_sent):
UnboundLocalError: local variable 'tagged_sent' referenced before assignment
>>> from Tagger import ClassifierTagger
>>> chunker = ClassifierChunker(train_sents, pos, MaxentClassifier,
    min_lldelta=0.01, max_iter=10)

Traceback (most recent call last):
  File "<pyshell#11>", line 2, in <module>
    min_lldelta=0.01, max_iter=10)
  File "Chunker.py", line 9, in __init__
    self.tagger = ClassifierTagger.train(train_chunks, *args, **kwargs)
  File "Tagger.py", line 22, in train
    for tagged_sent in train_sents:
UnboundLocalError: local variable 'tagged_sent' referenced before assignment
>>> ================================ RESTART ================================
>>> 
>>> chunker = ClassifierChunker(train_sents, pos, MaxentClassifier,
    min_lldelta=0.01, max_iter=10)

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    chunker = ClassifierChunker(train_sents, pos, MaxentClassifier,
NameError: name 'ClassifierChunker' is not defined
>>> from Tagger import ClassifierTagger
>>> from Chuker import ClassifierChunker

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    from Chuker import ClassifierChunker
ImportError: No module named Chuker
>>> from Chunker import ClassifierChunker
>>> from nltk.corpus import conll2000
>>> from nltk.classify import MaxentClassifier
>>> train_sents = conll2000.chunked_sents('train.txt')
>>> def pos(sent, i, history):
    word, pos = sent[i]
    return {'pos': pos}

>>> chunker = ClassifierChunker(train_sents, pos, MaxentClassifier,
    min_lldelta=0.01, max_iter=10)

Traceback (most recent call last):
  File "<pyshell#21>", line 2, in <module>
    min_lldelta=0.01, max_iter=10)
  File "C:\Python27\Chunker.py", line 9, in __init__
    self.tagger = ClassifierTagger.train(train_chunks, *args, **kwargs)
  File "C:\Python27\Tagger.py", line 27, in train
    featureset = feature_extractor(untsgged_sent,i, history)
NameError: global name 'untsgged_sent' is not defined
>>> ================================ RESTART ================================
>>> 
>>> from Tagger import ClassifierTagger
>>> from Chunker import ClassifierChunker
>>> from nltk.corpus import conll2000
>>> from nltk.classify import MaxentClassifier
>>> train_sents = conll2000.chunked_sents('train.txt')
>>> def pos(sent, i, history):
    word, pos = sent[i]
    return {'pos': pos}

>>> chunker = ClassifierChunker(train_sents, pos, MaxentClassifier,
    min_lldelta=0.01, max_iter=10)
  ==> Training (10 iterations)

      Iteration    Log Likelihood    Accuracy
      ---------------------------------------
             1          -1.94591        0.181
             2          -0.52466        0.781
             3          -0.49125        0.781
             4          -0.47042        0.781
             5          -0.45597        0.781
             6          -0.44525        0.781
         Final          -0.43695        0.781
>>> 
