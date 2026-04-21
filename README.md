🚀 30 Days Python Challenge

Welcome to my 30 Days Python Challenge Repository.
This repo documents my daily journey of learning Python from basics to advanced concepts.

📅 Day 1 – Python Basics
🐍 What is Python?

Python is a high-level, interpreted programming language created by Guido van Rossum.
It is popular because it is simple, readable, and powerful.

📌 Why the name Python?

Python is named after the comedy show “Monty Python’s Flying Circus”, not the snake.

💡 Programming Language

A programming language is used to give instructions to a computer.

⚙️ Types of Languages
Compiler
Converts full code at once
Example: C, C++
Interpreter
Executes line by line
Example: Python, JavaScript
🧠 Concepts Learned
📦 Variables
name = "Ali"
age = 20
📊 Data Types
int → numbers
float → decimal
str → text
bool → True/False
⌨️ Input / Output
name = input("Enter your name: ")
print("Hello", name)
🔤 Strings
text = "Hello World"
✂️ Indexing & Slicing
text = "Python"
print(text[0:4])  # Pyth
📅 Day 2 – Operators
➕ Arithmetic

+ - * / % // **

🧾 Assignment

= += -= *= /= //= %= **=

⚖️ Comparison

== != > < >= <=

🔗 Logical
and
or
not
🔀 Conditionals
if condition:
    print("True")
else:
    print("False")
📅 Day 3 – For Loop
🔁 What is a Loop?

A loop is used to repeat code multiple times.

🔹 Types of Loops
for loop → when iterations are known
while loop → when condition is known
🔹 For Loop Example
for i in range(5):
    print("Hello")
🔹 range() Function
range(start, stop, step)
default start = 0
default step = 1

Example:

for i in range(1, 6):
    print(i)
🔹 Loop on Strings
text = "Python"

for char in text:
    print(char)
🔹 break, continue, else
break → stops loop
continue → skips one iteration
else → runs if loop completes normally
🔹 Practice Done
Print numbers
Tables
Factorial
Prime check
Palindrome check
Reverse string
📅 Day 4 – While Loop
🔁 While Loop

Used when number of iterations is unknown

i = 1
while i <= 5:
    print(i)
    i += 1
🔹 Features
Works on condition
Can use break, continue, else
🎮 Mini Project

👉 Built a Number Guessing Game using while loop

🔹 Practice Done
Reverse number
Palindrome number
Digit separation
📅 Day 5 – Functions & Lists
🔹 Functions
What is Function?

A function is a reusable block of code

def greet():
    print("Hello")

greet()
🔹 Parameters vs Arguments
Parameter → variable in function
Argument → value passed
def add(a, b):   # parameters
    return a + b

add(2, 3)        # arguments
📘 Lists
🔹 What is List?

A list stores multiple values.

🔹 Properties
Mutable
Ordered
Allows duplicates
Heterogeneous
🔹 Example
my_list = [1, 2, 3, "Ali"]
🔹 Access (Indexing)
print(my_list[0])
🔹 Common Methods
my_list.append(4)
my_list.remove(2)
my_list.pop()
my_list.sort()
🔹 Practice Done
Find max element
Check sorted list
Mean of list
Second largest number
📅 Day 6 – Tuple, Set, Dictionary
📘 Tuple
🔹 Properties
Immutable
Ordered
Allows duplicates
Heterogeneous
🔹 Example
t = (1, 2, 3)
🔹 Methods
t.count(2)
t.index(2)
📘 Set
🔹 Properties
Mutable
No duplicates
Unordered
Only hashable types allowed
🔹 Example
s = {1, 2, 3}
🔹 Methods
s.add(4)
s.remove(2)
s.discard(5)
s.pop()
🔹 Set Operations
A | B   # Union
A & B   # Intersection
A - B   # Difference
A ^ B   # Symmetric Difference
📘 Dictionary
🔹 What is Dictionary?

Stores data in key-value pairs

🔹 Properties
Mutable
Ordered (Python 3.7+)
Keys must be unique
🔹 Example
student = {
    "name": "Ali",
    "age": 20
}
🔹 Access
print(student["name"])
🔹 Methods
student.keys()
student.values()
student.items()
student.update({"age": 21})
🚀 Progress Summary

✅ Day 1–2 → Basics & Operators
✅ Day 3 → For Loop
✅ Day 4 → While Loop + Game
✅ Day 5 → Functions + Lists
✅ Day 6 → Tuple, Set, Dictionary

⭐ Final Note

I am learning Python step by step and building strong fundamentals.
More updates coming daily 🚀