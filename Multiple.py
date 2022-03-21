#multiply all numbers in list
def multiplyList(myList):
     result=1
     for x in myList:
          result=result *x
     return result
l=[1,2,3]
l1=[4,5,6]
print(multiplyList(l))
print(multiplyList(l1))
# using numpy.prod
import numpy
l1=[1,2,3]
l2=[5,7,8]
result1=numpy.proud(l1)
result2=numpy.proud(l2)
print(result1)
print(result2)