a=list(map(int,input("Enter numbers:").split()))
x=int(input("Enter element to search:"))

if x in a:
    print("Found at position",a.index(x)+1)
else:
    print("Not Found")
