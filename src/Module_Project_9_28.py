"""PROBLEM NUMBER 1"""


def addBorder(picture):
    # we need to have 2 + plus start at the start of the border for the given len of the picture
    answer = ['**']

    for i in range(len(picture[0])):
        answer[0] += '*'

    for i in range(len(picture)):
        answer.append('*')
        for j in range(len(picture[0])):
            answer[i + 1] += picture[i][j]
        answer[i + 1] += '*'

    answer.append(answer[0])

    return answer


# Test 1
# Input:
# picture:
# ["abc",
#  "ded"]
# Output:
# ["*****",
#  "*abc*",
#  "*ded*",
#  "*****"]
# Expected Output:
# ["*****",
#  "*abc*",
#  "*ded*",
#  "*****"]
# Console Output:
# Empty


# Given an array of strings, return another array containing all of its longest strings.
#
# Example
#
# For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
# allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

"""PROBLEM NUMBER 2"""


# There is a bug in one line of the code. Find it, fix it, and submit.
# Given an array of integers, count the odd numbers before the first (i.e. leftmost) occurrence of zero.
#
# Example
#
# For sequence = [1, 2, 3, 0, 4, 5, 6, 0, 1], the output should be
# oddNumbersBeforeZero(sequence) = 2.


def oddNumbersBeforeZero(sequence):
    result = 0
    for i in range(0, len(sequence)):
        if sequence[i] == 0:
            break
        if sequence[i] % 2 == 1:
            result += 1
    return result


"""PROBLEM #3"""


def minMaxDifference(inputArray):
    indexOfMinimum = 0
    indexOfMaximum = 0

    for i in range(1, len(inputArray)):
        if inputArray[i] < inputArray[indexOfMinimum]:
            indexOfMinimum = i
        if inputArray[i] > inputArray[indexOfMaximum]:
            indexOfMaximum = i
    return inputArray[indexOfMaximum] - inputArray[indexOfMinimum]


"""PROBLEM NUMBER 4"""


def allLongestStrings(inputArray):
    # We want to output a list only consisting of the bigest elements
    # Do a for loop and compare the current elemtn in the loop with the previous one
    # Only keep the elements that are the biggest or equal to the biggest
    answer = [inputArray[0]]
    for i in range(1, len(inputArray)):
        if len(inputArray[i]) == len(answer[0]):
            answer.append(inputArray[i])
        if len(inputArray[i]) > len(answer[0]):
            answer = [inputArray[i]]
    return answer


"""PROBLEM NUMBER 5"""


# You are given a two-digit integer n. Return the sum of its digits.
#
# Example
# For n = 29, the output should be
# addTwoDigits(n) = 11.
def addTwoDigits(n):
    # we want to break the integer into two seperate numnbess
    # Then add them together
    n = str(n)
    sum = int(n[0]) + int(n[1])
    print(sum)
    return sum


"""PROBLEM NUMBER 7"""


def reverseSentence(sentence):
    # we want to reverse the sentence
    # we ultimately want to grab the words at the end of the sentence and somehow make them the starting words
    sentence = " ".join(sentence.split()[::-1])
    return sentence


"""PROBLEM #8 """


# To ensure the confidentiality of the stored information,
# the device is locked out of Dropbox after 10 consecutive failed passcode attempts.
# We need to implement a function that, given an array of attempts made throughout the
# day and the correct passcode, checks to see if the device should be locked, i.e. 10 or
# more consecutive failed passcode attempts were made.
#
# Example
#
# For
# passcode = "1111" and
#
# attempts = ["1111", "4444",
#             "9999", "3333",
#             "8888", "2222",
#             "7777", "0000",
#             "6666", "7285",
#             "5555", "1111"]
# the output should be
#
# incorrectPasscodeAttempts(passcode, attempts) = true

def incorrectPasscodeAttempts(passcode, attempts):
    # keep track of counts
    # check if passcode is in attempt for each count
    counts = 0
    for i in attempts:
        if i == passcode:
            counts = 0
        else:
            counts += 1
            if counts >= 10:
                return True
    return False


"""PROBLEM NUMBER 9"""


# Given an integer n, find the difference between the sums of its even and odd digits.
#
# Example
#
# For n = 412, the output should be
# digitSumsDifference(n) = 5;
# For n = 1203, the output should be
# digitSumsDifference(n) = -2.

def digitSumsDifference(n):
    # we want to take the sums btw the odds and evens digits for a given #
    # begin by splitting the number into indiv digits
    # run a for loop adding odds and evens together
    # subtract differe btw sums of evens and sum of odds

    list = [int(x) for x in str(n)]
    odds = 0
    evens = 0
    for x in list:
        if x == 0:
            continue
        elif x % 2 == 0:
            evens += x
        else:
            odds += x
    return evens - odds


""" PROBLEM NUMBER 10"""


# #Given a positive integer number n, your task is to calculate the difference between
# the product of its digits and the sum of its digits.
#
# Note: The order matters; the answer should be of the form product - sum (and not sum - product).
#
# Example
#
# For n = 123456, the output should be digitsManipulations(n) = 699.
#
# The product of the digits is equal to 1 * 2 * 3 * 4 * 5 * 6 = 720.
# The sum of the digits is equal to 1 + 2 + 3 + 4 + 5 + 6 = 21.

def digitsManipulations(n):
    # we want the difference btw the product of digits and the sum of digits
    # like other problems requiring us to work witht the digits in the number
    # we need to split the number into its digits

    # perform a for loop and keep track of product and sum
    # product can start as 1
    # sum will start at 0
    list = [int(x) for x in str(n)]
    print(list)
    product = 1
    sum = 0
    for x in list:
        sum += x
        product = product * x
    return product - sum


"""PROBLEM # 11"""""
# You are given a string s that consists of only lowercase English letters. If vowels ('a', 'e', 'i', 'o', and 'u') are given a value of 1 and consonants are given a value of 2, return the sum of all of the letters in the input string.
#
# Example
#
# For s = "a", the output should be
# countVowelConsonant(s) = 1;
#
# For s = "abcde", the output should be
# countVowelConsonant(s) = 8.

The
letters in s, converted
to
1
s and 2
s and added
together as described
above: 1 + 2 + 2 + 2 + 1 = 8.


def countVowelConsonant(s):
    # want two filter out the characters that are vowere and consontant and
    # keep track of them by adding a 1 or 2 two some variables in the for foor lop
    vowels = ['a', 'e', 'i', 'o', 'u']
    one = 0
    two = 0
    for x in s:
        if x in vowels:
            one += 1
        else:
            two += 2
    return one + two


"""PROBLEM #6"""
# You are given a string s, which consists only of lowercase English letters. Your task is
# to find the number of adjacent triplets of unique characters within s. In other words,
# count the number of indices i, such that s[i], s[i + 1], and s[i + 2] are all pairwise distinct.
#
# Example
#
# For s = "abcdaaae", the output should be threeCharsDistinct(s) = 3.
#
# If i = 0, s[0] = 'a', s[1] = 'b', and s[2] = 'c', which are pairwise distinct;
# If i = 1, s[1] = 'b', s[2] = 'c', and s[3] = 'd', which are pairwise distinct;
# If i = 2, s[2] = 'c', s[3] = 'd', and s[4] = 'a', which are pairwise distinct;
# If i = 3, s[3] = 'd', s[4] = 'a', and s[5] = 'a', which are not pairwise distinct because s[4] and s[5] are equal;
# If i = 4, s[4] = 'a', s[5] = 'a', and s[6] = 'a', which are not pairwise distinct because all pairs of
# characters are equal;
# If i = 5, s[5] = 'a', s[6] = 'a', and s[7] = 'e', which are not pairwise distinct because s[5] and s[6] are equal.
# If i = 6 or i = 7, at least one of characters s[i + 1] or s[i + 2] won't exist.
# For s = "abacaba", the output should be threeCharsDistinct(s) = 2.
#
# There are only 2 indices meeting the criteria:
#
# i = 1: s[1] = 'b', s[2] = 'a', and s[3] = 'c';
# i = 3: s[3] = 'c', s[4] = 'a', and s[5] = 'b'.
# All other triplets will contain more than one a character.
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] string s
#
# A string consisting of lowercase English letters.
#
# Guaranteed constraints:
# 1 ≤ s.length ≤ 1000.
#
# [output] integer
#
# The number of indices i in s, such that characters s[i], s[i + 1], and s[i + 2] all exist and are pairwise distinct.

def threeCharsDistinct(s):
    list = [x for x in s]
    list2 =[]
    counts = 0
    if len(list)<3:
        return 0
    for i in range(0,len(list)):
        if len(list[i:])<2:
            return len(list2)
        if list[i]!= list[i+1] and list[i+1]!=[i+2]:
            list2.append(list[i:i+2])
    return len(list2)