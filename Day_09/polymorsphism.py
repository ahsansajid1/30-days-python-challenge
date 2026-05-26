# Polymorphism in Python
''' Many Forms but work diff on diff forms
There are two methods '''

#1:  Method Overriding

# class Animal:
#     def show(self):
#         print('hello i am showing ')

# class Human(Animal):
#     def show(self):
#         print('i am showing too')

# obj = Human()
# obj.show()


# Duck Method 

class Animal:
    def show(self):
        print('hi ii i ii ')

class Human:
    def show(self):
        print('hello i am showing ')

obj1= Animal()
obj2 = Human()

obj1.show()
obj2.show()