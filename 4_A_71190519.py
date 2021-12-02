#proses input output
inputan = int(input("Input : "))
print("Output :")
a = 2

#perulangan untuk kolom dan baris
for kolom in range(1, inputan+1):
    for baris in range(1, 2*inputan):
        if kolom+baris == inputan+1 or baris-kolom == inputan-1:
            print("*", end="")
        elif kolom == inputan and baris != a:
            print("*", end="")
            a = a+2
        else:
            print(end=" ")
    print()
