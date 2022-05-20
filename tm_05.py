n = int(input("input number -> (1, 2, 3) : "))
c = str(input("input character -> (n, m) : "))
if(n == 1):
    if(c == 'n'):
        print(f"\nSquare perimeter -> 4 * side")
        s = int(input("input side : "))
        r = 4 * s
        print(f"\nresult : {r}\n")
    elif(c == 'm'):
        print(f"\nSquare area -> side ^ 2")
        s = int(input("input side : "))
        r = s ** 2
        print(f"\nresult : {r}\n")
elif(n == 2):
    if(c == 'n'):
        print(f"\nRectangle perimeter -> (length + width) * 2")
        l = int(input("input length : "))
        w = int(input("input width  : "))
        r = (l + w) * 2
        print(f"\nresult : {r}\n")
    elif(c == 'm'):
        print(f"\nRectangle area -> length * width")
        l = int(input("input length : "))
        w = int(input("input width  : "))
        r = l * w
        print(f"\nresult : {r}\n")
elif(n == 3):
    if(c == 'n'):
        print(f"\nCircle perimeter -> PI * r ^ 2")
        ra = float(input("input radius : "))
        Pi = 3.14
        r = Pi * (ra ** 2)
        print(f"\nresult : {r}\n")
    elif(c == 'm'):
        print(f"\nCircle area -> 2 * PI * r")
        ra = float(input("input radius : "))
        Pi = 3.14
        r = 2 * Pi * ra
        print(f"\nresult : {r}\n")
else:
    print("input number between 1 .. 3 !\n")