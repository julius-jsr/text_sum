from nltk.tag import TaggerI, untag

class ClassifierTagger(TaggerI):
    def __init__(self, feature_extractor, classifier):
        self.feature_extractor = feature_extractor
        self.classifier = classifier

    def tag(self,sent):
        history=[]

        for i,word in enumerate(sent):
            featureset = self.feature_extractor(sent,i,history)
            tag= self.classifier.classify(featureset)
            history.append(tag)

        return zip(sent,history)
    @classmethod

    def train(cls,train_sents, feature_extractor, classifier_cls,**kwargs):
        train_set = []

        for tagged_sent in train_sents:
            untagged_sent = untag(tagged_sent)
            history = []

            for i, (word,tag) in enumerate(tagged_sent):
                featureset = feature_extractor(untagged_sent,i, history)
                train_set.append((featureset,tag))
                history.append(tag)
        classifier = classifier_cls.train(train_set, **kwargs)
        return cls(feature_extractor, classifier)
    

        
        

    
