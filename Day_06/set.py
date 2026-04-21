# SET IN PYTHON

my_set = {1,2,3,4,5,6,7,8,9}

my_set.add(0)

print(my_set)

#Loop on set work 

for i in my_set:
    print(i)

#Check hash value here of random numbers

print(hash('2'))
print(hash('helo'))

# Methods Of set

s= {1,2,3,4,5,66,77,88,34}

s.add(22)
s.remove(34)
s.discard(1)
pop_value= s.pop()

print(s)

# SPECIAL OPEARTAION IN SETS

A = {1,2,3,4,5,6,7,8}
B = {6,7,8,9,10,11,12,12}

print(A|B) #Union here
print(A & B) # Interection
print(A - B) # A Diff B
print(A ^ B)  # symmetruec duff

