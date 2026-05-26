# Inheritace in python (Multilevel inhertiace)

# class factory:
#     def __init__(self,material,zips):
#         self.material = material
#         self.zips = zips

# class isb_factory(factory):
#     def __init__(self, material, zips, pocket):
#         super().__init__(material, zips)
#         self.pocket = pocket

# class lhr_factory(isb_factory):
#     def __init__(self, material, zips, pocket,color):
#         super().__init__(material, zips, pocket)
#         self.color = color

# object = lhr_factory()


# Syntax of inhertance

class Animal:
    name= 'lion'
    def show(self):
        pass

class Human(Animal):
    pass
# Now human class have access on all the parametrs and methods of animal class


'''Constrctor in inhertance '''

# class Factory:
#     def __init__(self, name):
#         self.name = name
    
# class Factory2(Factory):
#     def display(self,name):
#         print(f'my name is {self.name}')

# Super Function

'''class parent:
    def __init__(self,name):
        self.name = name

class child(parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    
    def show(self):
        print(f'My name is {self.name} and my age is {self.age}')

obj = child('lion', 23)
obj.show()

'''

# Multilevel inhertance

class Father:
    def __init__(self, coding, bussiness):
        self.coding = coding
        self.bussiness = bussiness
        
class Mother:
    def __init__(self, cooking):
        self.cooking = cooking

class child(Father, Mother):
    def __init__(self, coding, bussiness,cooking, study):
        super().__init__(coding, bussiness)
        self.study = study
        self.cooking = cooking
    
    def show(self):
        print(f'my father can do {self.coding} and {self.bussiness} and my mother can do {self.cooking} and i can do all')

obj = child('cpp', 'Software house','cooking', 'bs')
obj.show()