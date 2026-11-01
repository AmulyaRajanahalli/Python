s=[]
exp=input("Enter expression:")

for i in exp:
    if i in "({[":
        s.append(i)
    elif i in ")}]":
        if not s or "({[".index(s.pop()) !=")}]".index(i):
            print("Not Balanced")
            break
else:
    print("Balanced" if not s else "Not Balanced")
        
