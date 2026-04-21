📘 Tuple Basics
🔹 What is a Tuple?

A tuple is a collection of elements in Python.

Key Properties:
Immutable → You cannot change values after creation
Ordered → Elements have a fixed position (indexing allowed)
Duplicates Allowed → Same values can appear multiple times
Heterogeneous → Can store different data types (int, string, etc.)
🔹 Important Points
Once a tuple is created, it cannot be modified
You can access elements using index values
Works similar to a list, but without modification
🔹 Tuple Traversing

You can loop through a tuple just like a list:

my_tuple = (1, 2, 3)

for i in my_tuple:
    print(i)
🔹 Tuple Methods

Tuples have only 2 built-in methods:

count() → counts occurrences of an element
t = (1, 2, 2, 3)
print(t.count(2))   # Output: 2
index() → finds position of an element
print(t.index(2))   # Output: 1
📘 Set Basics
🔹 What is a Set?

A set is a collection of unique elements.

🔹 Key Properties:
Mutable → You can change values
No Duplicates → All elements must be unique
Unordered → No indexing (no fixed position)
Heterogeneous (Limited) → Supports int, string, tuple (only immutable types)
🔹 Important Points
You cannot access elements using index
Elements may appear in random order
Only hashable (immutable) data types are allowed
🔹 How Sets Work (Hashing Concept)
Each value is converted into a hash value using hash()
This hash is used to store data in memory
Because of hashing → order is not maintained
Mutable types like list/dictionary are not allowed
🔹 Set Traversing

Since sets are unordered, you can only loop:

my_set = {1, 2, 3}

for i in my_set:
    print(i)
🔹 Basic Set Methods
➤ Adding Elements
s = {1, 2}
s.add(3)
➤ Removing Elements
s.remove(2)     # Error if not found
s.discard(5)    # No error
s.pop()         # Removes random element
➤ Clearing Set
s.clear()
🔹 Set Operations (Very Important)
1. Union (Combine both sets)
A = {1, 2}
B = {2, 3}

print(A.union(B))   # {1,2,3}

Shortcut:

A | B
2. Intersection (Common elements)
print(A.intersection(B))   # {2}

Shortcut:

A & B
3. Difference (Elements in A but not in B)
print(A.difference(B))   # {1}

Shortcut:

A - B
4. Symmetric Difference (Not common)
print(A.symmetric_difference(B))   # {1,3}

Shortcut:

A ^ B
🔹 Other Useful Methods
s1.issubset(s2)      # True if s1 inside s2
s1.issuperset(s2)    # True if s1 contains s2
s1.copy()            # Copy set
🔹 Final Note
Tuple → fixed, safe, used when data should not change
Set → fast, unique values, useful for operations like union/intersection

Sets are not used everywhere, but very useful in:

Removing duplicates
Fast searching
Mathematical operations