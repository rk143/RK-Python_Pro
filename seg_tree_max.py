r,k=map(int,input().split())
h=(input().split())[0:r]
i=0
while i<k:
  o,p=map(int,input().split())
  i+=1
  print(min(h[o-1:p]))
