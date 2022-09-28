#!/usr/bin/python3
"""
Contains the number_of_lines function
"""

def write_file(filename="", text=""):
     """returns the number of lines of a text file"""
     with open(filename, 'r', encoding='utf-8')as f:
         i = 0
         for line in f
            i += 1
        return i
