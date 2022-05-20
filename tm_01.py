discount = 0
total = float(input("input total purchases    : "))
t = total
student = str(input("are you student -> (y,n) : "))
if(student == 'y'):
    discount = (total * 20) / 100
    temp = total - discount
    tax = (temp * 5) / 100
    total_d = total - discount
    t = total - discount + tax
    ts = "{:.2f}".format(t)
else:
    tax = (total * 5) / 100
    t = total - discount + tax
    ts = "{:.2f}".format(t)
# 
# 
print (f"\n\ntotal purchases    : {total}")
if(student == 'y'):
    print (f"student's discount : {discount}")
    print (f"discounted total   : {total_d}")
print (f"sales tax          : {tax}")
print (f"total              : {ts}")