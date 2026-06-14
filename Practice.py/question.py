''' Write a python to print Hello world'''
# print('Hello World')

''' Write a python program to do arthematic operations'''
# num1 = int(input('Enter the value of num1: '))
# num2 = int(input('Enter the value of num2 :'))

# # Addition
# print(f'Addition of num1 and num2 is equal to = {num1 + num2} ')
# print(f'Multiplication of Num1 and Num2 are = {num1 * num2}')
# print(f'Division of Num1 and Num2 are = {num1 / num2}')
# print(f'Subtraction Num1 and Num2 are = {num1 - num2}')

''' Write a Python program to swap two variables '''

# a = int(input('Enter the value of a : '))
# b = int(input('Enter the value of b :'))
# print(f'value of a = {a} and b = {b} are before swapping ')
# # Swapping variables

# temp  = a
# a = b
# b = temp

# print(f'value of a = {a} and b = {b} are after swapping')

''' Write a Python program to generate a random number.  '''

# import random
# print(f'Random numbers from 0 to 100 are = {random.randint(0,100)}')

''' Write a Python program to display calendar '''

# import calendar

# year = int(input('Enter the year : '))
# month = 1
# print(f'Calender For {year} year')
# for i in range(1,13):
#     cal = calendar.month(year,month)
#     month += 1
#     print(cal)

''' Soltion of Quadratic EQ ax^2 + bx + c
-b + (b**2 - 4ac) / ^1/2 (2a)'''

# import math

# a = float(input("Enter coefficient a: ")) 
# b = float(input("Enter coefficient b: ")) 
# c = float(input("Enter coefficient c: ")) 

# # Calculate the discriminant 
# discriminant = b**2 - 4*a*c 

# # Check if the discriminant is positive, negative, or zero 
# if discriminant > 0: 
# # Two real and distinct roots 
#     root1 = (-b + math.sqrt(discriminant)) / (2*a) 
#     root2 = (-b - math.sqrt(discriminant)) / (2*a) 
#     print(f"Root 1: {root1}")
#     print(f"Root 2: {root2}") 

# elif discriminant == 0: 
# # One real root (repeated) 
#     root = -b / (2*a) 
#     print(f"Root: {root}") 

# else: 
# # Complex roots 
#     real_part = - b / (2*a) 
#     imaginary_part = math.sqrt(abs(discriminant)) / (2*a) 
#     print(f"Root 1: {real_part} + {imaginary_part}i") 
#     print(f"Root 2: {real_part} - {imaginary_part}i") 

''' Prime Number checker'''

# num = int(input('Enter your number :'))

# flag = False

# if num == 1:
#     print(f'{num} is not prime number. ')

# elif num > 1:
#     for i in range(2, num):
#         if (num %  i) == 0:
#             flag = True
#             break

# if flag:
#     print(f'{num} is not a prime number. ')
# else:
#     print(f'{num} is a prime number. ')

''' Prime number between 1 to 10  '''

# lower = 1
# upper = 10

# for num in range(lower, upper+1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)

''' Write a Python Program to Find the Factorial of a Number. '''

# num = int(input('Enter your number :'))

# fact = 1

# for i in range(1,num+1):
#     fact = fact * i

# print(f'Fcatorial of a {num} is = {fact}')

''' Write a Python Program to Display the multiplication Table.  '''

# num = int(input('Enter your number :'))

# for i in range(1,11):
#     print(f'{num} * {i} = {(num) * (i)}')

'''Fabanochi series (add of previous 2 numbers)'''

# n_term = int(input('Enter how mnay terms : '))

# n1, n2 = 0 , 1
# count = 0

# if n_term <= 0:
#     print('please enter a positive number.')
# elif n_term == 1:
#     print(n1)
# else:
#     print('Fibonacci Series')
#     while count < n_term:
#         print(n1)
#         nth= n1 + n2
#         # update values
#         n1 = n2
#         n2 = nth
#         count += 1

'''Q: 12 Check armstong number (A no where its digts power sum is equal to no again in armstong no)'''

# num = int(input('Enter the number you want to check : '))
# #  check length of num
# num_str = str(num)
# num_digits= len(num_str)

# # intialize varaible
# temp_num = num
# sum_powers = 0

# while temp_num > 0:
#     digit = temp_num % 10
#     sum_powers += digit ** num_digits
#     temp_num //= 10

# # check armstong or not
# if sum_powers == num:
#     print(f'{num} is an Armstrong Number ')
# else:
#     print(f'{num} is not an Armstrong Number')

'''Q: 13 Chk armstong interval '''

# lower = int(input('Enter a lower number interval : '))
# higher = int(input('Enter a high interval : '))

# for num in range(lower, higher+1):
#     order = len(str(num))
#     sum = 0
#     temp_num = num

#     while temp_num > 0:
#         digit = temp_num % 10
#         sum += digit ** order
#         temp_num //= 10

# #  Chk armstrong number
#     if num == sum:
#         print(num)
    
''' Q: 14 Write a Python Program to Find the Sum of Natural Numbers. '''

# limit = int(input('Enter the limit of number: '))

# sum = 0

# for i in range(1,limit+1):
#     sum += i

# print(f'The sum of natural number upto {limit} is = {sum}')

''' Q:15 Convert decimal into binary. octal , hexa '''

# dec_num= int(input('Enter a decimal number : '))

# print(f'The decimal value of {dec_num} are :')

# print(f'{bin(dec_num)} Binary number ')
# print(f'{oct(dec_num)} Octal number ')
# print(f'{hex(dec_num)} HexaDeciimal number ')


''' Q:16 Write a Python Program To Find ASCII value of a character. '''

# chr = input(str('Enter a single character here: '))

# print(f'The ASCII Value of {chr} is = {ord(chr)} ')

'''Q:17  '''