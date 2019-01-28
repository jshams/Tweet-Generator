import random
import math


f = open('/usr/share/dict/words' , 'r')
words = f.readlines()
f.close()


sentence_len = input("How many words would you like your sentance to be? (int) ")
while not sentence_len.isdigit():
    sentence_len = input("Invalid input, please enter an integer. ")

output_string = ''
for i in range(0, int(sentence_len)):
    output_string += random.choice(words) + ' '
print(output_string)
