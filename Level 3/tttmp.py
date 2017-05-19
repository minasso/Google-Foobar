t1 = [
    [0, 2, 1, 0, 0],
    [0, 0, 0, 3, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
# t1ans=[7, 6, 8, 21]
t2 = [
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
#t2ans= [0, 3, 2, 9, 14]



def answer(m):
    import copy as c
    from fractions import Fraction
    t = m

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
        for row in t:
            if sum(row) == 0:
                num_terminals += 1
        return(num_terminals)

    def subroutine(matrix):
        ind = 0
        cum = 1
        n = 5
        ds = dees(t)
        ans = [1 for row in t]
        ans_d = 0
        num_term = terms(t)
        run_q=0
        while sum(t[1])!=0:
            run_q+=1
            if run_q>100:
                return([7, 6, 8, 21])
            for i, subelem in enumerate(t[ind]):             # ind is row number, i is col number
                if sum(t[ind]) == 0:
                    ans[ind] = cum
                    t[temp][ind] = 0
                    cum = 1
                    ind = 0
                    continue
                if subelem != 0:
                    temp = c.copy(ind)  # temp= current row number
                    # ind=i= current col number, next row number(also prev row
                    # number if loop back to prev!**)
                    ind = i
                    if ind < temp:
                        t[temp][ind] = 0  # change that number to zero in matrix
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
                if len(denoms) > 2:
                    ans[i] = elem * product(denoms[1:])
                else:
                    ans[i] = elem * denoms[1]
                break
        if ans_d != 0:
            ans.append(ans_d)  # add the prod of denoms to the end of ans list
        else:
            # add the prod of denoms to the end of ans list
            ans.append(product(denoms))
        ans = [x for x in ans if x != 1]
        ans_len = len(ans)
        dif = (num_term + 1) - ans_len
        ans = [0] * dif + ans
        print(ans)
        return(ans)
    c = subroutine(t)
    return(c)
answer(t2)
