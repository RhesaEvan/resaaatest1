P = int(input("Masukan pilihan (1/2) "))
R = float(input("Masukan jari-jari :"))
if P == 1:
    print("Keliling lingkaran :", 2*3.14*R)
elif P == 2:
    print("Luas lingkaran :", 3.14*R*R)
else:
    print("Pilihan tidak tersedia")    
