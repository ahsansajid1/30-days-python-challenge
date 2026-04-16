#Loop Concept In Python

'''n= int(input("Enter a number here: "))

for i in range(n):
    print("Hello")
'''
#Table using loop

'''no = int(input("Enter a number you want table:"))

for i in range(no,(no*10)+1,no):
    print(i)
'''
#Reverse for loop. Print n to 1

'''num= int(input("Enter a no : "))

for i in range(num,0,-1):
    print(i)
'''

#Sum up to n terms

#n= int(input("Enter a no : "))
'''sum = 0

for i in range(1,n+1):
    sum +=i

print(f"sum = {sum}")'''

# Factorial of a number

'''n = int(input("Enter a no : "))
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)
'''

#Print the sum of all even & odd numbers in a range separately
'''n = int(input("Enter a no : "))
even_sum= 0
odd_sum= 0

for i in range(n+1):
    if i%2==0:
        even_sum +=i
    else:
        odd_sum +=i
print(f"Even sum= {even_sum}")
print(f"Odd sum= {odd_sum}")'''


#Print all the factors of a number
'''n = int(input("Enter a no : "))

for i in range(1,n+1):
    if n%i == 0:
        print(i)

'''
# Perfect number
'''n = int(input("Enter a no : "))
sum= 0
for i in range(1,n):
    if n % i == 0:
        sum +=i

if sum ==n:
    print(f'{n} No is perfet number')
else:
    print(f"{n} no is not perfect number")
'''
#Check wether the number is prime or not
'''Only have two factore 1 and own'''

'''no = int(input("Enter a no : "))
is_prime = 0

for i in range(1,no+1):
    if no % i == 0:
        is_prime += 1

if is_prime == 2:
    print(f"{no} No is prime number")
else:
    print(f"{no} is not prime number")
    '''

# Reverse a string without using in build functions.

'''name= " password "
b = ""
for i in range(len(name)-1,-1,-1):
    b = b + name[i]

print(b)'''

a= "dAGG52146@@$$%"

char=0
digi=0
special=0
for i in a:
    if i.isdigit():
      digi+=1
    elif i.isalpha():
      char+=1
    else:
       special+=1
    
print(f"digit are {digi}\n charcter are {char}\n sepcial num are {special}")

   



