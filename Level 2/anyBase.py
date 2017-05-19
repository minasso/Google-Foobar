#n is number, k is len of number in digits, b is base of number


def find_cycle(n, b):

	z=0
	l=[]
	l2=[]

	while len(l)<100:

		st = str(n)
		k= len(st)
		array = list(st)
		arraynum = [int(x) for x in array]

		x = sorted(arraynum)
		xst=[str(j) for j in x]
		y = sorted(arraynum, reverse=True)
		yst=[str(j) for j in y]

		xnum=''.join(xst)
		ynum=''.join(yst)
		x=int(xnum, base=b)
		y=int(ynum, base=b)
		x,y=y,x
		f=x-y
		def base10toN(num, base):
		    """Change ``num'' to given base
		    Upto base 36 is supported."""

		    converted_string, modstring = "", ""
		    currentnum = num
		    if not 1 < base < 37:
		        raise ValueError("base must be between 2 and 36")
		    if not num:
		        return '0'
		    while currentnum:
		        mod = currentnum % base
		        currentnum = currentnum // base
		        converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
		    return converted_string

		z= base10toN(f, b)
		z=str(z)
		n=z.zfill(k)

		if z in l:
			print('z= '+z)
			ind=l.index(z)
			length=len(l)
			dif=length-ind
			print(dif)
			l2.append(z)
		else:
			l.append(z)
			print(l)
			continue
		if z in l2:
			return(dif)



test1= find_cycle(1211, 10)
test2= find_cycle(210022, 3)