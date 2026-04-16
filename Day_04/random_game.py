#Create a random number guessing game with python.

import random
num = random.randint(1,100)



tries = 0 

while True:
    guess = int(input("Enter a number b/w (1 to 100): "))

    if num == guess:
        tries +=1
        print(f"You can guess a right number in {tries} tries: ")
        break
        
    elif num > guess:
        print("go a litt bit higher: ")
        tries+=1
            
    elif num < guess:
        print("go a little bit lower: ")
        tries+=1

    else:
        print("Try again =>")
        tries+=1


