c=int(input(""))
temp=c
a=0
while(c>0):
    x=c%10
    a=a*10+x
    c=c//10
if(temp==a):
    print("yes")
else:
    print("no")
