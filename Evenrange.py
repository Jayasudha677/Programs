# program to even numbers in a range
start,  end = 4,19
for num in range(start, end+1):
      if num % 2== 0:
           print(num,end =" ")
        
# taking range  from user
start = int(input("enter the start of range:"))
end = int(input("enter the end of range:"))
for num in range(start, end+1):
     if num%2==0:
         print(num,end= " ")