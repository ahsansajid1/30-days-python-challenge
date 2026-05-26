#OOP IN PYTHON
'''For writing a program we use three approcahes in python .'''
#Imperative approach
'''a = 12
b = 20
print(a + b)

#Functional Approach
def addition(a , b):
    return a + b
print(addition(12,22))'''

#Object oriented approach
#What is Class

'''class Factory:
    a = 12

    def show(self):
        print('hello how are you')
    
    print('This class in intiliazed: -')


print(Factory().show())'''

#Obj in class
'''
class Animal:
    type = 'dOG'

    def action():
        print('bark')

obj =Animal()
print(obj.type,)
'''

# #Constrcuter In OOPs
# class Factory:
#     def __init__(self,material,zip,pocket):
#         self.material = material
#         self.zip = zip
#         self.pocket = pocket

#     def show(self):
#         print(f'Your objectes are {self.material},{self.zip},{self.pocket}')

# # intillize an obj
# reebok = Factory('leather',3,2)

# # accesing data 
# reebok.show()
# print(reebok.zip)

'''Types of Attributes '''
# Class attributes

class Animal:
    name = 'dog'# class attribute

    def __init__(self,color,height):
        self.color = color # instance attributes
        self.height = height

obj = Animal('black', 3.6)

print(obj.color)


