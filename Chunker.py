import nltk
from nltk.chunk import ChunkParserI
from nltk.chunk.util import tree2conlltags, conlltags2tree
class ClassifierChunker(nltk.chunk.ChunkParserI):
    def __init__(self, train_sents):
        tag_sents = [tree2conlltags(sent)for sent in train_sents]
        train_chunks = [[((w,t),c) for (w,t,c) in sent] for sent in tag_sents]
        train_set = []
        for tagged_sent in train_chunks:
            #print tagged_sent
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                
                featureset = self.featx(untagged_sent, i, history)
                #print featureset,tag
                train_set.append( (featureset, tag) )
                history.append(tag)
        self.classifier = nltk.naivebayes.NaiveBayesClassifier.train(train_set)

    def parse(self, tagged_sent):
        if not tagged_sent: return None
        chunks = self.tag(tagged_sent)
        #print chunks
        return conlltags2tree([(w,t,c) for ((w,t),c) in chunks])
    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            
            featureset = self.featx(sentence, i, history)
            #print featureset
            tag = self.classifier.classify(featureset)
            #print i,word,tag
            #print ""
            history.append(tag)
        return zip(sentence, history)
    
        
    def featx(self,sent, i, history):
        word, pos = sent[i]
        
        if i == 0:
            prevword, prevpos = '<START>', '<START>'
        else:
            prevword, prevpos = sent[i-1]
        if i == len(sent) - 1:
            nextword, nextpos = '<END>', '<END>'
        else:
            nextword, nextpos = sent[i+1]
        return {'pos': pos, 'nextpos': nextpos, 'word': word, 'prevpos': prevpos,'nextword': nextword,'prevword': prevword}




    
    

    
    
         

        
        

    

        


    
    
