30 Days Python Challenge

This repository documents my daily progress while learning Python from basic to advanced concepts.

Day 1 – Python Basics
What is Python

Python is a high-level, interpreted programming language created by Guido van Rossum.
It is widely used due to its simplicity and readability.

Programming Language

A programming language is used to give instructions to a computer.

Compiler vs Interpreter

Compiler

Converts the entire program into machine code at once
Faster execution after compilation
Example: C, C++

Interpreter

Executes code line by line
Easier to debug
Example: Python, JavaScript
Variables

Variables are used to store data.

name = "Ali"
age = 20
Data Types
int → numbers
float → decimal values
str → text
bool → True / False
Input / Output
name = input("Enter your name: ")
print("Hello", name)
Strings
text = "Hello World"
Indexing and Slicing
text = "Python"
print(text[0:4])
Day 2 – Operators
Arithmetic Operators

+ - * / % // **

Assignment Operators

= += -= *= /= //= %= **=

Comparison Operators

== != > < >= <=

Logical Operators
and
or
not
Conditional Statements
if condition:
    print("True")
else:
    print("False")
Day 3 – For Loop
Concept

A loop is used to execute a block of code multiple times.

for loop → used when number of iterations is known
Example
for i in range(5):
    print("Hello")
range() Function
range(start, stop, step)
Default start = 0
Default step = 1
for i in range(1, 6):
    print(i)
Looping Through String
text = "Python"

for char in text:
    print(char)
Control Statements
break → stops loop
continue → skips iteration
else → runs if loop completes normally
Practice
Print numbers
Table generation
Factorial
Prime number check
Palindrome check
Day 4 – While Loop
Concept

Used when the number of iterations is not known.

i = 1
while i <= 5:
    print(i)
    i += 1
Key Points
Works on condition
Supports break, continue, else
Practice
Reverse number
Palindrome number
Digit extraction
Mini Project

Implemented a simple number guessing game using while loop.

Day 5 – Functions and Lists
Functions

Functions are reusable blocks of code.

def greet():
    print("Hello")

greet()
Parameters vs Arguments
def add(a, b):
    return a + b

add(2, 3)
Lists
Properties
Mutable
Ordered
Allows duplicates
Supports multiple data types
Example
my_list = [1, 2, 3, "Ali"]
Common Methods
my_list.append(4)
my_list.remove(2)
my_list.pop()
my_list.sort()
Practice
Maximum element
Second largest element
Mean of list
Sorted check
Day 6 – Tuple, Set, Dictionary
Tuple
Properties
Immutable
Ordered
Allows duplicates
Example
t = (1, 2, 3)
Methods
t.count(2)
t.index(2)
Set
Properties
Mutable
No duplicates
Unordered
Stores only hashable values
Example
s = {1, 2, 3}
Methods
s.add(4)
s.remove(2)
s.discard(5)
s.pop()
Operations
A | B   # Union
A & B   # Intersection
A - B   # Difference
A ^ B   # Symmetric Difference
Dictionary
Concept

Stores data in key-value pairs.

Example
student = {
    "name": "Ali",
    "age": 20
}
Access
student["name"]
Methods
student.keys()
student.values()
student.items()
student.update({"age": 21})
Progress Summary
Day 1–2: Basics and operators
Day 3: For loop
Day 4: While loop and mini project
Day 5: Functions and lists
Day 6: Tuple, set, dictionary
Note

This challenge is focused on building strong Python fundamentals step by step. More updates will be added as learning progresses.