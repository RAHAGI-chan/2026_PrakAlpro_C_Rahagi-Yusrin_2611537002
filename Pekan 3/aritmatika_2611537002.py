# Buat program untuk operator aritmatika dalam python
# Nama variabel ditambah 4 digit NIM terakhir, contoh: angka1_1234
# Progam ini menggunakan fungsi input ()
# Nilai yang dimasukkan akan dikonveri menjadi tipe data integer

angka1_7002 = int(input("Input angka-1: "))
angka2_7002 = int(input("Input angka-2: "))

# Penjumlahan
hasil = angka1_7002 + angka2_7002
print("\nOperator Penjumlahan")
print("hasil =", hasil)


# Perkalian
hasil = angka1_7002 * angka2_7002
print("\nOperator Perkalian")
print("Hasil =", hasil)

# Pembagian, Pembagian Bulat, dan sisa bagi
if angka2_7002 != 0:
    hasil = angka1_7002 / angka2_7002
    print("\nOperator Pembagian")
    print("Hasil =", hasil)

    hasil = angka1_7002 // angka2_7002
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil)

    hasil = angka1_7002 % angka2_7002
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil)
else:
    print("angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil = angka1_7002** angka2_7002
print("\nOperator Pangkat")
print("Hasil =", hasil)
