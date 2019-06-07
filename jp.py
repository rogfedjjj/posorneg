x1,x2=input().split()
a=0
for i in range(int(x1),int(x2)+1):
    b=1
    f=0
    while b<=i:
        if i%b==0:
            f+=1
        b+=1
    if f==2:
        a+=1
print(a)
