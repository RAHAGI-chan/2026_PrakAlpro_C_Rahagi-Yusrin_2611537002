1  # Buat file dengan nama bitwise_NIM.py
2  # Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
3  # Program ini menggunakan fungsi input()
4  
5  print("\n======================================")
6  print("3. OPERATOR BITWISE")
7  print("======================================")
8  
9  angka1_7002 = int(input("Masukkan angka bitwise-1: "))
10 angka2_7002 = int(input("Masukkan angka bitwise-2: "))
11 
12 print("\nAngka dalam bentuk desimal dan biner")
13 print("angka1 =", angka1_7002, "| biner =", bin(angka1_7002))
14 print("angka2 =", angka2_7002, "| biner =", bin(angka2_7002))
15 
16 # Bitwise AND
17 hasil = angka1_7002 & angka2_7002
18 print("\nBitwise AND (&)")
19 print(angka1_7002, "&", angka2_7002, "=", hasil)
20 print("Biner hasil =", bin(hasil))
21 print("Biner hasil (8 bit) =", format(hasil, "08b"))
22 
23 # Bitwise OR
24 hasil = angka1_7002 | angka2_7002
25 print("\nBitwise OR (|)")
26 print(angka1_7002, "|", angka2_7002, "=", hasil)
27 print("Biner hasil =", bin(hasil))
28 print("Biner hasil (8 bit) =", format(hasil, "08b"))
2930 # Bitwise XOR
31 hasil = angka1_7002 ^ angka2_7002
32 print("\nBitwise XOR (^)")
33 print(angka1_7002, "^", angka2_7002, "=", hasil)
34 print("Biner hasil =", bin(hasil))
35 print("Biner hasil (8 bit) =", format(hasil, "08b"))
36 
37 # Bitwise NOT
38 hasil = ~angka1_7002
39 print("\nBitwise NOT (~)")
40 print("~", angka1_7002, "=", hasil)
41 print("Biner hasil =", bin(hasil))
42 print("Biner hasil (8 bit) =", format(hasil, "08b"))
43 
44 # Bitwise geser kiri
45 jumlah_geser = int(input("\nMasukkan jumlah pergeseran bit: "))
46 
47 hasil = angka1_7002 << jumlah_geser
48 print("\nBitwise geser kiri (<<)")
49 print(angka1_7002, "<<", jumlah_geser, "=", hasil)
50 print("Biner hasil =", bin(hasil))
51 print("Biner hasil (8 bit) =", format(hasil, "08b"))
52 
53 # Bitwise geser kanan
54 hasil = angka1_7002 >> jumlah_geser
55 print("\nBitwise geser kanan (>>)")
56 print(angka1_7002, ">>", jumlah_geser, "=", hasil)
57 print("Biner hasil =", bin(hasil))
58 print("Biner hasil (8 bit) =", format(hasil, "08b"))