''' Importing an module'''
# import my_module
# print(my_module.generate_full_name('Ahsan', 'Sajid'))

''' Importing multiple function from module '''

# from my_module import generate_full_name, addition, weight_of_obj, is_even
# print(generate_full_name('Semi', 'Khan'))

# print(addition(12,12))

# print(weight_of_obj(50, 9.8))

# print(is_even(13))

''' Import Built In Module '''
# import os

# print(os.mkdir('New'))
# # Remove current directory
# os.rmdir('New')
# # Get current directory
# print(os.getcwd())

''' MATH MODULE '''

# import math

# print(math.sqrt(2))
# print(math.pi)
# print(math.floor(9.123))

''' Statics Module'''
# from statistics import * # importing all the statistics modules
# ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
# print(mean(ages))       # ~22.9
# print(median(ages))     # 23
# print(mode(ages))       # 20
# print(stdev(ages))      # ~2.3

# Multtiple Function import 

# from math import pi, sqrt, pow, floor, ceil, log10
# print(pi)                 # 3.141592653589793
# print(sqrt(2))            # 1.4142135623730951
# print(pow(2, 3))          # 8.0
# print(floor(9.81))        # 9
# print(ceil(9.81))         # 10
# print(math.log10(100))    # 2

''' String Module'''

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

'''Random Module'''
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive