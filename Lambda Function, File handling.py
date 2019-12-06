def starprg(*b):
    print("type of passe args", type(b))
    print("psse args")

    for n in b:
        print(b)
print("fff","hhh","yyy")


def op():
    message="helloooooooooo"
    print(message)
op()


def calculate(*args):
    sum=0
    for arg in args:
        sum=sum+arg
    print(sum)

sum=0
calculate(10,20,30)
print("Value of sum outside the function:",sum)







'''
fileptr = open("files\\file.txt","r");
content = fileptr.readlines(3)
print(type(content))
print(content)
fileptr.close()
'''

'''
fh = open("files\\file.txt","r")
h=fh.readline(3)
print(h)
fh.close()
'''

'''
file = open("files\\file.txt","r")
for line in file:
    print(line)
file.close()
'''


fileptr = open("files\\file.txt","x");
fileptr.write("Python is the modern day language. It makes things so simple.")
#g=fh.writelines(fileptr)
#print(g)
fileptr.close();



'''fi=open("files\\file.txt")
g=fi.readlines()
print(g[3:5])
fi.close()'''

