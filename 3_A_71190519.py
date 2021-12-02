#memasukkan perintah input output
inputan = input("Input: ")
panjang = len(inputan)
print("Output :")

for i in range(0, panjang, 1):
    for j in range(0, i + 1):
        print(inputan[j], end='')
    print()
for i in range(panjang-1, 0, -1):
    for j in range(0, i):
        print(inputan[j], end='')
    print()
