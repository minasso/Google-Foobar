testcase1='--->-><-><-->-'
testcase2='>----<'
testcase3='<<>><'

def hallpass(st):

	n=0
	st=st.replace('-','')
	print(st)
	while len(st)>1:
		if st.startswith('<'):
			st=st[1:]
			print(st)	
		else:
			n=n+2*st.count('<') 
			print(n)
			st=st[1:]
			print(st)
	print(n)
	return(n)
hallpass(testcase3)



