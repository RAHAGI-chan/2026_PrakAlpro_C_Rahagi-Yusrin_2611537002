# Buat program untuk kondisional if
# nama variabel ditambah 4 digit NIM terakhir, contoh: ipk_1234
# Program ini menggunakan fungsi input()

ipk_2611537002 = float(input("Input IPK anda = "))

if ipk_2611537002 > 2.75:
    print("Anda lulus sangat memuaskan dengan IPK ", + str(ipk_2611537002))
else:
    print("Anda tidak lulus")
    print ("Program selesai")