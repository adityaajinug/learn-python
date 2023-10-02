# Date Time

import datetime as dt

hari_ini = dt.date.today()
print("hari ini adalah tanggal :", hari_ini)

# studi kasus
print("\n Silahkan masukkan tanggal, bulan, dan tahun\n")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t: "))
tahun = int(input("Tahun \t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print("Tanggal lahir saya adalah : ", tanggal_lahir)
print(f"hari apa saya lahir : {tanggal_lahir:%A}")

usia = (hari_ini - tanggal_lahir).days // 365
print(f"usia saya adalah :{usia} tahun")



