#python program to find sum of elements
total=0
list1=[2,4,6,7]
for ele in range(0,len(list1)):
     total=total+list1[ele]
print("sum of all elements:",total)
# using while loop
total=0
ele=0
l1=[6,7,8,9,10]
while(ele<len(l1)):
     total=total+l1[ele]
     ele +=1
     print("sum of all elements in given l1:",total)
     
#using sum() method
l1=[1,2,3,5]
total=sum(l1)
print("sum of all elements :",total)
