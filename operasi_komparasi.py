# Comparison Operatior
# Like : >, <, <=, >=, ==, !=, is, is not

a = 4
b = 2

# Operator >
print('----- Operator > ------')
hasil = a > 3
print(a, '>', 3, '=', hasil, '\n')

print('----- Operator < ------')
# Operator <
hasil = a < 3
print(a, '<', 3, '=', hasil, '\n')

print('----- Operator >= ------')
# Operator >= 
hasil = b >= 4
print(b, '>=', 4, '=', hasil, '\n')

print('----- Operator <= ------')
# Operator <=
hasil = b <= 4
print(b, '<=', 4, '=', hasil, '\n')

print('----- Operator <= ------')
# Operator ==
hasil = b == 4
print(b, '==', 4, '=', hasil, '\n')
hasil = a == 4
print(a, '==', 4, '=', hasil, '\n')

print('----- Operator is ------')
# Operator is
x = 5 # assignment membuat object
y = 5
print('nilai x =', x, 'id =', hex(id(x)))
print('nilai y =', y, 'id =', hex(id(x)))

hasil = x is y # comparison is equal or not

print('x is y =', hasil)
print('\n')

print('----- Operator is not ------')
# Operator is
x = 5 # assignment membuat object
y = 4
print('nilai x =', x, 'id =', hex(id(x)))
print('nilai y =', y, 'id =', hex(id(x)))

hasil = x is not y # comparison is equal or not

print('x is y =', hasil)






