# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# b = [i for i in a if i % 2 == 0]
#
# print(b)

# other ways to do this

def listComp1(user_list: list): return list(filter(lambda x: x % 2 == 0, user_list))


def listComp2(user_list: list): return [x for x in user_list if x % 2 == 0]


if __name__ == '__main__':
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print(listComp1(a))
    print(listComp2(a))
