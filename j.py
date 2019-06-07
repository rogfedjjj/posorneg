x1=[]
x2=[]
b=0
n=int(input())
item=input().split()
for i in item:
  x1.append(int(i))
for i in range(0,n-1):
  b=0
  for j in range(i+1,n):
    if x1[i]==x1[j]:
      b=b+1
      break
  if b>=1 and x1[i] not in x2:
    x2.append(x1[i])
z=len(x2)
if z==0:
  print("unique")
else:
  for i in x2:
    print(i,end=" ")
