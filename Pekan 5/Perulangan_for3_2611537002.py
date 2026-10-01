ulang_7002 = int(input("Masukkan jumlah perulangan: "))

jumlah_7002 = 0
for i_7002 in range (1, ulang_7002 + 1):
    print(i_7002, end=" ")
    jumlah_7002 = jumlah_7002 + i_7002

    if i_7002 < ulang_7002:
        print(" + ", end=" ")
    else:
        print(" = ", jumlah_7002, end=" ")
print()
print("jumlah =", jumlah_7002)