from fractions import Fraction, gcd
from functools import reduce

# ans=[Fraction(1, 3), Fraction(2, 7), Fraction(8, 21)]
# numerators=[i.numerator for i in ans]
# denominators=[i.denominator for i in ans]
# print(numerators)
# print(denominators)
##########################################

# a=[4,6]
# x=[2,3,4,97]


# def lcm(*args):
# 	xk= reduce(lambda a,b: a * b // gcd(a, b), args)
# 	print(xk)
# 	return(xk)

# lcm(*x)



# y=reduce(lambda x,y: x+y, [47,11,42,13])
# print(y)




	
# lcm2(a,b,c) = lcm2(a,lcm2(b,c))
# def gcd(a, b):
#     """Return greatest common divisor using Euclid's Algorithm."""
#     while b:      
#         a, b = b, a % b
#     return a

# def lcm(a, b):
#     """Return lowest common multiple."""
#     return a * b // gcd(a, b)

# def lcmm(*args):
#     """Return lcm of args."""   
#     return reduce(lcm, args)



# #set all diags =0

# t=  [                        #loop back to previous once
#             [1,1,0,0,0,1],
#             [4,0,0,3,2,0],
#             [0,0,0,0,0,0],
#             [0,0,0,0,0,0],
#             [0,0,0,0,0,0],
#             [0,0,0,0,0,1]
#     ]
# def kill_diag(t):
# 	for row_num, row in enumerate(t):
# 		for col_num, col in enumerate(row):
# 			if row_num == col_num:
# 				t[row_num][col_num]=0
# 	return(t)
# t= kill_diag(t)
# for row in t:
# 	print(row)


# if i < row_num:                          #loop subroutine
#     print('in loop subroutine')
#     loop = True
#     just_looped = True
#  	cum*= subelem
#  	r = cum
#     t[prev_row_temp][prev_col_temp] = 0                     
#     break

# prev_val = t[prev_row_temp][prev_col_temp]
# prev_d = ds[prev_row_temp]
# a0 = Fraction(prev_val, prev_d)
# row_num=1
# prev_row_temp=2
# prev_col_temp=1
# i=2
# if row_num == prev_col_temp and i == prev_row_temp:
# 	print('hi')

# t=  [                        #loop back to previous once
#             [0,1,0,0,0,1],
#             [4,0,0,3,2,0],
#             [0,0,0,0,0,0],
#             [0,0,0,0,0,0],
#             [0,0,0,0,0,0],
#             [0,0,0,0,0,0]
#     ]

# for i, row in enumerate(t):
# 	for j, col in enumerate(row):
# 		if t[i][j] != 0 and t[j][i] != 0

############################# transpose matrix
# matrix34 = [
# [2.5, 3.0, 4.0, 1.5],
# [1.5, 4.0, 2.0, 7.5],
# [3.5, 1.0, 1.0, 2.5]
# ]

# a=list(zip(*matrix34))
# [(2.5, 1.5, 3.5), (3.0, 4.0, 1.0), (4.0, 2.0, 1.0), (1.5, 7.5, 2.5)]

# b=sum(list(zip(*matrix34))[2])

# c=sum(list(zip(*matrix34))[3])
# print(a,b,c)
# for row in a:
# 	print(row)
# import pprint as p
# t= [
# 			[0,2,1,0,0],
# 			[0,0,0,3,4],
# 			[0,0,0,0,0],
# 			[0,0,0,0,0],
# 			[0,0,0,0,0]
# 	]

# dick=dict(((i,j), t[i][j]) for i in range(len(t)) for j in range(len(t[0])) if t[i][j]!=0)
# {(2, 0): 3, (1, 0): 2, (2, 1): 4}


# keys=list(dick.keys())
# vals=list(dick.values())
# print(keys)
# print(vals)

# j=dick.get((0,1), 0)
# print(j)

# di=list(dick.items())
# print(di)
# print(di[0][1])
items = [1, 2, 3, 4, 5]
squared = list(map(lambda (x,y): x**2, keys))

print(squared)

