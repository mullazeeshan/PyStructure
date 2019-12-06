'''try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a/b;
    print("a/b = ",c)
except Exception:
    print("can't divide by zero")
else:
    print("Hi I am else block")  '''




'''
try:

    fileptr = open("file.txt","r")
except IOError:
    print("File not found")
else:
    print("The file opened successfully")
    fileptr.close() '''


'''
try:
    a=10/0;
except (ArithmeticError,IOError,SyntaxError):
    print("Arithmetic Exception")
else:
    print("Successfully Done")
'''

'''
try:
    fileptr = open("file.txt","r")
    try:
        fileptr.write("Hi I am good")
    finally:
        fileptr.close()
        print("file closed")
except:
    print("Error")
'''

'''
try:
    age = int(input("Enter the age: "))
    if age<18:
        raise ValueError;
    else:
        print("the age is valid")
except ValueError:
    print("The age is not valid")
'''


'''
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if b is 0:
        raise ArithmeticError;
    else:
        print("a/b = ",a/b)
except ArithmeticError:
        print("The value of b can't be 0")
'''

'''

class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print(self.ram,"",self.cpu)
com1 = computer("i5",16)
com2 = computer("amd",8)
com1.config()
com2.config()
'''

def __init__(self,age):
    try:

        if age<18:
            raise ValueError
        else:
            print("valid age")
    except ValueError:
        print("invalid age")

