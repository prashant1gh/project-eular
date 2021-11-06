def common_remover(nume,deno):
    
    a = set(list(str(nume)))
    b = set(list(str(deno)))
    
    common = a.intersection(b)

    if common:
        common = common.pop()

        simplified_nume = int(str(nume).replace(common, ''))
        simplified_deno = int(str(deno).replace(common, ''))

        return  (simplified_nume, simplified_deno)

def is_digit_same(number):
    return list(str(number))[0]==list(str(number))[1]


deno_lst = []
for i in range(12,100):
    for j in range(13,100):

        if not i == j and not is_digit_same(i) and not is_digit_same(j):
            if not '0' in str(i) and not '0' in str('j'):
                a = common_remover(i, j)
                if a:
                    if a[0]==0 or a[1]==0:
                        pass
                    else:
                        if i/j == a[0]/a[1]:
                            print(f'{i}/{j}')