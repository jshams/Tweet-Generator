str = ['one', 'fish', 'two', 'fish', 'red' ,'fish', 'blue', 'fish']
from dictogram import Dictogram
from linkedlist import LinkedList
import random

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

# print(markov_chain(str))

# Make second order markov chain using dictionary of dictorgrams
class Markov_Chain(Dictogram):
    def __init__(self, word_list = None):
        super(Markov_Chain, self).__init__()
        self.word_list = word_list
        if self.word_list is not None:
            self.create(self.word_list)

    def create(self, word_list):
        # OLD CODE
        for i, word in enumerate(word_list):
            if i == len(word_list) - 1:
                return self
            # checks if the word is in the markov chain
            if word in self:
                # checks if the following word is in the word's dictionary
                word.add_count(word_list[i + 1], 1)
            else:
                self[word] = {word_list[i + 1]: 1}


class Second_Order_Markov_Chain(Dictogram):
    '''Markov chain is implemented as a subclass of Dictogram'''
    def __init__(self, word_list = None):
        super(Second_Order_Markov_Chain, self).__init__()
        self.word_list = word_list
        self.length = 0
        if self.word_list is not None:
            self.create(self.word_list)

    def create(self, word_list):
        for i, first_word in enumerate(word_list):
            if first_word == word_list[-2]:
                return
            second_word = word_list[i + 1]
            word_pair = "{} {}".format(first_word, second_word)
            # print(word_pair[2])
            third_word = word_list[i + 2]
            self.add_to_self(word_pair, third_word)

    def add_to_self(self, word_pair, next_word):
        if word_pair in self:
            self[word_pair].add_count(next_word)
        else:
            self[word_pair] = {next_word : 1}
            self.length += 1

    def random_sentence(self, sentence_length):
        if sentence_length <= 0:
            return
        elif sentence_length == 1:
            return random.choice(self.word_list)
        sentence = []
        random_num_from_zero_length = random.randint(0, self.length)
        # print(random_num_from_zero_length)
        # print(self.length)
        i = 0
        for key in self:
            # because dictionaries are unordered this will return a random key
            # print(i, random_num_from_zero_length)
            if random_num_from_zero_length == 0:
                key_as_list = key.split(" ")
                sentence.extend(key_as_list)
                break
            if i == random_num_from_zero_length - 1:
                key_as_list = key.split(" ")
                sentence.extend(key_as_list)
                break
            i += 1
        # now that our sentence has two words we can begin our loop
        x = 2
        while x < sentence_length:
            # print(x)
            # print(sentence)
            word_pair = "{} {}".format(sentence[-2], sentence[-1])
            new_word = self.random_next_word(word_pair)
            if new_word:
                sentence.append(self.random_next_word(word_pair))
            else:
                random_num_from_zero_length = random.randint(0, self.length)
                i = 0
                for key in self:
                    if i == random_num_from_zero_length:
                        key_as_list = key.split(" ")
                        sentence.extend(key_as_list)
                        break
            x += 1
        return " ".join(sentence)

    def random_next_word(self, word_pair):
        if word_pair not in self:
            return False
        rand_prob_dist = []
        total_tokens = 0
        for key in self[word_pair]:
            total_tokens += self[word_pair][key]
        incrementor = 0
        for key in self[word_pair]:
            prob_value = float(self[word_pair][key]) / float(total_tokens) + incrementor
            incrementor = prob_value
            rand_prob_dist.append((key, prob_value))
        rando_num = random.random()
        for i in rand_prob_dist:
            if i[1] > rando_num:
                return i[0]

    # once created we must create a random sentence FUNCTION
      # this should take arguments (self, sentence length)
        # sentence length should be an array
        # first randomly chose a word pair to begin with
        # next randomly chose a next word using next_word method
    # next_word method
      # this should take two arguments (self, word_pair)
        # the function should output a word to follow the word pair

''' print Tests '''
str = ['one', 'fish', 'two', 'fish', 'red' ,'fish', 'blue', 'fish']
my_chain = Second_Order_Markov_Chain(str)
print(my_chain)
print(my_chain.random_sentence(15))

f = open('frankenstein.txt' , 'r')
file = [word for line in f.read().split('\n') for word in line.split(' ')]
f.close()
# print(f)
my_long_chain = Second_Order_Markov_Chain(f)
# print(my_long_chain)
print(my_long_chain.random_sentence(15))
