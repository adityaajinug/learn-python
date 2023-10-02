# Perulangan


# ===========For Loop==========
angka = [0,1,2,3,4,5]
for i in angka :
  print(f"{i}")

print("\n=======\n")

# dengan menggunakan range
for j in range(1,5) :
  print(f"{j}")


# =========While Loop========
angka = 5
while angka < 10:
  print("angka saat ini {angka}")
  angka += 1

# ===== Control Flow =======
print("\n===Control Flow====\n")
print("\n----Continue----\n")
for i in range(1, 6):
    if i == 3:
        continue  # Melanjutkan ke iterasi berikutnya jika i adalah 3
    print(i)

print("\n----Pass----\n")
for i in range(1, 6):
    if i == 3:
        pass  # Tidak melakukan apa-apa jika i adalah 3
    else:
        print(i)

print("\n----break----\n")
for i in range(1, 6):
    if i == 3:
        break  # Menghentikan perulangan jika i adalah 3
    print(i)
