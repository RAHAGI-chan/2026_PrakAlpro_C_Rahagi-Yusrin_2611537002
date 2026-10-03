print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

# Input ukuran N
n_7002 = int(input("Memasukkan ukuran skala jam pasir (N): "))

# Hitung lebar bingkai horizontal
lebar_7002 = (4 * n_7002) + 5

# =========================
# Bingkai Atas
# =========================
for kolom_7002 in range(1, lebar_7002 + 1):
    if kolom_7002 == 1 or kolom_7002 == lebar_7002:
        print("#", end="")
    else:
        print("=", end="")
print()

# =========================
# Fase 1: Jam Pasir Atas
# =========================
for baris_7002 in range(n_7002, 0, -1):
    print("|", end="")       # sisi kiri
    print(" ", end="")       # padding kiri

    # spasi penyeimbang kiri
    for spasi_7002 in range(2 * (n_7002 - baris_7002)):
        print(" ", end="")

    # deret angka mundur
    for angka_7002 in range(baris_7002, 0, -1):
        print(angka_7002, end=" ")
    
    # poros kristal
    print("<*>", end="")

    # deret angka maju
    for angka_7002 in range(1, baris_7002 + 1):
        print(" " + str(angka_7002), end="")

    # spasi penyeimbang kanan
    for spasi_7002 in range(2 * (n_7002 - baris_7002)):
        print(" ", end="")

    print(" |")   # sisi kanan

# =========================
# Fase 2: Poros Tengah
# =========================
print("|", end="")
for spasi_7002 in range(2 * n_7002 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_7002 in range(2 * n_7002 + 1):
    print(" ", end="")
print("|")

# =========================
# Fase 3: Jam Pasir Bawah
# =========================
for baris_7002 in range(1, n_7002 + 1):
    print("|", end="")       # sisi kiri
    print(" ", end="")       # padding kiri

    # spasi penyeimbang kiri
    for spasi_7002 in range(2 * (n_7002 - baris_7002)):
        print(" ", end="")

    # deret angka mundur
    for angka_7002 in range(baris_7002, 0, -1):
        print(angka_7002, end=" ")

    # poros kristal
    print("<*>", end="")

    # deret angka maju
    for angka_7002 in range(1, baris_7002 + 1):
        print(" " + str(angka_7002), end="")

    # spasi penyeimbang kanan
    for spasi_7002 in range(2 * (n_7002 - baris_7002)):
        print(" ", end="")

    print(" |")   # sisi kanan

# =========================
# Bingkai Bawah
# =========================
for kolom_7002 in range(1, lebar_7002 + 1):
    if kolom_7002 == 1 or kolom_7002 == lebar_7002:
        print("#", end="")
    else:
        print("=", end="")
print()
