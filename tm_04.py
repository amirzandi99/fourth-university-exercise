a = int(input("input age    : "))
w = int(input("input Weight : "))
if((a >= 16 and a <= 25) and (w >= 56 and w <= 65)):
    print("varzesh rozi 2 sa'at - kohnavardi hafteyi 1 bar - valibal ya basketbal hafteyi 2 bar")
elif((a >= 16 and a <= 25) and (w >= 76 and w <= 85)):
    print("varzesh rozi 4 sa'at - kohnavardi hafteyi 2 bar - tenis hafteyi 3 sa'at - estakhr hafteyi 2 bar")
elif((a >= 26 and a <= 35) and (w >= 56 and w <= 65)):
    print("varzesh rozi 1 sa'at va nim - kohnavardi hafteyi 1 bar - estakhr hafteyi 2 bar - rezhim ghazayi sabok")
elif((a >= 26 and a <= 35) and (w >= 76 and w <= 85)):
    print("varzesh rozi 1 sa'at va nim - kohnavardi hafteyi 1 bar - estakhr hafteyi 2 bar - rezhim ghazayi sangin")
elif((a >= 36 and a <= 45) and (w >= 56 and w <= 65)):
    print("varzesh rozi 1 sa'at - kohnavardi 2 bar dar mah - estakhr hafteyi 3 bar - piade ravi hafteyi 2 bar")
elif((a >= 36 and a <= 45) and (w >= 76 and w <= 85)):
    print("varzesh rozi 1 sa'at - kohnavardi 3 bar dar mah - estakhr hafteyi 3 bar - piade ravi har roz")
elif((a >= 46 and a <= 55) and (w >= 56 and w <= 65) or (w >= 76 and w <= 85)):
    print("varzesh rozi 1 sa'at - narmesh har roz 1 sa'at - estakhr hafteyi 2 bar - piade ravi har roz - rezhim ghazayi mota'adel")
elif(a >= 56):
    print("varzesh rozi 1 sa'at - narmesh har roz 1 sa'at - estakhr hafteyi 2 bar - kohnavardi hafteyi 1 bar - piade ravi har roz - rezhim ghazayi mota'adel")