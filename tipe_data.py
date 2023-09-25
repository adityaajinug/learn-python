#check type data

# integer
data_1 = 1
print("type data :", type(data_1))

# float

data_float  = 1.5
print("type data :", type(data_float))


#string
string = "test variable"

print("type data :", type(string))


# boolean
data_boolean = True
print("type data :", type(data_boolean))

# tipe data khusus
data_complex = complex(5,6)
print("data complex :", data_complex)
print("type data :", type(data_complex))

# tipe data dari bahasa C

from ctypes import c_double, c_char, c_long

data_c_double = c_double(10.5)

print("data double :", data_c_double)
print("type data :", type(data_c_double))
