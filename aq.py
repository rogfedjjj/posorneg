x=int(input())
q=[]
for n in range(0,x):
 lan=input()
 q.append(lan)
thissss=[]
for n in zip(*q):
 if(n.count(n[0])==len(n)):
  thissss.append(n[0])
 else:
  break
print(''.join(thissss))
