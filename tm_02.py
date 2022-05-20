color1 = ["Yellow","White","Gray","Red","Brown","Green"]
color2 = ["Y","W","G","R","B","G"]
color3 = ["y","w","g","r","b","g"]
n = str(input("input character color : "))
for i in range(len(color1)):
    if(n == color2[i] or n == color3[i]):
        print(f"\ncolor : {color1[i]}")
        break