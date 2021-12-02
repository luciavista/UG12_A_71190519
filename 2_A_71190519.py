#input nama dan nomor kursi
nama = []
kursi = []

#penggunaan if elif
while(True):
    input_nama = input("Masukkan nama: ")
    if input_nama == "STOP":
        break

    input_kursi = input("Masukkan nomor kursi "+input_nama+": ")
    if input_kursi == "STOP":
        break

    if input_kursi in kursi:
        print("Mohon maaf kursi tersebut telah terisi!")

    elif input_kursi not in kursi:
        nama.append(input_nama)
        kursi.append(input_kursi)

print()
print("List kursi yang telah terisi : ")

for isi in range(0, len(kursi), 1):
    print("Kursi nomor", kursi[isi], "telah diisi oleh", nama[isi])
