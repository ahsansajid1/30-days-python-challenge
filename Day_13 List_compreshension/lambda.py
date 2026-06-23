'''Square of a number'''

square = lambda x: x * x
print(square(2))

''' Discount calculator'''

dic = lambda price : price * 0.9

print(dic(1000))

'''Even '''

even_num = lambda num : num % 2 == 0
print(even_num(4))

nums = [1, 2, 3, 4, 5, 6]

even_nums = list(filter(lambda x: x % 2 == 0, nums))

print(even_nums)