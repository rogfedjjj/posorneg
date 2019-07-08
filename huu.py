x,c=input().split(" ")
x =int(x)
c =int(c)
aa=input().split(" ")
bb=input().split(" ")
flag=0
flag1=1
for i in range(0,c):
    for j in range(0,x):
        if(int(bb[i])==int(aa[j])):
            flag=1
            break
    if(flag==0):
        flag1=0
        break
    flag=0
if(flag1==1):
    print("YES")
else:
    print("NO")
