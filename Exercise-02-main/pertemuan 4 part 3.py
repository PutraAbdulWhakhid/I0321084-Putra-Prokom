angka = int(input("masukkan angka dasar="))
pangkat = int(input("masukkan nilai pangkat="))
y = 1

while pangkat != 0:
    y= y *angka
    pangkat = pangkat -1
print("hasilnya=", y)