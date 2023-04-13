import re


def add_poly(q):
    '''Pass the polynomials to be solved as a string in the below format
    (a1x**n + b1x**n + c1x + d1) + (a2x**n + b2x**n + c2x + d2)
    Take care of the spacing between the operators while passing the input'''
    polynomials = re.split(r"\) [-+] \(" , q)
    operators = re.findall(r"\) [-+] \(", q)
    ops = []
    for op in operators:
        ops.append(op[2])
    master = []
    for i,p in enumerate(polynomials):
        master.append({})
        
        polynomial_regex = r"(([-+])?[ ]?(\d*)(x)(\*\*)?(\d*)|([-+])?[ ]?(\d+)(\))?$)"
        coeff_and_p = re.findall(polynomial_regex, p)
        for t in coeff_and_p:
            if t[3]=='x':
                power = int(t[5]) if t[4]=='**' else 1
                master[i][power] = (-int(t[2]) if t[1]=='-' else int(t[2])) if t[2]!='' else 1
            else:
                master[i][0] = -int(t[7]) if t[6]=='-' else int(t[7])
    
    result = {}
    i=-1
    for p in master:
        for k in p.keys():
            if result.get(k,0):
                if ops[i]=='+':
                    result[k]+=p[k]
                else:
                    result[k]-=p[k]
            else:
                result[k] = p[k]
        i+=1
    
    result = dict(sorted(result.items(), reverse=True))
    rs=''
    for i,(k,v) in enumerate(result.items()):
        str_v = str(v)
        if i!=0:
            if v>0:
                rs+=' + '
            else:
                str_v = ' - '+str(v*-1)
        if k>1:
            rs+=str_v+ 'x**' + str(k) if str_v!='1' else 'x**' + str(k)
        elif k==0:
            rs+=str_v
        else:
            rs+=str_v+ 'x' if str_v!='1' else 'x'
            
    print(q, "=", rs)

#testcases
add_poly('(x**3 + 5x**2 - 3x + 3) + (4x**5 - 2x**2 + 1) + (4x**3)')
add_poly('(x**3 + 5x**2 - 3x + 3) + (4x**5 - 2x**2 + 1) + (-1)')
add_poly('(x**3 + 5x**2 - 3x + 3) + (4x**5 - 2x**2 + 1)')
add_poly('(x**3 + 5x**2 - 3x + 3)')
add_poly('(x**3 + 5x**2 - 3x + 3) - (4x**5 - 2x**2 + 1)')
add_poly('(x**3 + 5x**2 - 3x + 3) - (-3)')