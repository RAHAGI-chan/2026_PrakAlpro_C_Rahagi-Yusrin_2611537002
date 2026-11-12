# Data Mahasiswa
name_input = "siti aisyah"  # Disimpan dalam huruf kecil sesuai instruksi
nim = "2610511023"
username = "siti023"

# Format data sesuai ketentuan
name = name_input.title()  # Mengubah ke format Title Case (Siti Aisyah)
intake = nim[:4]           # Mengambil tahun masuk dari NIM menggunakan slicing (2 digit tahun + 2 digit prodi/fakultas, misal '2610' atau disesuaikan dengan aturan kampus)

# Lebar kartu total 30 karakter
border = "=" * 30

print(border)
print("STUDENT CARD".center(30))  # Judul diletakkan di tengah dengan lebar 30
print(border)
print(f"{'Name':<10} : {name}")
print(f"{'NIM':<10} : {nim}")
print(f"{'Username':<10} : {username}")
print(f"{'Intake':<10} : {intake}")
print(border)

def check_palindrome(sentence):
    # Mengubah ke huruf kecil dan menghapus spasi
    cleaned = sentence.lower().replace(" ", "")
    
    # Membandingkan string dengan kebalikannya ([::-1])
    if cleaned == cleaned[::-1]:
        return "Palindrome"
    else:
        return "Not a palindrome"

# Pengujian dengan contoh soal
sentence_1 = "Kasur ini rusak"
sentence_2 = "Algoritma"
custom_sentence = "Kupu kupu"  # Contoh kalimat sendiri

print(f'Sentence: "{sentence_1}" -> Output: {check_palindrome(sentence_1)}')
print(f'Sentence: "{sentence_2}" -> Output: {check_palindrome(sentence_2)}')
print(f'Sentence: "{custom_sentence}" -> Output: {check_palindrome(custom_sentence)}')