def bilangan(n):
    ganjil = 0
    kel5 = 0
    bilganjil = []
    bilkel5 = []
    for i in range(n+1):
        if i%2 == 1:
            ganjil += 1
            bilganjil.append(i)
        if i%5 == 0 and i!=0:
            kel5 += 1
            bilkel5.append(i)

    print("Jumlah bilangan ganjil adalah", ganjil, bilganjil)
    print("Jumlah bilangan kelipatan 5 adalah", kel5, bilkel5)

bilangan(7)
