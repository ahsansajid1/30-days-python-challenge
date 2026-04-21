# Function In Python

'''def hello():
    print("Hello world ")

hello()'''

#Addition using function:

'''def sum(a,b):
    print(f"Sum is {a + b}")

sum(12,22)
'''
'''There are three types of Arguments
1: posional aurguments 
2: Default arguments 
3: keyword arguments 
'''

def palindrome(st):
    rev= " "
    for i in range(len(st),-1,-1):
        rev += i

    if rev == st:
        print("Palindrome")
    else:
        print("Not palindrome")

palindrome("Naman")
    