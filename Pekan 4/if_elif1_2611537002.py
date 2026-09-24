# Buat program untuk kondisional if
# # Nama variabel ditambah 4 digit NIM terakhir, contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_2611537002 = int(input("Masukkan umur anda: "))
sim_2611537002 = input("Apakah anda sudah punya SIM C (y/t): ")

if umur_2611537002 >= 17 and sim_2611537002 == 'y' :
    print("Anda sudah dewasa dan boleh membawa motor")
elif umur_2611537002 >= 17 and sim_2611537002!= 'y' :
    print("Anda sudah dewasa tetapi tidak boleh membawa motor")
elif umur_2611537002 < 17 and sim_2611537002 == 'y' :
    print("Anda belum cukup umur untuk memiliki SIM")
else:
    print("Anda belum cukup umur dan tidak boleh membawa motor")

print ("program selesai")