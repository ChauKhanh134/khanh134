"""
Author: Tran Chau Khanh
Date: 03/09/2021
Program: Exercise_01-09_page_85.py
Problem:
    Assume that the variables x and y refer to strings. Write a code segment that prints
    these strings in alphabetical order. You should assume that they are not equal.

Solution:
    Display:
        nho
        loi
"""
x = "loi"
y = "nho"
words = [x, y]
words.sort()
for word in words:
    print(word)


