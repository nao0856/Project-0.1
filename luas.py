def hitungKLlingkaran (r):
    luas = math.pi * ( r ** 2)
    keliling = 2 * math.pi *r
    return luas, keliling
    JJ = float(input("masukkan angka jari jari: "))
    luas, keliling = hitungKLlingkaran(JJ)
    print("luas : ", luas)
    print("keliling : ", keliling)