'''x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)

print(x is y)'''


'''
x = ["apple", "banana"]
print("pineapple" not in x)


name=input("enter name:")


no=int(input("enter no:"))

fees=float(input("enter fees:"))
'''

'''
r=int(input("r:"))
print(r)
area= 3.14*r**2

print("area of circle:",area)



x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))

a=((x+y+z)/2)
print('avg of three:', a)


print("Name:",x,"\nNo:",y,"\nFees:",z)

'''


'''
d = {1:'Jimmy', 2:'Alex', 3:'john', 4:'mike'};
print("1st name is "+d[1]);
print("2nd name is "+ d[4]);
print (d);
print (d.keys());
print (d.values());  

'''

'''
num=[1,2,3,4,5]
print(num)

search=int(input("enter no:"))


if search in num:
    print("in list")
else:
    print("not in list")

print(num.index(search))
'''
    



n=int(input("enter n:"))
print(n)
print("#",end="      \n")
if n%2==0:
    print(n, "is even")
elif n%2!=0:
    print(n, "is odd")
elif n<5:
    print("less than 5")
print(id(n))


