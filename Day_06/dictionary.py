# Dictionay In Python

'''student_record = {1:70,2:80,3:85,4:90}

for i in student_record.values():
    print(i)'''

# Write a Python script to merge two Python dictionaries

'''a = {1:100,2:200,3:300,4:400}
b = {5:500,6:600,7:700}

for i in b:
    a[i] = b[i]

print(a)
'''
#Write a Python program to sum all the values in a dictionary

'''a = {1:100,2:200,3:300,4:400}

sum = 0
for i in a:
    sum += a[i]
    
print(sum)'''

# Count the frequency of each element

'''data = [1, 2, 2, 3, 1, 1, 4]

freq={}

for i in data:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)'''

# Write a Python program to combine two dictionary by adding values for common keys.

a = {1: 100, 2: 200, 3: 300}
b = {2: 50, 3: 70, 4: 400}

res ={}

for key in a:
    res[key] = a[key] # copy from a

# process b
for key in b:
    if key in res:
        res[key] += b[key]
    else:
        res[key] = b[key]

print(res)



