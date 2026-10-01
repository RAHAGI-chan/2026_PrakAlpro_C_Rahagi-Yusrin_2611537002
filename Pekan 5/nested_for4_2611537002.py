tinggi_7002 = int(input("Masukkan tinggi pola (Bilangan genap, misal 10): "))

if tinggi_7002 % 2 != 0:
    print("Tinggi haru bilangan genap!")
else:
    a_7002 = tinggi_7002
    c_7002 = a_7002
    lebar_7002 = (2 * tinggi_7002) - 2

    for i_7002 in range(1, tinggi_7002 +1):
        b_7002 = c_7002 + 1

        for j_7002 in range(1, lebar_7002 + 1):

            # Baris atas dan bawah
            if i_7002 == 1 or i_7002 == tinggi_7002:
                if j_7002 == 1 or j_7002 == lebar_7002:
                    print("#", end="")
                else:
                    print("=", end="")
            
            # Baris isi

            else:
                if j_7002 == 1 or j_7002 == lebar_7002:
                    print("|", end="")
                else:
                    if j_7002 == c_7002:
                        print("<", end="")
                    elif j_7002 == b_7002:
                        print(">", end="")
                    elif j_7002 == (lebar_7002 - c_7002 - 1):
                        print("<", end="")
                    elif j_7002 == (lebar_7002 - c_7002 + 1):
                        print(">", end="")
                    elif j_7002> b_7002 and j_7002 < (lebar_7002 -c_7002):
                        print(",", end="")
                    else:
                        print (" ", end="")
        print()

        # Logika asli j_7002ava
        a_7002 -= 2

        if a_7002 <= 0:
            c_7002 = (-a_7002) + 2
        else:
            c_7002 = a_7002