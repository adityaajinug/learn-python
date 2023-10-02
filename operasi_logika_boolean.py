# operasi logika atau boolean

# not, or, xor

print('--- NOT ---')
# NOT
a = True
c = not a
print('data boolean =', a)
print('-----NOT')
print('data c =', c)
print('\n')


print('--- OR ---')
# OR
a = False
b  = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b  = True
c = a or b
print(a, 'OR', b, '=', c)
a = True
b  = False
c = a or b
print(a, 'OR', b, '=', c)
a = True
b  = True
c = a or b
print(a, 'OR', b, '=', c)
print('\n')

print('--- AND ---')
# AND
a = False
b  = False
c = a and b
print(a, 'AND', b, '=', c)
a = False
b  = True
c = a and b
print(a, 'AND', b, '=', c)
a = True
b  = False
c = a and b
print(a, 'AND', b, '=', c)
a = True
b  = True
c = a and b
print(a, 'AND', b, '=', c)
print('\n')

print('--- XOR ---')
# XOR akan true jika salah satu true
a = False
b  = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b  = True
c = a ^ b
print(a, 'XOR', b, '=', c)
a = True
b  = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = True
b  = True
c = a ^ b
print(a, 'XOR', b, '=', c)
print('\n')