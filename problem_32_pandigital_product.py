#!/usr/bin/python

def is_pandigital(stringified_number):
    a = list(stringified_number)
    for i in range(1,10):
        if str(i) in a:
            a.remove(str(i))
    return len(a)==0

if __name__ == '__main__':

    count=0
    products = []
    for i in range(1, 100):
        for j in range(1, 10000):
            if len(str(i)+str(j)+str(i*j))==9:
                string = str(i)+str(j)+str(i*j)
                if is_pandigital(string):
                    print(f'{i} x {j} = {i*j}')
                    if i*j not in products:
                        products.append(i*j)
                        count+=(i*j)
    
    print(count)