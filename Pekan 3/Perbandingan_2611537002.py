# Buat file dengan nama assignment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam Python

angka1_7002 = int(input("Input angka-1: "))
angka2_7002 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_7002)
print("Nilai angka2 =", angka2_7002)

# Assignment biasa
hasil = angka1_7002
print("\nAssignment biasa (=)")
print("Hasil =", hasil)

# Assignment penambahan
hasil = angka1_7002
hasil += angka2_7002
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil)

# Assignment pengurangan
hasil = angka1_7002
hasil -= angka2_7002
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil)
