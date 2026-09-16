# === SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===
# Nama: Rahagi Yusrin
# NIM: 2611537002

from typing import Final

# Konstanta batas kelulusan
BATAS_LULUS: Final = 75.0

# Input data praktikan
nama_7002 = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin_7002 = input("Masukkan Jenis Kelamin (L/P): ")
umur_7002 = int(input("Masukkan Umur : "))
nilai_7002 = float(input("Masukkan Skor Tes Awal : "))

# Alamat multiline
alamat_7002 = """Jl. Kampus Unand,
Kecamatan Pauh,
Kota Padang"""

# Token identifikasi (bilangan kompleks)
id_token_7002 = 100 + 3j

# Evaluasi kelulusan (boolean)
status_lulus_7002 = nilai_7002 >= BATAS_LULUS

# Output hasil
print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print(f"Nama Mahasiswa : {nama_7002} | Tipe: {type(nama_7002)}")
print(f"Jenis Kelamin : {jenis_kelamin_7002} | Tipe: {type(jenis_kelamin_7002)}")
print(f"Alamat Domisili:\n{alamat_7002} | Tipe: {type(alamat_7002)}")
print(f"Umur : {umur_7002} tahun | Tipe: {type(umur_7002)}")
print(f"Skor Tes Awal : {nilai_7002} | Tipe: {type(nilai_7002)}")
print(f"ID Token Sinyal: {id_token_7002} | Tipe: {type(id_token_7002)}")

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print(f"Batas Minimum Nilai: {BATAS_LULUS}")
print(f"Apakah Dinyatakan Lulus?: {status_lulus_7002} | Tipe: {type(status_lulus_7002)}")
