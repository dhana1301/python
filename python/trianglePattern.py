n = int(input("Enter the number")) 

for i in range(1,n+1):
    print("* " * i) 

for i in range(1,n+1):
    print((str(i) + " ") * i) 

for i in range (1,n+1):
    for j in range(1,i+1):
        print(j,end=" ") 
    print()