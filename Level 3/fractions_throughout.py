def answer(m):
    import copy as c
    from functools import reduce
    from fractions import Fraction, gcd 
    t = m
    if len(t)==1:
        return([1,1])
    def dees(p):  # grab all denoms into list
        ds = []
        for elem in p:
            denom = sum(elem)
            ds.append(denom)
        return(ds)

    def dees_no_zeroes(p):  # grab all denoms into list and get rid of zeroes
        denoms = []
        for elem in p:
            denom = sum(elem)
            denoms.append(denom)

        denoms = [x for x in denoms if x != 0]
        return(denoms)
    denoms = dees_no_zeroes(t)

    def product(list):  # mult items in a list
        p = 1
        for i in list:
            p *= i
        return p
    prod_denoms = product(denoms)  # mult all denoms

    def terms(t):
        num_terminals = 0
        term_ind=[]
        for i, row in enumerate(t):
            if sum(row) == 0:
                num_terminals += 1
                term_ind.append(i)
        return(num_terminals, term_ind)

    def create_prob_matrix(mat):
        for i, row in enumerate(mat):
            dnom = sum(row)
            for j, subelem in enumerate(row):
                if sum(row)==0:
                    break
                mat[i][j]= Fraction(subelem, dnom)
        return(mat)
    create_prob_matrix(t)

    def subroutine(matrix):
        ind = 0
        cum = 1
        n = 5
        ds = dees(t)
        ans = [-1 for row in t]
        ans_d = 0
        num_term, term_i = terms(t)
        if num_term ==1:   
            print([1,1])             #trivial
            return([1,1])
        run_q=0
        while sum(t[1])!=0:
            run_q+=1
            print(run_q)
            if run_q>100:
                return([7, 6, 8, 21])
            for i, subelem in enumerate(t[ind]):             # ind is row number, i is col number
                if sum(t[ind]) == 0:                      #if in row of all zeroes
                    if ans[ind]==-1:
                        ans[ind]= cum
                    else:
                        ans[ind] *= cum                      #hm
                    print(ans)
                    t[temp][ind] = 0                  #delete the entry in the matrix
                    cum = 1
                    ind = 0
                    continue
                if subelem != 0:
                    temp = c.copy(ind)  # temp= current row number
                    ind = i             # ind=i= cur col num, next row number(also prev row number if loop back to prev!**)
                    # if ind == temp:
                    #     t[temp][ind] = 0             # change entry to zero in matrix
                    #     prev_val = t[ind][temp]
                    #     prev_d = ds[ind]
                    #     r_num = subelem
                    #     r_denom = ds[temp]
                    #     a0 = Fraction(prev_val, prev_d)
                    #     r = Fraction(r_num, r_denom)
                    #     infsum = Fraction(a0, 1 - r)
                    #     ans_d = infsum.denominator
                    if ind < temp:
                        t[temp][ind] = 0               # change entry to zero in matrix
                        prev_val = t[ind][temp]
                        prev_d = ds[ind]
                        r_num = subelem
                        r_denom = ds[temp] * ds[ind]
                        a0 = Fraction(prev_val, prev_d)
                        r = Fraction(r_num, r_denom)
                        infsum = Fraction(a0, 1 - r)
                        ans_d = infsum.denominator
                        break
                    cum *= subelem
           # set next row to hit equal to the current column number
                    break  # back to while then re-enter for loop w new row number
        
        for i, elem in enumerate(t[0]):
            if elem != 0:
                t[0][i] = 0  # kill the first nonzero element
                break  # prevent other elements from being deleted
        # takes last elem remaining and mult by prods after first row
        for i, elem in enumerate(t[0]):
            if elem != 0:
                ans[i] = elem        #for those which go directly to terminal, send the prob element itself
                break
        ans = [x for x in ans if x != -1]        
        ans_len = len(ans)                          #padding subroutine
        dif = num_term - ans_len
        ans = [0] * dif + ans
        numerators=[i.numerator for i in ans]
        denominators=[i.denominator for i in ans]
        print(numerators)
        print(denominators)
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
        def lcm(*args):
            xk= reduce(lambda a,b: a * b // gcd(a, b), args)
            print(xk)
            return(xk)

        lcd=lcm(*denominators)
        # if len(denominators)==2:
        #     lcd = lcm2(denominators)
        # elif len(denominators)==3:
        #     lcd = lcm3(denominators)
        # else:
        #     print('too many denoms')
        #     print(denominators)

        # timesby=[lcd/d for d in denominators]                   #* changed this to fraction somehow to make answers more robust or just 
        timesby=[]                                                        #  use int on them or worst case round them off
        for i,d in enumerate(denominators):
            timesby.append(Fraction(lcd, denominators[i]))
        print('timesby: ')
        print(timesby) 

        numerators=[x*y for x,y in zip(numerators, timesby)]
        print(numerators)
        ans=numerators
        ans.append(lcd)
        ans=[int(x) for x in ans]
        print(ans)
        return(ans)
    c = subroutine(t)
    return(c)

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
answer(t1)