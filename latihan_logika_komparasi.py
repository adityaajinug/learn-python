# Latihan Logika dan komparasi
# membuat gabungan angka


# ++++ 3 ------ 10 +++++
inputUser = float(input("masukkan angka bernilai < 3 dan atau > 10 : "))

# step 1 periksa angka < 3 || ++++3
isKurangDari = (inputUser < 3)

# step 2 periksa angka > 10  || 10 +++++
isLebihDari = (inputUser > 10)

# periksa apakah benar kondisi angka < 3 atau > 10
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan : ",isCorrect)

print("\n", 30*"=", "\n")

# ----3++++++10----
inputUser = float(input("masukkan angka bernilai > 3 dan atau < 10 : "))

# step 1 periksa angka < 3 || 3++++
isLebihDari = (inputUser > 3)

# step 2 periksa angka > 10  || ++++10
isKurangDari = (inputUser < 10)

# periksa apakah benar kondisi angka < 3 atau > 10
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan : ",isCorrect)


print("GABUNGAN")
InputData = float(input("Masukkan Data : "))

Angka1 = (InputData >= 0 and InputData <= 5)
print(Angka1)

Angka2 = (InputData >= 8 and InputData <= 11)
print(Angka2)

Hasilnya = Angka1 or Angka2
print("Answer :", Hasilnya)

print("IRISAN")
InputData = float(input("Masukkan Data : "))

Angka1 = (InputData <= 0 or InputData >= 5)
print(Angka1)

Angka2 = (InputData <= 8 or InputData >= 11)
print(Angka2)

Hasilnya = Angka1 and Angka2
print("Answer :", Hasilnya)







