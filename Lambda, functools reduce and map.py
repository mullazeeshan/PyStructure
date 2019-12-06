

'''
x=lambda a:a+10
y=lambda a:a-10
z=lambda a:a*10
print("sum ",x(20))
print("diff ",y(20))
print("mul ",z(20))


l=lambda c,r,g,h:c+r+g+h
print("sum1",l(10,10,10,10))


def table(n):
    return lambda a:a*n
n=9    #int(input("enter the number: "))
b=table(n)  #function called over here
for i in range(1,11):
    print(n, "*", i,"=", b(i))
'''

from functools import reduce
def add_all(a,b):
    return a+b
nums=[2,5,6,3,7,8,9,1]
evens=list(filter(lambda n:n%2==0,nums))
doubles=list(map(lambda n:n*2,evens))
sum=reduce(lambda a,b:a+b,doubles)
print(evens)
print(doubles)
print(sum)

sums=reduce(add_all,doubles)
print(sums)





