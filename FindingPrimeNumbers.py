'''
Created on Feb 3, 2018

@author: ITAUser
'''

integer = int(input ("Enter a positive number, except 0:"))
if integer > 1:
    for i in range(2,integer):
        if (integer % i) == 0:
            print("Not a prime number.")
            break
        else:
            print("Prime number")
            break
            