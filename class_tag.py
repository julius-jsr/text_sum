import nltk
import nltk.tag
import re
from nltk.corpus import wordnet
def pos_features(tokens,index,history):
    word = tokens[index]
    if index == 0:
        prevword = prevprevword = None
        prevtag = prevprevtag = None
    elif index == 1:
        prevword = tokens[index-1].lower()
        prevprevword = None
        prevtag = history[index-1]
        prevprevtag = None
    else:
        prevword = tokens[index-1].lower()
        prevprevword = tokens[index-2].lower()
        prevtag = history[index-1]
        prevprevtag = history[index-2]

    if re.match('[0-9]+(\.[0-9]*)?|[0-9]*\.[0-9]+$', word):
        shape = 'number'
    elif re.match('\W+$', word):
        shape = 'punct'
    elif re.match('[A-Z][a-z]+$', word):
        shape = 'upcase'
    elif re.match('[a-z]+$', word):
        shape = 'downcase'
    elif re.match('\w+$', word):
        shape = 'mixedcase'
    else:
        shape = 'other'

    syn= wordnet.synsets(word.lower())
    v='no'
    n='no'
    r='no'
    a='no'

    if len(syn) is 0:
        identity='unknown'
    else:
        identity='known'
    for s in syn:
        if s.pos=='v':
            v='yes'
        if s.pos=='n':
            n='yes'
        if s.pos=='r':
            r='yes'
        if s.pos=='a':
            a='yes'
        

    

    features = {
        'len':len(word),
        'a':a,
        'v':v,
        'r':r,
        'n':n,
        'prevtag': prevtag,
        'prevprevtag': prevprevtag,
        'word': word,
        'word.lower': word.lower(),
        'identity':identity,
        'suffix3': word.lower()[-3:],
        'suffix2': word.lower()[-2:],
        'suffix1': word.lower()[-1:],
        'prevprevword': prevprevword,
        'prevword': prevword,
        'prevtag+word': '%s+%s' % (prevtag, word.lower()),
        'prevprevtag+word': '%s+%s' % (prevprevtag, word.lower()),
        'prevword+word': '%s+%s' % (prevword, word.lower()),
        'shape': shape,
         }
             


    return features



class ConsecutivePosTagger(nltk.TaggerI):
    def __init__(self,train_sents):
        train_set = []
        for tagged_sent in train_sents:
            untagged_sent  = nltk.tag.untag(tagged_sent)
            history =[]
            for i, (word,tag) in enumerate(tagged_sent) :
                featureset = pos_features(untagged_sent, i, history)
                train_set.append((featureset,tag))
                history.append(tag)
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)


    def tag(self,sentence):
        history = []
        for i, word in enumerate(sentence):
            featureset = pos_features(sentence,i,history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence,history)
 

                
        
