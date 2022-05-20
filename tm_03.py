charges = [250,500,1000,1500,2000]
n = float(input("input data usage, GBs : "))
if(n > 0 and n <= 1.0):
    print(f"charge : {charges[0]}")
elif(n > 1.0 and n <= 2.0):
    print(f"charge : {charges[1]}")
elif(n > 2.0 and n <= 5.0):
    print(f"charge : {charges[2]}")
elif(n > 5.0 and n <= 10.0):
    print(f"charge : {charges[3]}")
elif(n > 10.0):
    print(f"charge : {charges[4]}")
else:
    print(f"input number between 1 .. 10 !\n\n")