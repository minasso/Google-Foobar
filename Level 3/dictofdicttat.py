import pprint as p
from fractions import Fraction, gcd
from functools import reduce
import pprint as p

t1= [                         #base case
            [0,2,1,0,0],
            [0,0,0,3,4],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
    ]
# t1ans=[7, 6, 8, 21]
t2=  [                        #loop back to previous once
            [0,1,0,0,0,1],
            [4,0,0,3,2,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0]
    ]
#t2ans= [0, 3, 2, 9, 14]
#[0, Fraction(3, 14), Fraction(1, 7), Fraction(9, 14)]
#[0, 3, 2, 9, 14]

t3=[                          #trivial:one terminal
    
    [0]
#t3ans= [1,1]
    ]
t4= [
            [1,2,3],          #trivial: one terminal
            [3,4,2],
            [0,0,0]
    ]
#t4ans= [1,1]
t5= [                         #self loop plus repeat
            [1,1,0,1],
            [0,0,1,1],
            [0,0,0,0],
            [0,0,0,0]
    ]
#t5ans= [1,3,4]
t6= [                         #self loop only
            [1,1,0,1,0],
            [0,0,1,0,1],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
    ]
# t6ans=[1,2,1,4]
t9= [                        
            [0,1,0,1,0],
            [0,0,1,0,1],
            [1,0,0,0,1],
            [0,0,0,0,0],
            [0,0,0,0,0]
    ]

t10= [                        
            [0,1,0,1,0],
            [0,0,1,0,1],
            [1,0,0,0,1],
            [0,0,0,1,0],
            [0,0,0,0,0]
    ]

t=t10

def answer(m):
	r=0
	t=m
	if len(t)==1:
		print([1,1])
		return([1,1])
	inf_sum=0
	ans = [-1 for row in t]
	tms=[ i for i,x in enumerate(t) if sum(x)==0  ]
	# print('tms')
	# print(tms)
	if len(tms)==1:
		# print([1,1])
		return([1,1])
	def kill_diag(t):                                        
	    for row_num, row in enumerate(t):
	        for col_num, col in enumerate(row):
	            if row_num == col_num:
	                t[row_num][col_num]=0
	    return(t)
	t= kill_diag(t)
	def create_prob_matrix(mat):
	    for i, row in enumerate(mat):
	        dnom = sum(row)
	        for j, subelem in enumerate(row):
	            if sum(row)==0:
	                break
	            mat[i][j]= Fraction(subelem, dnom)
	    return(mat)

	create_prob_matrix(t)

	dick=dict(  (  (i,j), t[i][j]  ) for i in range(len(t)) for j in range(len(t[0])) if t[i][j]!=0)

	keys=list(dick.keys())
	vals=list(dick.values())

	# print('keys')
	# print(keys)

	paths=[((x1,y1),(x2,y2)) for x1,y1 in keys for x2,y2 in keys if y1==x2 ] 
	# paths=[reduce(    (((x1,y1),(x2,y2))) for x1,y1 in keys for x2,y2 in keys if y1==x2, paths) ]  #and x1<x2

	# ky=keys
	# def pair(ky):
	# 	pth=[]
	# 	for (x1,y1) in ky:
	# 		for (x2,y2) in ky:
	# 			if y1==x2:
	# 				pth.append(((x1,y1),(x2,y2)))
	# 				return(ky)


	# paths=pair(ky)

	# print('paths')
	# print(paths)	






	# for (x1,y1),(x2,y2) in paths:
	# 	if x1==y2:        #inf loop
	# 		r=dick[(x1,y1)]*dick[(x2,y2)]
	# 		inf_sum=Fraction(1,1-r)
	# 	else:
	# 		ans[y2]=dick[(x1,y1)]*dick[(x2,y2)]

	tms=[ i for i,x in enumerate(t) if sum(x)==0  ]
	# print('tms')
	# print(tms)
	if len(tms)==1:
		# print([1,1])
		return([1,1])


	direct=dict(  ((x,y) , dick[x,y] ) for  x,y in keys if x==0 and y in tms  )
	# print('direct')
	# print(direct)


	cums=dict(  (((x1,y1),(x2,y2)),  ((dick[(x1,y1)]*dick[(x2,y2)])))  for  (x1,y1),(x2,y2) in paths if x1!=y2 and x1<y1 )
	# print('cums')
	# print(cums)
	rdict= dict(  (((x1,y1),(x2,y2)),  ((dick[(x1,y1)]*dick[(x2,y2)])))  for  (x1,y1),(x2,y2) in paths if x1==y2 and x1<x2 )
	# print('rdict')
	# print(rdict)
	infsumdict= dict(  (   (  x1,y1  ),  (  Fraction(1, 1-dick[(x1,y1)]*dick[(x2,y2)])  )  )  for  (x1,y1),(x2,y2) in paths if x1==y2 and x1<x2)
	# print('infsumdict')
	# print(infsumdict)

	for (x1,y1), v in cums.items():                       #adjust cums to accommodate infsum
		if x1 in infsumdict:
			cums[x1,y1]*= infsumdict.get(x1,y1)



	for (x1,y1), v in direct.items():                       #adjust direct to accommodate infsum
		print(x1)
		for j in range(1,10):
			if (x1,j) in infsumdict:
				print(x1,y1)
				print(x1,j)
				print(infsumdict.get(x1,y1))
				direct[x1,y1]*= infsumdict[x1,j]



	for k, v in cums.items():
		# print('items')
		# print(k,v)
		ans[k[1][1]]=v
		# print('ans1')
		# print(ans)
		

	for (x1,y1), v in direct.items():
		# print(x1,y1,v)
		if ans[y1]==-1:
			ans[y1]=v
		else:
			ans[y1]+=v
		# print(ans)


	# for k, v in infsumdict.items():
	# 	# print('items')
	# 	print(k[0])
		

	        





	ans = [x for x in ans if x != -1]           # kill -1's representing unreached states
	def terms(t):
	    num_terminals = 0
	    term_ind=[]
	    for i, row in enumerate(t):
	        if sum(row) == 0:
	            num_terminals += 1
	            term_ind.append(i)
	    return(num_terminals, term_ind)

	num_term, term_i = terms(t)

	ans_len = len(ans)                          #pad zeroes (*still need to add in denom)
	dif = num_term - ans_len
	ans = [0] * dif + ans


	def lcm(*args):
	    xk= reduce(lambda a,b: a * b // gcd(a, b), args)
	    # print(xk)
	    return(xk)

	numerators=[i.numerator for i in ans]          
	denominators=[i.denominator for i in ans]

	lcd=lcm(*denominators)

	timesby=[]                                                      
	for i,d in enumerate(denominators):
	    timesby.append(Fraction(lcd, denominators[i]))

	numerators=[x*y for x,y in zip(numerators, timesby)]
	# print(numerators)
	ans=numerators
	ans.append(lcd)
	ans=[int(x) for x in ans]
	# print('ans')
	# print(ans)
	return(ans)
answer(t)

