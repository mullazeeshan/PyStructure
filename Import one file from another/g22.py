from sixth.f22 import minus
a=4
b=5
if(a<b):
   ''' a=a+b
    b=a-b
    a=a-b'''

   temp_a = a
   a = b
   b = temp_a + b
print("minus= ",minus(a,b))