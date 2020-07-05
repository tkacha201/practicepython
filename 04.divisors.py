
# number_input = int(input("Please enter a whole number: "))
#
#
# x = range(1, number_input + 1)
#
#
# for elem in x:
#     if number_input % elem == 0:
#         print(elem)


# another way to write this out only looking halfway, checking if user inputs something other than an int
from math import ceil


def divisors(number_input: int):
    for i in range(2, ceil(number_input/2) + 1):
        if number_input % i == 0:
            yield i


if __name__ == "__main__":
    while True:
        try:
            number_input = int(input("Please enter a whole number: "))
            break
        except ValueError:
            print("You did not enter a whole number!")
    print(list(divisors(number_input)))