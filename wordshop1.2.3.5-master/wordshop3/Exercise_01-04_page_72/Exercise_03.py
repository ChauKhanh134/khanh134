"""
Author: Tran Chau Khanh
Date: 02/09/2021
Program: Exercise_01-04_page_72.py
Problem:
    Write a format operation that builds a string for the float variable amount that has
    exactly two digits of precision and a field width of zero.

Solution:
    Display:
        3.14

"""
import math
amount = math.pi
print(f"{amount:0.2f}")

