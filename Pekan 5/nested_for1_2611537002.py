batas_7002 = int(input("Masukkan nilai batas: "))
for line in range(1, batas_7002 + 1):
    for j_7002 in range(1, (-1 * line + batas_7002) + 1):
        print(".", end="")
print(line)