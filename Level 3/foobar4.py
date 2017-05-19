# using fractions, lcm

from fractions import Fraction


p= [
			[0,2,1,0,0],
			[0,0,0,3,4],
			[0,0,0,0,0],
			[0,0,0,0,0],
			[0,0,0,0,0]
	]
denoms=[]
ans=[1,1,1,1,1]


def create_prob_matrix(p):
	for i, row in enumerate(p):
		denom = sum(row)
		row.append(denom)
		denoms.append(denom)
		for j, subelem in enumerate(row):
			if denom==0:
				break
			p[i][j]= Fraction(subelem, denom)
	return(p)
creation=create_prob_matrix(p)
print('creation: '+str(creation))

denoms = [x for x in denoms if x!= 0]


def lcm(num):
	if num1>num2:
		num1, num2 = num2, num1
	for x in range (num2, num1 * num2 + 1, num2):
		if x % num1 == 0:
			return x
def lcm2(nums):
	nums.sort()
	worst = nums[0]* nums[1]
	for x in range (nums[1], worst +1, nums[1]):
		if x % nums[0] == 0:
			return x
def lcm3(nums):
	nums.sort()
	worst = nums[0]* nums[1]* nums[2]
	for x in range (nums[2], worst +1, nums[2]):
		if x % nums[0] == 0 and x % nums[1] == 0:
			return x

lcd = lcm2(denoms)


def subroutine(matrix):
	ind=0
	cum=1
	n=5
	while ind<n:
		for i, subelem in enumerate(p[ind]):
			if sum(p[ind])==0:
				ans[ind]=cum
				return
			if subelem != 0:
				cum*=subelem
				ind=i
				break

subroutine(p)
print(ans)


