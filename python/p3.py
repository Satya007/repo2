n = 10
count = 0
sum = 0
while count < n:
	num = int(raw_input("Enter the numbers :"))
	sum=sum+num
	count=count+1
avg=float(sum/n)
print "sum=%d"% sum
print "avg=%d"% avg
