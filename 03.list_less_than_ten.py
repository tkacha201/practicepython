# first way, using the built in filer function, using an iterable and casing it to a list


def less_than_ten(user_list: list): return list(filter(lambda x: x < 10, user_list))


#second way, using list comprehension


def less_than_ten2(user_list: list): return [x for x in user_list if x < 10]
if __name__ == "__main__":
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print(less_than_ten(a))
    print(less_than_ten2(a))