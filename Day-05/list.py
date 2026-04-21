# List in python

'''l = [12,14,11,77,88,99,"ali",'ahmed']
print(l[5]) #list indexing
print(l[:8])  #list slicing
'''
#Modify value

'''list = [22,55,44,2,1,00,77]

list[3] = "Modify"

print(list)
'''
#list traversing

'''list = [22,55,44,2,1,00,77]

for i in range(len(list)):
    print(list[i]) 
'''

# Print positive and negative elements of an List

'''l= [1,-22,11,-21,33,12]

print("postive number are")
for i in l:    
    if i >= 0:
        print(i)

print("Negative numbers are")
for i in l:
    if i < 0:
        print (i)'''

# Mean of List elements

'''list= [22,45,66,121,23,1]

sum = 0

for i in list:
    sum = sum + i

print(f"Mean of list = {sum / len(list)}")'''

#Find the greatest element and print its index too

l= [22,45,66,121,23,1]

largest = l[0]

index = 0

for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i

print(f"Largest number are {largest} at index {index}")






