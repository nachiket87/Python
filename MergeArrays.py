my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]

def merge_lists(list1, list2):
    return list(set(sorted(list1 + list2)))


print(merge_lists(my_list, alices_list))


