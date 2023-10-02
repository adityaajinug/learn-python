# Latihan perulangan segitiga

sisi = 8

# menggunakan for loop
count = 1
for i in range(sisi) :
  print("*"*count)
  count += 1

print("=====Menggunakan Perulangan Bersarang=======")
for i in range(1, sisi + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
print("============")

# menggunakan while loop
count = 1
while count <= sisi:
  print("*"*count)
  count += 1


print("=====Membuat segitiga sama sisi=======")
# Contoh jika segitiga sama sisi

for i in range(sisi) :
  for j in range(sisi - i - 1) :
    print("-", end=" ")
  for k in range(2 * i + 1) :
    print("+", end=" ")
  for j in range(sisi - i - 1):
    print("-", end=" ")
  print()
