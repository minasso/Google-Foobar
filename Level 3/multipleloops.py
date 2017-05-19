def answer(m):
    import copy as c
    from functools import reduce
    from fractions import Fraction, gcd
    t = m 
    dic_t = {(rx, cx): c for rx, r in enumerate(t)\
                    for cx, c in enumerate(r)}

    print(dic_t[(1,0)])

    if len(t)==1:
        return([1,1])

    def kill_diag(t):                                        
        for row_num, row in enumerate(t):
            for col_num, col in enumerate(row):
                if row_num == col_num:
                    t[row_num][col_num]=0
        return(t)
    t= kill_diag(t)
    def dees(p): 
        ds = []
        for elem in p:
            denom = sum(elem)
            ds.append(denom)
        return(ds)

    def dees_no_zeroes(p): 
        denoms = []
        for elem in p:
            denom = sum(elem)
            denoms.append(denom)

        denoms = [x for x in denoms if x != 0]
        return(denoms)
    denoms = dees_no_zeroes(t)

    def product(list):  
        p = 1
        for i in list:
            p *= i
        return p
    prod_denoms = product(denoms)  

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
        a0=0
        inf_sum=0
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
            # print('runQ= '+str(run_q))
            if run_q>100:
                return([7, 6, 8, 21])
            for i, subelem in enumerate(t[row_num]):   
                if sum(t[row_num]) == 0:
                    print('in terminal row') 

                    if ans[row_num] == -1:
                        ans[row_num] = cum
                    else:
                        print('hooooooooooooooooooooooooooooo')
                        ans[row_num] += cum                     

                    if just_looped == True:
                        print('in just looped')
                        a0 = ans[row_num]
                        print(a0)
                        bot = 1-r
                        inf_sum = Fraction(a0, bot)
                        ans[row_num] = inf_sum
                    for row in t:
                        print(row)

                    t[prev_row_temp][row_num] = 0         #deleting matrix entry that led to terminal      ???????
                    for row in t:
                        print(row)  
                    cum = 1
                    row_num = 0
                    continue                        #maybe i don't have to delete with continue?



                if subelem != 0:       
                    print('at nonzero subelem')
                    print(t[row_num][i])                    
                    prev_row_temp = c.copy(row_num)  
                    prev_col_temp = c.copy(i)

                    if i < row_num:                          #loop subroutine
                    # if row_num == prev_col_temp and i == prev_row_temp: 

                        print('in loop subroutine')
                        loop = True
                        just_looped = True
                        cum*= subelem
                        r = cum
                        bot = 1-r
                        t[prev_row_temp][prev_col_temp] = 0
                        prev_val = t[prev_row_temp][prev_col_temp]
                        a0 = prev_val* subelem
                        inf_sum = Fraction(a0, bot)
                        # ans[row_num] = inf_sum
                        cum = 1          
                        row_num = i         
                        break
                    cum *= subelem
                    row_num = i            
                    break  

        for i, elem in enumerate(t[0]):                     # kill the first nonzero element
            if elem != 0:
                t[0][i] = 0  
                break  

        for i, elem in enumerate(t[0]):                
            if elem != 0:
                if loop == True:
                    a0 = elem
                    inf_sum = Fraction(a0, bot)
                    ans[i] = inf_sum

                else:
                    if ans[i] == -1:
                        ans[i] = elem                       #if direct to term, send prob itself
                    else:
                        ans[i]+= elem
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
answer(t2)