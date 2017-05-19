# using fractions

from fractions import Fraction
from copy import deepcopy

t= [
			[0,2,1,0,0],
			[0,0,0,3,4],
			[0,0,0,0,0],
			[0,0,0,0,0],
			[0,0,0,0,0]
	]
denoms=[]
ans=[0,0,0,0,0]
	# [Fraction(0, 1), Fraction(2, 3), Fraction(1, 3), Fraction(0, 1), Fraction(0, 1), Fraction(1, 1)]
	# [Fraction(0, 1), Fraction(0, 1), Fraction(0, 1), Fraction(3, 7), Fraction(4, 7), Fraction(1, 1)]
	# [0, 0, 0, 0, 0, 0]
	# [0, 0, 0, 0, 0, 0]
	# [0, 0, 0, 0, 0, 0]
p= deepcopy(t)
n=len(p)

def denoms(matrix)
	denoms=[]
	for i, elem in enumerate(p):
		denom = sum(elem)
		elem.append(denom)
		denoms.append(denom)
		for j, subelem in enumerate(elem):
			if denom==0:
				break
			p[i][j]= Fraction(subelem, denom)

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
	while ind<n:
		for i, subelem in enumerate(p[ind]):
			# print('pind= '+ str(ind))
			if sum(p[ind])==0:
				ans[ind]=cum
				return
			if subelem != 0:
				print('sub= '+str(subelem))
				cum*=subelem
				print('cum= '+str(cum))
				ind=i
				print('ind= '+ str(ind))
				break

subroutine(p)
print(ans)


