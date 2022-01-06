products=float(input("enter products :"))
Rs=float(input("enter Rs each  products :"))
total=products*Rs
print('total is ',total)
if total >=3000:
    print('your price are discountable :',total)
    total2=total-1000
    print('with discount your price is :',total2)
else:
    print('sorry your price are not discountable :',total)
    input()