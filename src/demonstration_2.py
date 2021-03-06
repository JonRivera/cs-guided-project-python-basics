"""
You have been asked to implement a line numbering feature in a text editor that
you are working on.

Write a function that takes a list of strings and returns a new list that
contains each line prepended by the correct number.

The numbering starts at 1 and the format should be `line_number: string`. Make
sure to put a colon and space in between the `line_number` and `string` value.

Examples:
number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]
"""
# use enumerate or run some for loop that keeps track of both the element and index


def number(lines):
    # Your code here
    list = []
    for i, x in enumerate(lines):
        list.append(str(i + 1) + ":" + str(x))
    return list
