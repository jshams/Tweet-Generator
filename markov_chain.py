str = ['one', 'fish', 'two', 'fish', 'red' ,'fish', 'blue', 'fish']
from dictogram import Dictogram

def markov_chain(word_list):
    mc = {}
    for i, word in enumerate(word_list):
        if i == len(word_list) -1:
            return mc
        if word in mc:
            # THERES A FUNCTION FOR THIS VV
            if word_list[i + 1] in mc[word]:
                mc[word][word_list[i + 1]] += 1
            else:
                mc[word][word_list[i + 1]] = 1
        else:
            mc[word] = {word_list[i + 1]: 1}

print(markov_chain(str))

# Make second order markov chain using dictionary of dictorgrams



class Markov_Chain(Dictogram):
    '''Markov chain is implemented as a subclass of Dictogram'''
    def __init__(self, word_list = None):
        super(Markov_Chain, self).__init__()
        self.word_list = word_list
        if self.word_list is not None:
            self.create(self.word_list)

    def create(self, word_list):
        for i, word in enumerate(word_list):
            if i == len(word_list) - 1:
                return self
            # checks if the word is in the markov chain
            if word in self:
                # checks if the following word is in the word's dictionary
                word.add_count(word_list[i + 1], 1)
            else:
                self[word] = {word_list[i + 1]: 1}


    def sample_word(mc):
