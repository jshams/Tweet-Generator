numbers = [1,2,4,8,3,6,9,90,4,234,2351,352,234,123,65,12,53]

# if highest / middle == middle / lowest its good
# if r % 1 > 0 it doesnt count

# for num in set_of_nums:
    # print(num)
numbers.sort()
# for i in range(len(numbers - 1)):


"""
write a function to check if there is a number before it that has a divisor that is
should take in the index of the number

write two functions:
    one to check if there is a number before it that is a multiple
    next is to write a function that takes that number and sees if there is a number before it with the same divisor
"""
def is_divisor(list, index):
    x = 0
    for i in range(len(list) + index -1):
        if (list[index] / list[index - i - 1]) % 1 == 0:
            # print((list[index] / list[index - i - 1]) % 1)
            x += same_divisor(list, -(i-1), list[index] / list[index - i - 1])
    return x

def same_divisor(list, index, divisor):
    # print(divisor)
    i = index - 1
    while i > -len(list):
        if list[index] / list[i] == divisor:
            # print(divisor)
            print(list[index] , list[i], list[index] / list[i])
            return 1
        i -= 1
    return 0

x = 0
for i in range(len(numbers) - 1):
    x += is_divisor(numbers, -i -1)

print(x)
