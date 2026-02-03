"""
Random number generator
Author: Dmitrii Dolgov
Date: 2/3/2026
Purpose: generate 100 random numbers, print out the total number or elements, sum and average
"""
import random

random_numbers=[random.randint(1,10) for _ in range(100)]
print(random_numbers)


#participation
#use list comprehension to create a list of 100 random numbers 1 to 10
#list_example= 10,9,8,1,10,4 etc
#print out the total elements in the list (how many elements are there, probably len())
#print out the sum
#print out the average