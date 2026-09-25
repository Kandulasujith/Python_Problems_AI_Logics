n=int(input())
minn=0
maxx=1
for _ in range(n):
  a,b=list(map(int,input().split()))
  minn=a
  maxx=b
  if a<maxx or b<maxx:
    print(min,maxx)
  else:
    print(a,b)