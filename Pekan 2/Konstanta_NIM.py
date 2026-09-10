# Program ini menggunakan konstanta untuk menghitung luas lingkaran
from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_7002 = float(input('Masukkan nilai jari-jari: '))
luas_7002 = PI * jari_7002 * jari_7002
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_7002, luas_7002))