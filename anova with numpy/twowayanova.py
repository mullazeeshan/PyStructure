import numpy as np
arr=np.asarray(([36,36,21,35],[28,29,31,32],[26,28,29,29]))
print('arr\n',arr)

mn=np.mean(arr)
print()

data=(arr-mn)
print('data\n',data)
rows=data.shape[0]
cols=data.shape[1]

datasquare=data**2
print('datasquare\n',datasquare)

cf=(np.sum(data)**2/(data.shape[0]*data.shape[1]))
#print('cf',cf)


CJ=np.sum(data,axis=0,dtype=int)
#print(CJ)
CJsquare=CJ**2
#print((CJsquare))
SSC=np.sum(CJsquare/3)-cf
#print(SSC)

RJ=np.sum(data,axis=1,dtype=int)
#print(RJ)
RJsquare=RJ**2
#print((RJsquare))
SSR=np.sum(RJsquare/4)-cf
#print(SSR)

Xij=np.sum(np.sum(datasquare,axis=0))
#print(Xij)
SST=Xij-cf
#print('SST',SST)

SSE=SST-SSC-SSR
#print('SSE',SSE)

MSE=SSE/((rows-1)*(cols-1))
#print(MSE)

MSR=SSR/(rows-1)
#print(MSR)
MSC=SSC/(cols-1)
#print(MSC)


FC=MSE/MSC
FR=MSE/MSR
print('FC=',FC,'FR=',FR)


