# === SISTEM TRANSAKSI TOKO ===
# Program Kasir Sederhana - NIM 7002

# Input data pelanggan
nama_7002 = input("Masukkan Nama Pelanggan : ")
status_7002 = input("Masukkan Status Pelanggan (anggota/nonmember) : ").lower()
total_belanja_7002 = int(input("Masukkan Total Belanja : "))
jumlah_barang_7002 = int(input("Masukkan Jumlah Barang : "))
kode_promo_7002 = input("Masukkan Kode Promo : ")

# Daftar promo tersedia
promo_list_7002 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

# === Operator Perbandingan ===
syarat_belanja_7002 = total_belanja_7002 >= 200000
syarat_barang_7002 = jumlah_barang_7002 >= 3
status_member_7002 = status_7002 == "anggota"

# === Operator Keanggotaan ===
promo_tersedia_7002 = kode_promo_7002 in promo_list_7002

# === Operator Logika ===
dapat_diskon_7002 = status_member_7002 and syarat_belanja_7002
dapat_promo_7002 = promo_tersedia_7002 and syarat_barang_7002

# === Operator Aritmatika ===
diskon_7002 = 0
if dapat_diskon_7002:
    diskon_7002 = total_belanja_7002 * 10 / 100  # diskon 10%

# Operator Penugasan (augmented assignment)
total_bayar_7002 = total_belanja_7002
total_bayar_7002 -= diskon_7002  # -= untuk mengurangi total dengan diskon

rata_barang_7002 = total_bayar_7002 / jumlah_barang_7002
sisa_bagi_7002 = total_bayar_7002 % jumlah_barang_7002  # contoh penggunaan %

# === Operator Identitas ===
nilai_a_7002 = [1, 2, 3]
nilai_b_7002 = [1, 2, 3]
identitas_sama_7002 = nilai_a_7002 is nilai_b_7002
nilai_sama_7002 = nilai_a_7002 == nilai_b_7002

# === Operator Bitwise ===
kode_status_7002 = 0
if status_member_7002: kode_status_7002 |= 0b0001
if syarat_belanja_7002: kode_status_7002 |= 0b0010
if syarat_barang_7002: kode_status_7002 |= 0b0100
if promo_tersedia_7002: kode_status_7002 |= 0b1000

# Pemeriksaan bitwise
cek_member_7002 = kode_status_7002 & 0b0001
cek_promo_7002 = kode_status_7002 & 0b1000
perbandingan_xor_7002 = kode_status_7002 ^ 0b1011
pergeseran_7002 = kode_status_7002 << 1

# === OUTPUT PROGRAM ===
print("\n=== DATA TRANSAKSI ===")
print("Nama Pelanggan :", nama_7002)
print("Status Pelanggan:", status_7002)
print("Total Belanja: Rp", total_belanja_7002)
print("Jumlah Barang :", jumlah_barang_7002)
print("Kode Promo:", kode_promo_7002)

print("\n=== HASIL VALIDASI ===")
print("Belanja >= Rp200000 :", syarat_belanja_7002)
print("Jumlah Barang >= 3 :", syarat_barang_7002)
print("Status Anggota:", status_member_7002)
print("Kode Promo Tersedia :", promo_tersedia_7002)
print("Dapatkan Diskon :", dapat_diskon_7002)
print("Dapatkan Promo :", dapat_promo_7002)

print("\n=== HASIL PERHITUNGAN ===")
print("Diskon : Rp", int(diskon_7002))
print("Total Pembayaran : Rp", int(total_bayar_7002))
print("Rata-rata Harga Barang : Rp", int(rata_barang_7002))
print("Sisa Pembagian : Rp", sisa_bagi_7002)

print("\n=== OPERATOR IDENTITAS ===")
print("nilai_a is nilai_b :", identitas_sama_7002)
print("nilai_a == nilai_b :", nilai_sama_7002)

print("\n=== OPERASI BITWISE ===")
print("Kode Status Biner :", format(kode_status_7002, '04b'))
print("Kode Status Desimal :", kode_status_7002)
print("Cek Anggota (AND) :", cek_member_7002)
print("Cek Promo (AND) :", cek_promo_7002)
print("Perbandingan XOR :", perbandingan_xor_7002)
print("Pergeseran Kiri :", pergeseran_7002)

print("\n=== SELESAI ===")
