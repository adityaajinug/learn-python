# Konversi suhu

print("\n Program Konversi Temperatur\n")

celcius = float(input("Masukkan suhu dalam celcius: "))
print("suhu celcius : ", celcius, "C")

# konversi reamur
reamur = (4/5) * celcius
print("suhu reamur : ", reamur, "R")

# konversi fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu fahrenheit : ", fahrenheit, "F")

# konversi Kelvin
kelvin = celcius + 273
print("suhu kelvin : ", kelvin, "K")


