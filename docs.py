import nltk
from nltk.classify import apply_features
import random
import nltk.tokenize
from process import * 
from nltk.corpus import movie_reviews
from noise import *

class docs:
    def __init__(self):
        self.documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
        random.shuffle(self.documents)

        all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
        word_features = all_words.keys()[:2000]
        
    
    def document_features(self, document):
        print "document_features entered"
        document_words = set(document)
        features = {}
        #for word in document:
               #features['contains(%s)' % word] = (word in document_words)
        #print document
        f=open("xyz.txt","wb")
        for word in document:
            f.writelines(word+" ")
        f.close()
        de=open("xyz.txt","rb")
        doc=de.read()
        de.close()
        print "ie_process called"
        ie_preprocess(doc,self.t,self.chunker)
        
        noise()
        g=open("efgh.txt","rb")
        st=g.readline()
        while st!="":
            features['contains(%s)' % st] = True
            st=g.readline()
        g.close()
        
        
        return features
    
    
    def train(self):
        print "feature extraxtion..."
        inp=open("ppp.p","rb")
        self.t=load(inp)
        inp.close()
        inp= open("chunking.p","rb")
        self.chunker=load(inp)
        inp.close()
        featuresets = [(self.document_features(d), c) for (d,c) in self.documents]
        self.train_set, self.test_set = featuresets[800:], featuresets[:800]
        print "training start.."
        self.classifier = nltk.NaiveBayesClassifier.train(self.train_set)
        print "testing..."
        print nltk.classify.accuracy(self.classifier, self.test_set)
        return self.classifier
   
    def process(self,document):
        
    
        featuresets = self.document_features(document)
        print self.classifier.classify(featuresets)
