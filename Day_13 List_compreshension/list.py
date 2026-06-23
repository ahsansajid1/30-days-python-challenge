# List comprehension in python
# Fist way
# name = 'Ahsan'
# lst = list(name)
# print(type(lst))
# print(lst)
#Second way
# lst = [i for i in name]
# print(lst)

#generate list of numbers
# num = 20
# empty = []
# for i in range(1,num):
#     empty.append(i)

# print(empty)

''' List of 1 - 2- '''
# number = [i for i in range(1,21)]
# print(number)

'''Sq of num from 1 10'''

# num = [x * x for x in range(1,11)]
# print(num)

''' Cube of num'''

# nums  = [x**3 for x in range(1,10)]
# print(nums)

''' even from 1 50'''
# even_num = [num for num in range(1,50) if num %2 == 0]
# print(even_num)

''' uppercase '''

# names = ["ali", "sara", "ahmed"]

# upper = [name.upper() for name in names]
# print(upper)

''' add 10'''
# nums = [5, 10, 15, 20]

# new = [num + 10 for num in nums]
# print(new)

''' get onky postive '''
# nums = [-5, 10, -2, 20, 0]

# pos = [nums for num in nums if num > 0]
# print(pos)


prices = [500, 1500, 2000, 800, 3000]

new_price = [price for price in prices if price > 1000]
print(new_price)

# From email list, keep only Gmail addresses.

# emails = [
#     "ali@gmail.com",
#     "test@yahoo.com",
#     "sara@gmail.com"
# ]

# new_email = [mail for mail in emails if mail.endswith("@gmail.com")]

# print(new_email)

# files = [
#     "cv.pdf",
#     "image.png",
#     "report.pdf"
# ]

# new_file  = [file for file in files if file.endswith('.pdf')]
# print(new_file)