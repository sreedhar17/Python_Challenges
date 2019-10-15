import numpy as np
import itertools
arr=np.array([1,3,2,4,5])
print(arr)
print(arr.argsort())
print(arr.argsort()[:3])
print(arr.argsort()[-3:][::-1])

try:
    print(2//1)
except:
    print("Error")
else:
    print("Inside else")

l1=(1,2,3)
l2=[4,5,6]
l=itertools.chain(l1,l2)
print(list(l))