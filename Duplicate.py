#progrm to print duplicate from a  list of integer

# using counter() function
from collections import Counter
l1=[1,2,1,2,3,4,5,1,2,5,6,7,8,9,9]
d=Counter(l1)
print(d)
new_list=list([item for item in d if d[item]>1])
print(new_list)
#using count()
list=[1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
new=[]
for a in list:
    n=list.count(a)
    if n>1:
        if new.count(a)==0:
            new.append(a)
            print(new)