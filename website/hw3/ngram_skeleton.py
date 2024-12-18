import math, random

################################################################################
# Utility Functions
################################################################################

def start_pad(c):
    ''' Returns a padding string of length n to append to the front of text
        as a pre-processing step to building n-grams '''
    return '~' * c

def ngrams(c, text):
    ''' Returns the ngrams of the text as tuples where the first element is
        the length-n context and the second is the character '''
    pass

def create_ngram_model(model_class, path, c=2):
    ''' Creates and returns a new n-gram model '''
    model = model_class(c)
    with open(path, encoding='utf-8', errors='ignore') as f:
        model.update(f.read())
    return model


################################################################################
# Basic N-Gram Model
################################################################################

class NgramModel(object):
    ''' A basic n-gram model without smoothing '''

    def __init__(self, c):
        pass

    def get_vocab(self):
        ''' Returns the set of characters in the vocab '''
        pass

    def update(self, text):
        ''' Updates the model n-grams based on text '''
        pass

    def prob(self, context, char):
        ''' Returns the probability of char appearing after context '''
        pass

    def random_char(self, context):
        ''' Returns a random character based on the given context and the 
            n-grams learned by this model '''
        pass

    def random_text(self, length):
        ''' Returns text of the specified character length based on the
            n-grams learned by this model '''
        pass

    def perplexity(self, text):
        ''' Returns the perplexity of text based on the n-grams learned by
            this model

        Acknowledgment: 
          https://towardsdatascience.com/perplexity-intuition-and-derivation-105dd481c8f3 
          https://courses.cs.washington.edu/courses/csep517/18au/
          ChatGPT with GPT-3.5
        '''
        
        # Remove any unseen characters
        text = ''.join([c for c in text if c in self.vocab])
        N = len(text)
        
        # Calculate product of the inverse probabilities of the text according to the model
        char_probs = []
        for i in range(self.c, N):
            context = text[i-self.c+2:i]
            char = text[i]
            char_probs.append(math.log2(self.prob(context, char)))
        ppl = 2 ** (-1 * sum(char_probs) / (N - self.c + 2))

        return ppl
