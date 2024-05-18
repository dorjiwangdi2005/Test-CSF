#exercise 1, making multiplication table 

num = int (input("enter number to show the multiplication table : "))
num_2 = int(input("enter the multiplication limit number: "))

for i in range (1, num_2 + 1):
    print (f"{num} * {i} = {num * i}")

# exercise 2 making a triangle using nested loop
triangle = int (input ("enter the height of the triangle: "))

for i in range (1, triangle + 1) : 
        
    for j in range(i):
        print(f"*", end= " ")  
    print()  
    
# to make a pyramid shape of using * in output and nested loops
size = int(input("Enter the size: "))
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print()  

# exercise 3 To skip the numbers from the middle and to exit using continue and break 
for i in range(1, 10):

    if i == 3:
        continue  
    for j in range(1, 10):
        if j == 7:
            break 
        print(i, j)
        