"""
Write a function that takes in a two-dimensional list (a list that contains
lists) and returns a new list which contains only the lists from the original
which:

1. were not empty
2. have items that are all of the same type

You can assume that the lists inside the list will only contain integers or
strings. Also, for this challenge, we are assuming that empty arrays are not
homogenous. Also, the resultant lists should be in the same order as the
original list and none of the values should be changed.

**Example:**

Given `[[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]]`, your function should
return `[[1, 5, 4], ['b']]`.
"""


def filter_homogenous(arrays):
    # Your code here
    list = []
    list2 = []
    if len(arrays) == 0:
        return None
    for x in arrays:
        if x == []:
            continue
        # if len(x) == 1:
        #     list.append(x)
        # print(type(x[0]))
        for y in x:
            list2.append(isinstance(y, type(x[0])))
            # check that when list2 is the same size as x and all of the elements inside list2 are true
            # then proceeed to append list2 to list1 which will contain  only lists where all datatypes are the same
            if len(list2) == len(x) and all(list2):
                list.append(x)
                list2 = []
        # reset list2 to all start back as an empty list for every list inside the list of arrays
        list2 = []
    return list
