# operator bitwise

a = 9
b = 5

# bitwise OR (|)

c = a | b
print('\n', 10*"=", "OR", 10*"=")
print('nilai :', a, 'binary :', format(a, '08b'))
print('nilai :', b, 'binary :', format(b, '08b'))

print('---- c = binary a | binary b -----')

print('nilai :', c, 'binary :', format(c, '08b'))

# bitwise AND (&)
c = a & b
print('\n', 10*"=", "AND", 10*"=")
print('nilai :', a, 'binary :', format(a, '08b'))
print('nilai :', b, 'binary :', format(b, '08b'))

print('---- c = binary a & binary b -----')
print('nilai :', c, 'binary :', format(c, '08b'))

# bitwise XOR (^)
c = a ^ b
print('\n', 10*"=", "XOR", 10*"=")
print('nilai :', a, 'binary :', format(a, '08b'))
print('nilai :', b, 'binary :', format(b, '08b'))

print('---- c = binary a ^ binary b -----')
print('nilai :', c, 'binary :', format(c, '08b'))

# bitwise NOT (~)
c = ~a
print('\n', 10*"=", "NOT", 10*"=")
print('nilai :', a, 'binary :', format(a, '08b'))
print('nilai :', b, 'binary :', format(b, '08b'))

print('---- c = ~a -----')
print('nilai :', c, 'binary :', format(c, '08b'))
print('Nilai c:',c,' dalam bntk binary:', format(c & 0xFF, '08b'))
