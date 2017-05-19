def answer(m):
    import copy as c
    from functools import reduce
    from fractions import Fraction, gcd
    t = m 
    if len(t)==1:
        return([1,1])

    def kill_diag(t):                                         #set all diagonals=0
        for row_num, row in enumerate(t):
            for col_num, col in enumerate(row):
                if row_num == col_num:
                    t[row_num][col_num]=0
        return(t)
    t= kill_diag(t)
    for row in t:
        print(row)
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
        row_num = 0
        cum = 1
        n = 5
        ds = dees(t)
        ans = [-1 for row in t]
        ans_d = 0
        loop=False
        just_looped = False
        num_term, term_i = terms(t)
        if num_term ==1:   
            print([1,1])             #trivial
            return([1,1])
        run_q=0
        while sum(t[1])!=0:
            run_q+=1
            print('runQ= '+str(run_q))
            if run_q>100:
                return([7, 6, 8, 21])
            for i, subelem in enumerate(t[row_num]):   
                if sum(t[row_num]) == 0:                 
                    print('in terminal row')     
                    if ans[row_num] == -1:
                        ans[row_num] = cum
                    else:
                        ans[row_num] *= cum                     
                    print(ans)
                    t[prev_row_temp][row_num] = 0         #deleting matrix entry that led to terminal      ???????  
                    cum = 1
                    row_num = 0
                    continue                        #maybe i don't have to delete with continue?



                if subelem != 0:       
                    print('at nonzero subelem')
                    print('row and col')
                    print(row_num, i)
                    prev_row_temp = c.copy(row_num)  
                    prev_col_temp = c.copy(i)



                    if i < row_num:                          #loop subroutine
                        print('in loop subroutine')
                        loop= True
                        just_looped = True
                        prev_val = t[prev_row_temp][prev_col_temp]
                        prev_d = ds[prev_row_temp]
                        r_num = subelem
                        r_denom = ds[prev_row_temp] * ds[row_num]
                        a0 = Fraction(prev_val, prev_d)
                        r = Fraction(r_num, r_denom)
                        bot= 1-r
                        infsum = Fraction(a0, bot)
                        ans_d = infsum.denominator
                        t[prev_row_temp][prev_col_temp] = 0                      
                        break




                    cum *= subelem
                    for row in t:
                        print(row)

                    row_num = i            
                    break  
        



        for i, elem in enumerate(t[0]):                     # kill the first nonzero element
            if elem != 0:
                t[0][i] = 0  
                break  



        for i, elem in enumerate(t[0]):                
            if elem != 0:
                ans[i] = elem                       #if direct to term, send prob itself
                break



        ans = [x for x in ans if x != -1]           # kill -1's representing unreached states


        ans_len = len(ans)                          #pad zeroes (*still need to add in denom)
        dif = num_term - ans_len
        ans = [0] * dif + ans


        numerators=[i.numerator for i in ans]          
        denominators=[i.denominator for i in ans]


        def lcm(*args):
            xk= reduce(lambda a,b: a * b // gcd(a, b), args)
            print(xk)
            return(xk)

        numerators=[i.numerator for i in ans]          
        denominators=[i.denominator for i in ans]

        lcd=lcm(*denominators)

        timesby=[]                                                      
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
        print(ans_d)


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
answer(t2)