fl=int(input())
nspaced=[]
for _ in range(f1):
  n=int(input())
  nspaced.append(n)
max_allow=int(input())

window_stable=[]
left=0
right=left+1
for x in range(len(nspaced)):
  if nspaced[left]-nspaced[right]<=max_allow:
    window_stable.append(npaced[left],nspaced[right])
    left+=1
    right+=1
print(window_stable)
    