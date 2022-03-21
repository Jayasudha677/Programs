#sort list ascending order
l1=[1,2,4,5]
l1.sort()
print("largest element is:",l1[-1])
#using max() method
l1=[2,4,6,7]
print("largest is:",max(l1))
#input provide by user
l1=[]
num=int(input("enter number of elements in list:"))
for i in range(1,num+1):
     ele=int(input("enter elements:"))
     l1.append(ele)
print("largest element is:",max(l1))
#without using built in function
def myMax(list1):
     max=list1[0]
     for x in  list1:
         if x>max:
             max=x
     return max
     lisgt1=[1,3,5,7]
     print("largest element is:",myMax(list1))
