# manipulasi string


# Concate String (Menggabungkan String)
nama_awal = "aditya"
nama_tengah = "aji"
nama_akhir = "nugroho"

nama_lengkap = nama_awal + " " + nama_tengah + " " + nama_akhir
print("nama lengkap :", nama_lengkap)

# Menghitung Panjang String
panjang = len(nama_lengkap)
print("panjang string dari nama_lengkap :", panjang)

# Operator String (Melakukan pengecekan string karakter yang berada pada string)
a = "a"
status = a in nama_lengkap
print("Apakah ada huruf a di nama_lengkap? :", status)


# mencari index pada string
print("index ke 0 dari nama_lengkap :", nama_lengkap[0])
print("index ke 16 dari nama_lengkap :", nama_lengkap[16])
print("index ke -1 dari nama_lengkap :", nama_lengkap[-1])
print("index ke 0 - 4 dari nama_lengkap :", nama_lengkap[0:4])


# case sensitive
print("Hasil nama lengkap di buat capital :", nama_lengkap.upper())

string_nama = "aDiTYA AJI NUGroho"
print("Hasil nama lengkap di buat kecil :", string_nama.lower())

# case sensitive check
print("Apakah semua karakter string huruf kecil? :", nama_lengkap.islower())
print("Apakah semua karakter string huruf Capital? :", nama_lengkap.isupper())

# case sensitive check isalpha() -> pengecekan semua adalah huruf
# case sensitive check isnum() -> pengecekan semua adalah angka
# case sensitive check isdecimal() -> pengecekan semua adalah angka decimal
# case sensitive check isspace() -> check spasi
# case sensitive check istitle() -> check huruf besar

judul = "Coba Text Ini"
print("Apakah judul is title :", judul.istitle())

# ========== Komponen ==============
# komponen startswith() 
text = "Lagi Coding Python"
print("start =", text.startswith("Lagi"))
# endswith()
text = "Lagi Coding Python"
print("start =", text.endswith("Python"))


# ======= Penggabungan Komponen =========

arr = ['aku', 'lagi', 'coding', 'python']

# join()
text_join = " ".join(arr)
print("Gabungan dari arr :", text_join)

# split()
text_split = text_join.split(text)
print("Split dari text :", text_split)

# alokasi karakter rjust(), ljust(), center(), strip()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")
kiri = "kiri".ljust(5)
print("'"+kiri+"'")
tengah = "tengah".center(25, '-')
print("'"+tengah+"'")
print("'"+tengah.strip('-')+"'")


# ===== Format String ======
# contoh string
nama = "adit"
format_str = f"hello {nama}"
print(format_str)

#contoh angka
angka = 123.12
format_str = f"ini adalah angka {angka}"
print(format_str)

#contoh bilangan bulat
angka = 12312
format_str = f"ini adalah bilangan bulat {angka:d}"
print(format_str)

#contoh untuk harga atau bilangan ordo
angka = 12000000
format_str = f"ini adalah bilangan ordo {angka:,}"
print(format_str)

#contoh untuk bilangan desimal
angka = 2000.43232
format_str = f"ini adalah bilangan desimal {angka:.3f}"
print(format_str)

angka = 432.32
format_str = f"ini adalah bilangan desimal {angka:09.3f}"
print(format_str)

#contoh untuk menampilkan tanda + atau -
angka_minus = -20
format_str = f"ini adalah angka minus {angka_minus:+d}"
print(format_str)

angka_plus = 432.32
format_str = f"ini adalah angka plus {angka_plus:+.3f}"
print(format_str)

# contoh untuk format presentase
persentase = 0.045
format_str = f"ini adalah persentase {persentase:.2%}"
print(format_str)

# contoh untuk dengan operasi aritmatika
harga = 10000
jumlah = 4
format_str = f"Hasil dari harga x jumlah = {harga*jumlah:,}"
print(format_str)

# format binary, octal, hexadecimal

angka = 200
format_binary = f"binary = {bin(angka)}"
format_octal = f" octal = {oct(angka)}"
format_hexadecimal = f"hexadecimal = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hexadecimal)



