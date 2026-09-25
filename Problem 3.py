n=int(input())
first=[]
for x in range(n):
  v=int(input())
  first.append(v)
m=int(input())
second=[]
for x in range(m):
  v=int(input())
  second.append(v)
first=first[::-1]
second=second[::-1]
first=int(''.join([str(x) for x in first]))
second=int(''.join([str(x) for x in second]))
res=first+second
res=str(res)[::-1]
for x in res:
  print(x,end=' ')
  