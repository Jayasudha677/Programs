#print positive numbers in a list
l=[11,4,5,6,8,7,-45,-67]
for num in l:
     if num>=0:
         print(num,end=" ")
         
         
# using while loop
list1=[4,6,7,8,9]
num=0
while(num<len(list1)):
     if list1[num] >=0:
         print(list1[num],end=" ")
         num +=1

list1=[-10,-21,7,8]
pos_nos=[num for num in list1 if num>=0]
print("positive numbers in the list:" ,*pos_nos)
