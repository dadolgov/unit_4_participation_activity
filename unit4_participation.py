"""
Random number generator
Author: Dmitrii Dolgov
Date: 2/3/2026
Purpose: generate a list of 100 random numbers, 
print out the total number or elements, sum and average
"""
import random
#Creating a new list of random integers using list comprehension
random_numbers=[random.randint(1,10) for _ in range(100)]

#printing length, sum and average respectively
print(f"Total elements in the list: {len(random_numbers)}")
print(f"Sum of all elements is {sum(random_numbers)}")
print(f"Average of all values is {sum(random_numbers)/len(random_numbers):.2f}") #limited to 2 decimal spaces for better readability
