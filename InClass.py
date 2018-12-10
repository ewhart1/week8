#!/usr/bin/env python

# script to reverse the seqeuence of a sring of DNA and to generate the complement

# insert a DNA sequence
myString = input("DNA sequence here:")

# This command will convert the characters to lower case in order to delienate differences
myString = myString.lower()

# Next 4 commands replace the original nucleotide with its complement
myString = myString.replace("g", "C")

myString = myString.replace("c", "G")

myString = myString.replace("a", "T")

myString = myString.replace("t", "A")

# print the inverse of compliment sequence
print(myString[::-1])

# DB: Looks good!
