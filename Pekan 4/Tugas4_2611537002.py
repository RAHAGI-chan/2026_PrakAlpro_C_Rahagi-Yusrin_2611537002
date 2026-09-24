print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

nama_pengunjung_7002 = input("Masukkan Nama Pengunjung : ")
umur_7002 = int(input("Input umur anda : "))
sim_7002 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0].lower()

print("\nPilihan Paket Wahana (1-5):")
print(" 1. Safari Rimba (Rp 50,000)")
print(" 2. Arung Jeram (Rp 75,000)")
print(" 3. Motor ATV Ekstrim (Rp 120,000)")
print(" 4. Roller Coaster Kilat (Rp 100,000)")
print(" 5. All-Access VIP (Rp 220,000)")

paket_7002 = int(input("Masukkan nomor paket (1-5) : "))
jumlah_tiket_7002 = int(input("Masukkan jumlah tiket : "))

if jumlah_tiket_7002 <= 0:
    print("Peringatan: Kuota tiket tidak valid.")

is_member_7002 = input("Apakah Anda member? (y/t) : ").strip().lower()
kode_promo_valid_7002 = input("Apakah kode promo valid? (y/t) : ").strip().lower()

harga_satuan_7002 = 0
nama_wahana_7002 = ""

match paket_7002:
    case 1:
        nama_wahana_7002 = "Wahana Safari Rimba"
        harga_satuan_7002 = 50000
    case 2:
        nama_wahana_7002 = "Wahana Arung Jeram"
        harga_satuan_7002 = 75000
    case 3:
        nama_wahana_7002 = "Wahana Motor ATV Ekstrim"
        harga_satuan_7002 = 120000
    case 4:
        nama_wahana_7002 = "Wahana Roller Coaster Kilat"
        harga_satuan_7002 = 100000
    case 5:
        nama_wahana_7002 = "Wahana All-Access VIP"
        harga_satuan_7002 = 220000
    case _:
        print("Paket wahana tidak valid!")
        exit()

print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_7002 == 3:
    if umur_7002 >= 17 and sim_7002 == 'y':
        print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
    elif umur_7002 >= 17 and sim_7002 != 'y':
        print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
    elif umur_7002 < 17 and sim_7002 == 'y':
        print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
    else:
        print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
else:
    if umur_7002 >= 10:
        print("Status Akses: Anda memenuhi batas usia untuk wahana.")
    else:
        print("Status Akses: Anda belum cukup umur untuk wahana ini.")

subtotal_7002 = harga_satuan_7002 * jumlah_tiket_7002
total_diskon_persen_7002 = 0

if subtotal_7002 >= 200000:
    total_diskon_persen_7002 += 10

if is_member_7002 in ['y', 'ya']:
    total_diskon_persen_7002 += 5

if kode_promo_valid_7002 in ['y', 'ya']:
    total_diskon_persen_7002 += 15

if jumlah_tiket_7002 >= 5:
    total_diskon_persen_7002 += 5

nominal_diskon_7002 = subtotal_7002 * (total_diskon_persen_7002 / 100)
total_bayar_7002 = subtotal_7002 - nominal_diskon_7002

print("\n--- Rincian Pembayaran ---")
print(f"Nama Pengunjung : {nama_pengunjung_7002}")
print(f"Wahana : {nama_wahana_7002}")
print(f"Jumlah Tiket : {jumlah_tiket_7002}")
print(f"Subtotal Belanja : Rp {subtotal_7002:,.0f}")
print(f"Total Diskon : {total_diskon_persen_7002}% (Rp {nominal_diskon_7002:,.0f})")
print(f"Total Bayar : Rp {total_bayar_7002:,.0f}")

if total_bayar_7002 > 300000:
    print("Catatan Layanan : Selamat! Anda berhak mendapatkan Souvenir Gratis.")
else:
    print("Catatan Layanan : Terima kasih telah berkunjung.")

print("Program Selesai")
