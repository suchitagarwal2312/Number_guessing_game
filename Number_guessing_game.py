# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 00:16:28 2021

@author: vasu
"""

import random

number = random.randint(1,100)

print("you have only 3 chances")
for i in range(3):
    choice = int(input("Enter any no. between 1 to 100"))

    if choice == number:
        print("Hoorayyy! it is a right guess")
    elif number > choice:
        print("Guess any larger no.")
    else:
        print("Guess any samller no.")
        
print("real no. is" , format(number))