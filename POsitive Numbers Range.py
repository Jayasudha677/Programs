#program to print positive numbers in a range
start,  end=-4,19
for num in range(start,end+1):
     if num>=0:
         print(num,end=" ")

    # taking range limit form user input
start=int(input("enter the start of range: "))
end= int(input("Enter the end of range:"))
for num in range (start,end+1):
     if num >=0:
         print(num,end=" ")
