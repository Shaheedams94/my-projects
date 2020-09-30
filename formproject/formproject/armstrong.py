l=1
h=1000




for i in range(l,h+1):
	sum=0
	temp=i

	while temp>0:

		digit=temp%10
		sum=sum+digit**3
		temp=temp//10
		if sum==i:
			print(i)
