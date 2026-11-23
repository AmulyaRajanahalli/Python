a=sorted(list(map(int,input("Enter sorted numbers:").split())))
x=int(input("Enter element:"))

l,h=0,len(a)-1

while l<=h:
    m=(l+h)//2
    if a[m]==x:
        print("Found at position",m+1)
        break
    elif x<a[m]:
        h=m-1
    else:
        l=m+1
else:
    print("Not Found")
