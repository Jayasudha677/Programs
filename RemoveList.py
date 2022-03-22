#program to print Remove empty list from list
test_list=[5,6,[],3,[],9]
print("the original list is:" +str(test_list))
res=[ele for ele in test_list if ele!=[]]
print("list after empty list removal:"+str(res))
# using filter()
test_list= [5,[],6,[],7,[]]
res=list(filter(None,test_list))
print("list after empty list removal:"+str(res))