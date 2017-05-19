#start deleting finished entries?
#denoms on tmpe.py
#trying w/o probabilities
t= [
			[0,2,1,0,0],
			[0,0,0,3,4],
			[0,0,0,0,0],
			[0,0,0,0,0],
			[0,0,0,0,0]
	]
denoms=[]
ans=[1,1,1,1,1]

# def subby(matrix):
# 	i=0
# 	cum=1

# 	a=0
# 	for i, row in enumerate(t):
# 		for j, elem in enumerate(row):
# 			if elem != 0:
# 				print('sub= '+str(elem))
# 				cum*=elem
# 				ans[j]*=cum
# 				print('cum= '+str(cum))
# 				print('ans['+str(i)+']= '+str(ans[j]))
# 				i=j
# 				print('ind= '+ str(i))
# 		# 		continue
# 		# if all([ v == 0 for v in row ]) :
			
# subby(t)
# print(ans)







def subroutine(matrix):
	ind=0
	cum=1
	n=5
	while ind<n:
		for i, subelem in enumerate(t[ind]):
			print('subelem= '+str(subelem))
			print('ind= '+ str(ind))
			if sum(t[ind])==0:
				ans[ind]=cum
				print(ans)
				return
			if subelem != 0:
				print('sub= '+str(subelem))
				cum*=subelem
				print('cum= '+str(cum))
				ind=i
				print('ind= '+ str(ind))
				break

subroutine(t)




# def subby(matrix):
# 	i=0
# 	cum=1

# 	a=0
# 	for i, row in enumerate(t):
# 		for j, elem in enumerate(row):
# 			if elem != 0:
# 				print('sub= '+str(elem))
# 				cum*=elem
# 				ans[j]*=cum
# 				print('cum= '+str(cum))
# 				print('ans['+str(i)+']= '+str(ans[j]))
# 				i=j
# 				print('ind= '+ str(i))
# 		# 		continue
# 		# if all([ v == 0 for v in row ]) :
			
# subby(t)
# print(ans)
