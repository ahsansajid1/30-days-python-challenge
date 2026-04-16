# While Loop in python

#Separate each digit of a number and print it on the new line

'''num = 5689

while num > 0:
    print(num % 10)
    num= num // 10'''

#Accept a number and print its reverse
# Accept a number and check if it is a pallindromic number

num= int(input("Enter a number: "))
orignal_num= num

rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10

print(rev)

if rev == orignal_num:
    print(f"{orignal_num} is palindrome. ")
else:
    print(f"{orignal_num}o is not a palindrome number")


