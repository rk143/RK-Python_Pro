def fa(ar, r): 

	found = False
	lsum = 0
	for i in range(r - 1): 
	
		lsum += ar[i] 
		rsum = 0
		for j in range(i + 1, r): 
			rsum += ar[j] 
		if (lsum * (r - i - 1) == rsum * (i + 1)): 
			print("yes") 
			found = True


	if (found == False): 
		print("no") 


if __name__ == "__main__":
  n= int(input())
  arr=[]
  arr=list(map(int,input().strip().split()))[:n]
  fa(arr,n) 
