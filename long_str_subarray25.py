def loa(ar, r) : 
	m = 1
	l = 1
	for i in range(1, r) : 
		if (ar[i] > ar[i-1]) : 
			l =l + 1
		else :
			if (m < l) : 
				m = l 
			l = 1
	if (m < l) : 
		m = l 
	return m 

n =int(input()) 
arr =list(map(int,input().split()))
print(loa(arr, n)) 
