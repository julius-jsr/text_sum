import nltk.tokenize
from nltk.tag.sequential import ClassifierBasedPOSTagger
from nltk.corpus import treebank
import postagger
import trainChunker
from cPickle import load
from nltk.corpus import conll2000
import sys
import class_tag
from class_tag import *

import printNP
i=0
j=0
x=0

def traversing(temp1):
    print "sid", temp1.sent_id
    if temp1.related_with!=None:
        print temp1.related_with.phrase
    if temp1.relation!=None:
        print temp1.relation.phrase
    
    print "phrase",temp1.phrase
    
   
                    #print "phrase222",temp.related_to[0].phrase
    if len(temp1.related_to)==0:
        return
    for x in temp1.related_to:
        traversing(x)
                    
    

def ie_preprocess(document):
    ph=sys.stdout
    #sys.stdout= open("abc.txt","w")
    global i
    global j
    global x
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    inp=open("ppp.p","rb")
    t=load(inp)
    inp.close()
    sentences = [t.tag(sent) for sent in sentences]
    #print sentences
    l=[]
    for i,t in enumerate(sentences):
        for x in t:
            dic={}
            dic['sent_id']=i
            dic['word']=x[0]
            dic['pos']=x[1]
            l.append(dic)
    #print l
            
        
    inp= open("chunking.p","rb")
    chunker=load(inp)
    inp.close()
    print "done"
    ch= [chunker.parse(sent) for sent in sentences]
    #print chunker.classifier.show_most_informative_features(50)
    print ""
    #print ch
    #test_sents = conll2000.chunked_sents('test.txt')
    #print chunker.evaluate(test_sents)
    al=[]
    gr=[]
    for i,t in enumerate(ch):
        m=[]
        z=printNP.printn()
        print ""
        head=None
        head=z.print_NP(t,i,gr,head=None)
        #print "head out ",head
        #if head!=None:
           # print len(head.related_to)
            #for temp in head.related_to:
               #traversing(temp)
        
        m=z.col
        head.related_to=[]
        #print m
        print ""
        al.append(m)
        for w in z.col:
            z.col.remove(w)
        z.y=0
        z.x=0
        z.prevt=0
        z.vp=0
        z.pp=0
        z.np=0
        z.pnp=0
        z.prevk=0
        
    #print al
    #sys.stdout.close()
    sys.stdout=ph
    print"***************************************"
    print"LIST OF NODES OF ER GRAPH:-"
    print""
    print gr
    print "done"
    return

