# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas


print("==========================================")
print("1. OPERATOR KEANGGOTAAN")
print("==========================================")

# Input beberapa data yang dipisahkan dengan koma
input_data = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_7002 = [int(angka.strip()) for angka in input_data.split(',')]

nilai_dicari = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil = nilai_dicari in data_7002
print("\nOperator keanggotaan IN")
print(nilai_dicari, "in", data_7002, "=", hasil)


# Operator not in
hasil = nilai_dicari not in data_7002
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari, "not in", data_7002, "=", hasil)