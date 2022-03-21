#smalest element in a list
list1=[1,2,3,4]
list1.sort()
print("smallest element is:",*list1[:1])
#using min() method
l1=[2,6,7,8,9]
print("smallest element is :",min(l1))
# using min list
l1=[]
num=int(input("enter number of elements in list:"))
for i in range(1,num+1):
     ele=int(input("enter element:"))
     l1.append(ele)
print("smallest element :",min(l1))