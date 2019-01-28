import random
import sys

arr = [0,1,2,3,4,5,6,7,8,9]

def shuffle(arr):
    shuffled_arr = []
    while len(arr) != 0:
        x = random.choice(arr)
        arr.remove(x)
        shuffled_arr.append(x)
    return shuffled_arr

# print(shuffle(arr))

str_input = sys.argv[1:]
print(", ".join(shuffle(str_input)))
