#different ways to clear a list
#using clear() method
num=[1,2,3,4]
print('num before clear:',num)
num.clear()
print('num after clear:',num)

#using "*=0":
l1=[1,2,4]
print("l1 before deleting is "+str(l1))
l1 *=0
print("l1 after clearing using *=0:"+str(l1))
#using del method
n1=['h','e','l','l','o']
del n1[:]
print("n1 before deletiting is :" +str(n1))
print("n1 after deleting is :" +str(n1))