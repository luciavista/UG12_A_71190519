#input deret
deret_angka = input("Masukkan deret angka : ")
pemisah = deret_angka.split(",")
jumlah = len(pemisah)

if(int(pemisah[0]) % 2 == 0):
    mulai = pemisah[0]
    hitung = int(mulai)
else:
    mulai = int(pemisah[0])* -1
    hitung = int(mulai)

print("Total :", mulai, end="")

for a in pemisah[1:jumlah]:
    if(a != pemisah[0]):
        if (int(a) % 2 == 1):
            a = int(a) * -1
            hitung = hitung + int(a)
            print("", a, end="")
        elif (int(a) % 2 == 0):
            hitung = hitung + int(a)
            if (a == pemisah[0]):
                print(a, end="")
            else:
                print(" +", a, end="")

#print hasil
print()
print("Hasil perhitungan diatas ialah", hitung)
