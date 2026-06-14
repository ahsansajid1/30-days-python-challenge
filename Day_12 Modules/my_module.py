def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname

def addition(a,b):

    sum = a + b
    return sum


def is_even(num):

    for i in range(num):
        if num % 2 == 0:
            return 'even Number'
        else:
            return 'Not even'
        

def weight_of_obj(mass,gravity):
    weight= str(mass * gravity)+ 'N'
    return weight

