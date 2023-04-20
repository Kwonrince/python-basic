def print_min(ls):
    print('------------#1 execute------------')
    print(min(ls))

def print_sort(ls):
    print('------------#2 execute------------')
    print(sorted(ls, reverse=True))

def print_sum_minus(ls):
    print('------------#3 execute------------')
    print('sum =', min(ls)+max(ls), '\nminus =', max(ls)-min(ls))

def print_quotient_remainder(ls):
    print('------------#4 execute------------')
    try:
        print('quotient =', max(ls)//min(ls), '\nremainder =', max(ls)%min(ls))
    except:
        print("zero division error!!")
        for i in sorted(ls):
            if i==0:
                continue
            elif i!=0:
                new_min = i
                break
        print('quotient =', max(ls)//new_min, '\nremainder =', max(ls)%new_min)