def filter_list(l):
    """
    return a new list with the strings filtered out
    """

    return [item for item in l if type(item) is int]


print(filter_list([1, 5, 7, 'abc', 6]))
print(filter_list([1, 5, 9.789, [23, 4], {4, 3}, 7, 209, 'abc', 6]))
