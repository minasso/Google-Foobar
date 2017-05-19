
import copy as c
from fractions import Fraction
t1= [
			[0,2,1,0,0],
			[0,0,0,3,4],
			[0,0,0,0,0],
			[0,0,0,0,0],
			[0,0,0,0,0]
	]

t2=  [
			[0,1,0,0,0,1],
			[4,0,0,3,2,0],
			[0,0,0,0,0,0],
			[0,0,0,0,0,0],
			[0,0,0,0,0,0],
			[0,0,0,0,0,0]
	]
t3=[
			[0,1,0,0,0,1],
			[0,0,0,3,2,0],
			[0,0,0,0,0,0],
			[0,0,0,0,0,0],
			[0,0,0,0,0,0],
			[0,0,0,0,0,0]
	]
t4=[
	
	[0]

	]
t=t1

def dees(p):   #grab all denoms into list
	ds=[]
	for elem in p:
		denom = sum(elem)
		ds.append(denom)
	return(ds)

print('ds ='+str(dees(t)))

def dees_no_zeroes(p):   #grab all denoms into list and get rid of zeroes
	denoms=[]
	for elem in p:
		denom = sum(elem)
		denoms.append(denom)

	denoms = [x for x in denoms if x!= 0]
	return(denoms)

denoms=dees_no_zeroes(t)
def product(list):   #mult items in a list
    p = 1
    for i in list:
        p *= i
    return p
prod_denoms=product(denoms)     #mult all denoms

def terms(t):
	num_terminals=0
	for row in t:
		if sum(row)==0:
			num_terminals+=1
	return(num_terminals)

def subroutine(matrix):
	ind=0
	cum=1
	n=5
	ds=dees(t)
	ans= [1 for row in t]
	ans_d=0
	num_term=terms(t)
	while all([ v == 0 for v in t[1] ])!=True :       
		for i, subelem in enumerate(t[ind]):         #ind is row number, i is col number
			print('subelem= '+str(subelem))
			if sum(t[ind])==0:
				ans[ind]=cum
				print('temp= '+str(temp))
				print(ind)
				t[temp][ind]=0
				for row in t:
					print(row)
				cum=1
				print()
				print(ans)
				ind=0
				continue
			if subelem != 0:
				temp= c.copy(ind)           #temp= current row number 
				ind=i                       #ind=i= current col number, next row number(also prev row number if loop back to prev!**)
				if ind<temp:
					t[temp][ind]=0          #change that number to zero in matrix
					print()
					print(t)                  
					print(ind,temp)
					print('need geo')
					prev_val=t[ind][temp]
					print(prev_val)
					prev_d=ds[ind]
					print(prev_d)
					r_num=subelem
					print(r_num)
					r_denom=ds[temp]*ds[ind]
					print(r_denom)
					a0=Fraction(prev_val, prev_d)
					print(a0)
					r=Fraction(r_num, r_denom)
					print(r)
					infsum=Fraction(a0,1-r)
					ans_d=infsum.denominator
					print('ans_d= '+str(ans_d))
					break
				cum*=subelem
				print('cum= '+str(cum))
                   #set next row to hit equal to the current column number
				print('ind= '+ str(ind))
				break                       #back to while then re-enter for loop w new row number
	for i, elem in enumerate(t[0]):       
		if elem !=0:
			print(elem)
			t[0][i]=0              #kill the first nonzero element
			print(t)
			break                  #prevent other elements from being deleted
	for i, elem in enumerate(t[0]):       #takes last elem remaining and mult by prods after first row
		if elem!=0:
			if len(denoms)>2:
				print('denoms= '+str(denoms))
				ans[i]=elem* product(denoms[1:])
			else:
				print('denoms= '+str(denoms))
				ans[i]=elem* denoms[1]
			print(ans)
			break
	print('hi')
	if ans_d!=0:
		print('hm')
		ans.append(ans_d)  #add the prod of denoms to the end of ans list
	else:
		print('ho')
		ans.append(product(denoms))  #add the prod of denoms to the end of ans list
	ans=[x for x in ans if x!=1]
	print(ans)
	ans_len=len(ans)
	print(ans_len)
	print(num_term)
	dif=(num_term+1)-ans_len
	print(dif)
	ans=[0]*dif + ans  
	print(ans)
	print('ans= '+str(ans))
	return(ans)
	
subroutine(t)





# if ind<temp:
# 	t[temp][ind]=0          #change that number to zero in matrix
# 	print()
# 	print(t)                  
# 	print(ind,temp)
# 	print('need geo')
# 	prev_val=t[ind][temp]
# 	print(prev_val)
# 	prev_d=ds[ind]
# 	print(prev_d)
# 	cur_val=subelem
# 	print(cur_val)
# 	prod_d=ds[temp]*ds[ind]
# 	print(prod_d)
# 	a0=Fraction(prev_val, prev_d)
# 	print(a0)
# 	r=Fraction(cur_val, prod_d)
# 	print(r)
# 	infsum=Fraction(a0,1-r)
# 	print(infsum)
# 	return
