# Pengecekan kondisi ada if, elif, else

# studi kasus 1
nilai = float(input("Masukkan nilai : "))

if nilai > 85:
    print("Nilai adalah A")
elif nilai >= 80 and nilai < 85:
    print("Nilai adalah AB")
elif nilai >= 70 and nilai < 80:
    print("Nilai adalah B")
elif nilai >= 60 and nilai < 70:
    print("Nilai adalah C")
elif nilai >= 40 and nilai  < 60:
    print("Nilai adalah D")
else:
    print("Nilai adalah E")


# studi kasus 2

angka_1 = float(input("masukkan angka 1 : "))
operator = input("masukkan operator (+, -, /, %, x) : ")
angka_2 = float(input("masukkan angka 2 : "))


if operator == "+" :
  hasil = angka_1 + angka_2
  print(f"hasil dari penjumlahan = {hasil}")
elif operator == "-": 
  hasil = angka_1 - angka_2
  print(f"hasil dari pengurangan = {hasil}")
elif operator == "x": 
  hasil = angka_1 * angka_2
  print(f"hasil dari perkalian = {hasil}")
elif operator == "%": 
  hasil = angka_1 % angka_2
  print(f"hasil dari modulus= {hasil}")

