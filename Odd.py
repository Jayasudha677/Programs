l1=[10,21,4,5,66,93]
for num in l1:
     if num%2!=0:
          print(num,end = " ")

# using while loop
l=[1,2,5,7,8,9]
i=0
while(i<len(l)):
     if l[i]%2!=0:
          print(l[i],end = " ")
     i+=1
     # using lamda expresssion
     l2=[10,21,4,45,66,93,11]
     odd_nos =l2(filter(lambda x: (x %2!=0),l2))
     print("odd numbers in list:",odd_nos)