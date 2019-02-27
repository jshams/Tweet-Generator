import random
import math


f = open('/usr/share/dict/words' , 'r')
words = f.readlines()
f.close()


'''
x = 0

for word in words:
    print(word[0:-1])
    if x == 10:
        break


sentence_len = input("How many words would you like your sentance to be? (int) ")
while not sentence_len.isdigit():
    sentence_len = input("Invalid input, please enter an integer. ")

output_string = ''
for i in range(0, int(sentence_len)):
    output_string += random.choice(words) + ' '
print(output_string)
'''


def auto_complete(prfx, file):
    for word in file:
        if word[0:len(prfx)] == prfx.lower():
            print(word)
# auto_complete("APPL", words)
def dictogram(list_of_words):
    # histogram = {'one': 1, 'blue': 1, 'two': 1, 'fish': 4, 'red': 1}
    dict = {}
    for word in list_of_words:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    return dict



def anagram(word, dictionary):
    word_dict = dictogram(word)
    for item in dictionary:
        if dictogram(item.lower()) == word_dict:
            print(item)
anagram("brain", words)
