# Conditional Statement In Python

'''class_time=int(input("Enter Your class time in between 9 to 5PM : "))

if class_time == 9:
    print('I will go uni at 9PM')
elif class_time > 9 and class_time < 12:
    print("I will gp uni at 11 Pm")
else:
    print("i will go uni after 10Pm Anytime")
'''

# 1. Accept two numbers and print the greatest between them.

'''num1 = int(input("Enter value of num1 here: "))
num2 = int(input("Enter value of numb2 here: "))

if num1 > num2:
    print("Num1 is greater'")
else:
    print("num2 is greatest.")
'''

# Q2. Accept the gender from the user as char and print the respective greeting message

'''gender = (input("Enter your gender between (M,F) :"))

if gender.upper() == 'M':
    print(f"Good Morning Sir")
elif gender.upper() == 'F':
    print(f"Good Morning Mam")'''

#  Accept a year and check if it a leap year or not (google to find out what is a leap year)

year = int(input("Enter a year here: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
