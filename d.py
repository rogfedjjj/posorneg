x1,x2=input().split()
a=0
if len(x1)!=len(x2):
    print("no")
else:
    for i in range(len(x1)):
        if x1[i]!=x2[i]:
            a+=1
if a==1:
    print("yes")
else:
    print("no")
