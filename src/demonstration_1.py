"""
Define a function that transforms a given string into a new string where the
original string was split into strings of a specified size.

For example:
If the input string was this:

"supercalifragilisticexpialidocious"

and the specified size was 3, then the return string would be:

"sup erc ali fra gil ist ice xpi ali doc iou s"

The assumptions we are making about our input are the following:

- The input string's length is always greater than zero.
- The string has no spaces.
- The specified size is always a positive integer.
"""


# This function should an array
def split_in_parts(s, part_length):
    # Your code here
    # we need to split the input string into smaller chunks of whatever
    # the specified size is
    # init an output array
    #    const output = [];
    output = []
    # iterate over characters in the input string
    # keep a counter that will count up to `part_length` characters
    # check if our counter is equal to `part_length`
    # then we've collected enough chars for a single substring
    # add that collected substring to an array
    # start the counter over the again
    # otherwise
    # increment our counter
    # add the current character to the substring we're building up
    # return our output array
    output = []
    for index in range(0, len(s), part_length):
        output.append(s[index: index + part_length])
    return output


#