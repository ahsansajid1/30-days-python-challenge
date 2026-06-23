# Closure of a function
def add():
    ten= 10
    def sum(num):
        return num + ten

    return sum  
closure = add()
print(closure(4))

''' Discount function'''
def discount_creator(discount):
    def apply(price):
        return price - (price * discount)
    return apply

student_discount = discount_creator(0.2)

print(student_discount(1000))  # 800