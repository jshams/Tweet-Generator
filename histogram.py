import random
import sys
#
# f = open('frankenstein.txt', 'r')
# str = f.readlines()
# f.close()
# str = words.split() for words in str

str = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
def histogram_lol_old(list_of_words):
    #list of lists
    # histogram = [['one', 1], ['fish', 4], ['two', 1], ['red', 1], ['blue', 1]]
    # my result = [['one', 1], ['fish', 4], ['two', 1], ['red', 1], ['blue', 1]]
    used_words = []
    lol = []
    for word in list_of_words:
        if word not in used_words:
            used_words.append(word)
            temp_list_of_words = [word, 1]
            lol.append(temp_list_of_words)
        else:
            for list_of_words in lol:
                if word in list_of_words:
                    list_of_words[1] += 1
    return lol

def histogram(list_of_words):
    # list of lists
    hist_lol = []
    for word in list_of_words:
        found = False
        for list in hist_lol:
            if word in list:
                list[1] += 1
                found = True
        if not found:
            hist_lol.append([word, 1])
    return hist_lol

print(histogram(str))



def touplogram(list_of_words):
    #list of touples
    # histogram = [('one', 1), ('fish', 4), ('two', 1), ('red', 1), ('blue', 1)]
    # my result = [('one', 1), ('fish', 4), ('two', 1), ('red', 1), ('blue', 1)]
    list_of_touples = []
    for word in list_of_words:
        in_list = False
        for touple in list_of_touples:
            if word == touple[0]:
                count = touple[1] + 1
                list_of_touples.remove(touple)
                list_of_touples.append((word, count))
                in_list = True
                break
        if not in_list:
            list_of_touples.append((word, 1))
    return list_of_touples
# print(touplogram(str))


# print(touplogram(str))

def dictogram(list_of_words):
    # histogram = {'one': 1, 'blue': 1, 'two': 1, 'fish': 4, 'red': 1}
    dict = {}
    for word in list_of_words:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    return dict




def countagram(list_of_words):
    countagram = [(1, [])]
    for word in list_of_words:
        found = False
        incrementor = 0
        while incrementor < len(countagram) and found == False:
            if word in countagram[incrementor][1]:
                found = True
                temp_list = countagram[incrementor][1]
                temp_list.remove(word)
                countagram[incrementor] = (countagram[incrementor][0] , temp_list)
                # if the word was found in the last list create a new one
                if countagram[incrementor] == countagram[-1]:
                    countagram.append((countagram[incrementor][0] + 1, [word]))
                # if the next list's number is one more, add the word to that list
                elif countagram[incrementor][0] == countagram[incrementor + 1][0] - 1:
                    temp_list = countagram[incrementor + 1][1]
                    temp_list.append(word)
                    countagram[incrementor + 1] = (countagram[incrementor + 1][0], temp_list)
                # if the next list is not one more and the list isnt the last
                else:
                    countagram.insert(incrementor + 1, (countagram[incrementor][0] + 1 , [word]))
                if len(countagram[incrementor][1]) == 0:
                    countagram.pop(incrementor)
            incrementor += 1
        if found == False:
            if countagram[0][0] == 1:
                temp_list = countagram[0][1]
                temp_list.append(word)
                countagram[0] = (1, temp_list)
            else:
                countagram.insert(0, (1, [word]))
    return countagram

# def sample_words_by_frequency(histogram, n):
#     sample_size = 0
#     for element in histogram:
#         sample_size += element[1]
#     range = 0
#     for element in histogram:
#         range += element[1] / sample_size
#         element.append(range)
#     incrementor = 0
#     list_of_outputs = []
#     while incrementor < n:
#         rando = random.random()
#         for element in histogram:
#             if element[2] > rando:
#                 list_of_outputs.append((element[0]))
#                 break
#         incrementor += 1
#     return list_of_outputs


def hist_probability_distribution(histogram):
    # takes in a dictogram (list of lists)
    sample_size = 0
    for element in histogram:
        sample_size += element[1]
    range = 0
    list_of_values = []
    for element in histogram:
        range += element[1] / sample_size
        list_of_values.append(range)
    return list_of_values

def sample_word(histogram, probability_distribution):
    rando = random.random()
    for i in range(len(probability_distribution)):
        if probability_distribution[i] > rando:
            return histogram[i][0]

def sample_words_by_frequency(histogram, n = 1):
    probability_distribution = hist_probability_distribution(histogram)
    output_string = ''
    for i in range(n):
        random_word = sample_word(histogram, probability_distribution)
        output_string += random_word + ' '
    return output_string

# print(sample_words_by_frequency(histogram(str), 10))


# '''
# should return a histogram of the outputs but "TypeError: 'list' object is not callable"
# while this is being figured out it will return a list of the outputs
# '''


def test_relative_probabilities(histogram, random_outputs):
    sample_size = 0
    for element in histogram:
        sample_size += element[1]
    for element in histogram:
        element[1] = element[1]/sample_size
    # print(histogram(random_outputs))
    print(histogram)
    return histogram

def reverse_word_sentences(sentence):
    half_len = int(len(sentence) / 2)
    x = 0
    while x < half_len:
        sentence[x], sentence[-(x+1)] = sentence[-(x+1)], sentence[x]
        x += 1
    return sentence
