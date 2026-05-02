
from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items} ")


def createfile():
    try:
        readfileandfolder()
        name = input('please tell your file name :- ')
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data =input('tell what you want to write in this file: ')
                fs.write(data)
        
            print('FILE CREATED SUCCESFULLY')
        else:
            print('This File already exist:- ')

    except Exception as err:
        print(f"An error occured as an {err}")

def readfile():
    try:
        name = input('Which file do you want to read:- ')
        p= Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print('This file read succesfully: ')
        else:
            print('This file noe exist:')

    except Exception as err:
        print(f'An error  occur as an {err}')

def updatefile():
    try:
        readfileandfolder()
        name = input('tell which file do you want to update:- ')
        p= Path(name)
        if p.exists() and p.is_file():
            print('Press 1 for changing the name of your file :- ')
            print('Press 2 for overwriting the data of your file :- ')
            print('Press 3 for appending some data into your file :- ')

            res =int(input('tell your responce:- '))
            new_name = input("Enter new file name: ")
            p2 = Path(new_name)
            p.rename(p2)
            print("File renamed successfully")

            if res == 2:
                with open(p, 'w')as fs:
                    data=input('tell what you want to write this as a overwriting: -: ')
                    fs.write(data)
            if res == 3:
                with open(p, 'a') as fs:
                    data=input('tell what you want to appned in file -: ')
                    fs.write(" " +data)
    except Exception as err:
        print(f"An error occured as {err}")

def deletefile():
    try:

        readfileandfolder()
        name= input('tell the name of file which you want to delete: ')
        p= Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print('File deleted succesfully')
        else:
            print('No such file exist: ')
    
    except Exception as err:
        print(f'An error occur as {err}')


print("Press 1 for creating a file :- ")
print("Press 2 for reading a file :- ")
print("Press 3 for Updating a file :- ")
print("Press 4 for deletion a file :- ")

check = int(input('Enter what you want to do :- '))
if check == 1:
    createfile()
if check == 2:
    readfile()

if check == 3:
    updatefile()

if check ==4:
    deletefile()
