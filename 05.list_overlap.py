# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# # final_list = []
# #
# # for item in a:
# #     if item in b:
# #         final_list.append(item)
# #
# # print(final_list)


# another method using class set data structure

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def list_overlap(a_list: list, b_list: list): return list(set(a_list).intersection(b_list))


if __name__ == '__main__':
    print(list_overlap(a, b))

