class Tokenizer(object):


    def tokenize(self, input_bag, item):
        import nltk
        if item=='None':
            self.output_bag = input_bag.map(nltk.word_tokenize, input_bag)
        else:
            self.output_bag = input_bag.pluck(item).map(nltk.word_tokenize, input_bag)
        return self.output_bag
