# Encapsulation In Python

'''Three types of attributes '''
# Public we done

# 2: Prtected Attributes and methods

# 3: private attributes and methods

class demo:
    def __init__(self):
     self.name = 'Ahsan'
     self._age = 21
     self.__salary = 3000000
    
    def show(self):
            print('Inside the class')
            print('Public', self.name)
            print('protcted', self.age)
            print('private', self.__salary)
