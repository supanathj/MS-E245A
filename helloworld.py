import math

#Investment Science HW1

#Question 3
def frange(start, stop, step):
	i = start
	while i<=stop:
		yield i
		i += step

def calculate_pv(init,A,r,n):
	pv = init
	for i in frange(0,n-1,1):
		pv = pv + A/((1+(r*(i+1))))
		#print(i+1)
	return pv

def calculate_pv_concom(init,A,r,n):
	pv = init
	for i in frange(0,n-1,1):
		pv = pv + A/((math.e**(r))**(i+1))
		#print(i+1)
	return pv

# #1_i
# PV1_i = calculate_pv(1000,1000,0.12/12,6)
# print(PV1_i)

# #1_ii
# PV1_ii = calculate_pv(1000+900,900,0.12/12,6)
# print(PV1_ii)

# #2_i
# PV2_i = calculate_pv(1000,1000,0.12/12,12)
# print(PV2_i)

# #2_ii
# PV2_ii = calculate_pv(1000+900,900,0.12/12,12)
# print(PV2_ii)

# #Question 6
# NPV1 = calculate_pv(-100,30,0.05,6)
# print(NPV1)

# NPV2 = calculate_pv(-150,42,0.05,6)
# print(NPV2)

# for i in frange (660.49,660.55,0.001):
# 	NPV_1 = calculate_pv(0,i,0.05/12,61)
# 	print('i is:', '%.3f' %i, 'and NPV is:','%.3f' %NPV_1)

#X = calculate_pv(0,660.5,0.05/12,61)
#print(X)
#for j in frange(314,316,0.01):
#	NPV_2 = calculate_pv(0,200,0.05/12,j)
#	print('j is:', '%.3f' %j, 'and NPV is:','%.3f' %NPV_2)

#for k in frange(314,316,0.01):
#	NPV_2 = calculate_pv_concom(0,200,0.05/12,k)
#	print('k is:', '%.3f' %k, 'and NPV is:','%.3f' %NPV_2)

B = calculate_pv(0,654.765,0.05/12.0,60)
print(B)
A = calculate_pv(0,200,0.05/12.0,259)
print(A) 

Y = calculate_pv_concom(0,660.665,0.05/12,60)
print(Y)
X = calculate_pv_concom(0,200,0.05/12.0,315)
print(X)