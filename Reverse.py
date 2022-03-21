# Reversing a list in python
def Reverse(list):
     return [ele for ele in reversed (list)]
list=[1,2,3,4,5]
print(Reverse(list))
# reversing a list using slicing technique
def Reverse(num):
     new_num=num[::-1]
     return new_num
num=[4,5,6,7,8]
print(Reverse(num))