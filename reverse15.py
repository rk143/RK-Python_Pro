l=int(input())
o=list(map(int,input().split()))[0:l]
o.sort(reverse=True)
i=0
while i<l:
    print(o[i],end="\n")
    i+=1
