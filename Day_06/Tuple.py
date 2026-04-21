# Tuple in Python

t = (2,5 ,7 ,8 ,5 ,9, "hello", "print")

# Tuple tranversing 1: Direct
for i in t:
    print(i)

# using len function and have acces to index as well
for i in range(len(t)):
    print(t[i])

# Tuple Methods:

a = t.index('hello')
b = t.count(5)
print(a,b)