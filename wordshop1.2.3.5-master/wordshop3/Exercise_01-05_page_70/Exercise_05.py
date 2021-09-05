"""
Author: Tran Chau Khanh
Date: 02/09/2021
Program: Exercise_01-05_page_70.py
Problem:
        Assume that the variable teststring refers to a string. Write a loop that prints
    each character in this string, followed by its ASCII value.

Solution:
    Display:
       A = 84; n = 117; h = 110;

"""
name = "Khanh"
for i in name:
    print(i, "=", ord(i), end="; ")


