# Buat file dengan nama multi_if2_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: total_belanja_1234
# Program ini menggunakan fungsi input()
# Program Menghitung Diskon Belanja


# Input dari user
total_belanja = float(input("Masukkan total belanja (Rp): "))


# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member = input("Apakah Anda member? (y/t): ").strip().lower()
is_member = input_member in ['y', 'ya']


# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid = input_promo in ['y', 'ya']


total_diskon_persen = 0


# Multi-If terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus 
if total_belanja > 1000000:
      total_diskon_persen += 10  
# Diskon belanja besar if is_member:
    total_diskon_persen += 5   # Diskon member
  
if kode_promo_valid:
     total_diskon_persen += 15  # Diskon voucher
  
 # Menghitung nominal diskon dan total bayar
  nominal_diskon = total_belanja * (total_diskon_persen / 100)
total_bayar = total_belanja - nominal_diskon
  
  # Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon  : {total_diskon_persen}% (Rp {nominal_diskon:,.0f})")
  print(f"Total Bayar   : Rp {total_bayar:,.0f}")
  
  print(f"Total diskon yang Anda dapatkan: {total_diskon_persen}%")
  # Output: Total diskon yang Anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid