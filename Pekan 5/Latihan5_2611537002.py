tinggi_7002 = int(input("Masukkan nilai segitiga: "))

for i_7002 in range(1, tinggi_7002 + 1):
    print("", end=" ")

    for j_7002 in range(tinggi_7002 - i_7002):
        print("", end=" ")
          
    for j_7002 in range(i_7002):
        print("*", end=" ")

    print()