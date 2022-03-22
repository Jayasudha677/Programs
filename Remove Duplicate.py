#to print remove duplicate from a list
test_list=[1,3,5,6,3,5,6,1]
print("the original list is:" + str(test_list))
res=[]
for i in test_list:
     if i not in res:
           res.append(i)
print("the list after removing duplicates:"+str(res))
#using list comprenhension
test_list=[1,3,5,6,3,5,6,1]
print("the original list is :",+str(test_list))
res=[]
[res.append(x) for x in test_list if x not in res]
print("the list after removing duplicates:"+str(res))