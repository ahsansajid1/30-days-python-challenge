# Map function in python

numbers = [1, 2, 3, 4, 5]
def square(x):
    return x **2
num_sq = map(square, numbers)
print(list(num_sq))

number_squared= map(lambda x : x ** 2 , numbers)
print(list(number_squared))