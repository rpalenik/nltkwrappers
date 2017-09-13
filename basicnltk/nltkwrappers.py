class Tokenizer(object):


    def tokenize(self, input_bag, item):
        import nltk
        if item=='None':
            self.output_bag = input_bag.map(nltk.word_tokenize)
        else:
            self.output_bag = input_bag.pluck(item).map(nltk.word_tokenize)
        return self.output_bag

class SentTokenizer(object):

    def sent_tokenize(self, input_bag, item):
        import nltk
        if item=='None':
            self.output_bag = input_bag.map(nltk.word_tokenize)
        else:
            self.output_bag = input_bag.pluck(item).map(nltk.word_tokenize)
        return self.output_bag

class Normalizer(object):

    def cucco_normalize(self, input_bag, item):
        from cucco import Cucco
        cucco = Cucco()
        if item=='None':
            self.output_bag = input_bag.map(cucco.normalize)
        else:
            self.output_bag = input_bag.pluck(item).map(cucco.normalize)
        return self.output_bag

