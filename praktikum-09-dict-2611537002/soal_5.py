n = int(input().strip())

setoran = {}

for _ in range(n):
    bagian = input().strip().split()
    if not bagian:
        continue
    nama = bagian[0]
    nominal = int(bagian[1])

    if nama in setoran:
        setoran[nama] += nominal
    else:
        setoran[nama] = nominal

# Cetak rekap tiap mahasiswa sesuai urutan kemunculan pertama
for nama, total in setoran.items():
    print(f"{nama}: {total}")

# Hitung dan cetak total kas
total_kas = sum(setoran.values())
print(f"Total cash: {total_kas}")

# Cari penyetor terbesar (jika seri, pilih yang muncul lebih dulu)
if setoran:
    top_nama, top_total = max(setoran.items(), key=lambda item: item[1])
    print(f"Top contributor: {top_nama} ({top_total})")