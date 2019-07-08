from collections import C
nu1=int(input())
nu2=list(map(int,input().split()))
nu3=C(nu2)
list=[]
for x in nu3.items():
  if(x[1] != 1):
   print(x[0],end ='')
for y in nu3.items():
  list.append(y[1])
if(max(list) == 1):
  print("unique")
