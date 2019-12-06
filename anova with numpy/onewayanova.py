import numpy as np
arr=np.asarray(([9,7,4],[8,6,3],[7,6,2],[8,7,3],[8,8,4],[9,7,3],[8,6,2]))
print(arr)

a=arr.shape[1]
print(a)
n=arr.shape[0]
print(n)
N=(arr.shape[0]*arr.shape[1])
print(N)

dfbetween= a-1
dfwithin= N-a
dftotal= N-1
print("dfbetween=",dfbetween ,", dfwithin=",dfwithin ,", dftotal=",dftotal)

T= np.sum(arr)**2
print(T)
col1=np.sum(arr,axis=0)
print(col1)
print("keepdimension",np.sum(arr,axis=0,keepdims=True))
col1square=col1**2
print(col1square)
sumcol1square=np.sum(col1square)
print(sumcol1square)

SSbetween=(sumcol1square/n)-(T/N)
print(SSbetween)


sumofYsquare=(np.sum(np.square(arr)))
print(sumofYsquare)
SSwithin=sumofYsquare-(sumcol1square/n)
print(SSwithin)


SStotal=sumofYsquare-(T/N)
print(SStotal)

MSbetween=SSbetween/dfbetween
MSwithin=SSwithin/dfwithin
print(MSbetween,MSwithin)

F=MSbetween/MSwithin
print(F)


