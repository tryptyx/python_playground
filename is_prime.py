#!/usr/bin/python

import math

def get_if_prime(val):
	max_sqrt = math.sqrt(val);

	if (val % 2 == 0):
		print("is Divisable by 2")
		return (False); 
		
	if (val % 3 == 0):
		print("is Divisable by 3")
		return (False); 

    # now go on to test the 6k +/- 1
	for k in range(0, 10000):
		#6k+1
		testval = 6 * k + 1;
		if testval > max_sqrt:
			break
		if val % testval == 0:
			return (False)
		#6k-1
		testval = 6 * k - 1;
		if testval > max_sqrt:
			break
		if (val % testval == 0):	
			print("Dividing by "),
			print(testval)
			return (False)
	return(True)
	
		
# print("Please enter a number: "),
val=input()
res = get_if_prime(val)
if (res==True):
	print str(val)+" is prime"
else:	
	print str(val)+" is composite"





# for k in range(0, 10000):
# 	res = get_if_prime(k)
# 	print(res),
# 	if (res==True):
# 		print str(k)+" is prime"
# 	else:	
# 		print str(k)+" is not prime"