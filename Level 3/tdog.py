#deleting finished entries. 
#works on base case, brutish towards end
#trying w/o probabilities

t= [
			[0,2,1,0,0],
			[0,0,0,3,4],
			[0,0,0,0,0],
			[0,0,0,0,0],
			[0,0,0,0,0]
	]


def dees(p):   #grab all denoms into list and get rid of zeroes
	denoms=[]
	for elem in p:
		denom = sum(elem)
		denoms.append(denom)

	denoms = [x for x in denoms if x!= 0]
	return(denoms)

denoms=dees(t)
def product(list):   #mult items in a list
    p = 1
    for i in list:
        p *= i
    return p
prod_denoms=product(denoms)     #mult all denoms



ans=[1,1,1,1,1]
nonterm_ind=[0,1]
term_ind=[2,3,4]

def subroutine(matrix):
	ind=0
	cum=1
	n=5
	while all([ v == 0 for v in t[1]])!=True:       
		for i, subelem in enumerate(t[ind]):         #ind is row number, i is col number
			print('subelem= '+str(subelem))
			if sum(t[ind])==0:
				ans[ind]=cum
				print(ind)
				for row in t:
					print(row)
				cum=1
				print()
				print(ans)
				ind=0
				continue
			if subelem != 0:
				cum*=subelem
				print('cum= '+str(cum))
				ind=i    
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
			ans[i]=elem* product(denoms[1:])
			print(ans)
			return
subroutine(t)


ans=[x for x in ans if x!=1]
ans.append(product(denoms))  #add the prod of denoms to the end of ans list

print(ans)



