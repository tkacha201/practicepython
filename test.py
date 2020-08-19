# word = '12345'
# print(word[::1])


#start index:stop index:step index

# import random
#
# numlist = []
# list_length = random.randint(5, 15)
#
# while len(numlist) < list_length:
#     numlist.append(random.randint(1, 75))
#
# evenlist = [number for number in numlist if number % 2 == 0]
#
# print(numlist)
# print(evenlist)

#get random list and print even numbers




list_random = [1,2,3,4,5,6]
list_randomish = [4,2,3,10,11,213,4234,354356]
c = []



for i in range(len(list_random)):
    for j in range(len(list_randomish)):
        if list_random[i] == list_randomish[j]:
            c.append(list_random[i])
        else:
            pass
print(c)