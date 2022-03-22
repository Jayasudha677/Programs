#program to print negative numbers  in a list
list1=[-11,21,-8,-5,7,8]
for num in list1:
     if num<0:
         print(num,end=" ")
          

          # using while loop
l1=[-10,21,-4,7,9,-9]
num=0
while(num<len(l1)):
     if l1[num]<0:
          print(l1[num],end = " ")
          num ++1
          # using list comprehension
l=[-10,8,9,-5]
neg_nos=[num for num in l if num<0]
print("negative numbers in the list:",*neg_nos)