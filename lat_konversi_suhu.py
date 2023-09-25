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


# konversi fahrenheit ke kelvin
temperatur_kelvin = ((5/9) * fahrenheit - 32) + 273
print("suhu fahrenheit ke kelvin : ", temperatur_kelvin, "K")

print("\nProgram Konversi Temperatur\n")

kelvin = float(input("Masukkan suhu dalam Kelvin: "))
print("Suhu Kelvin: ", kelvin, "K")

# Konversi ke Fahrenheit
fahrenheit = (kelvin - 273) * 9/5 + 32
print("Suhu Fahrenheit: ", fahrenheit, "F")


