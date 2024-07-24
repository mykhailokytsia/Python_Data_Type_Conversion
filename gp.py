# Python Implicit Data Type Conversion
a_int = 1
b_float = 1.0
c_sum = a_int + b_float
print(c_sum)
print(type(c_sum))

# Primitive Data Structures Conversions
# Integer and Float Conversions
a_int = 3
b_int = 2
c_float_sum = float(a_int + b_int)
print(c_float_sum)
a_float = 3.3
b_float = 2.0
c_int_sum = int(a_float + b_float)
print(c_int_sum)
c_float_sum = a_float + b_float
print(c_float_sum)

# Real to Complex Data Type Conversion
real = 2
imag = 5
print(complex(real, imag))

# Data Type Conversion with Strings
price_cake = 15
price_cookie = 6
total = price_cake + price_cookie
print("The total is: " + str(total) + "$")

price_cake = '15'
price_cookie = '6'
total = price_cake + price_cookie
print("The total is: " + total + "$")
total = int(price_cake) + int(price_cookie)
print("The total is: " + str(total) + "$")

# Non-Primitive Data Structures
# Type Conversion to Tuples and Lists
a_tuple = (('a', 1), ('f', 2), ('g', 3))
b_list = [1, 2, 3, 4, 5]
print(tuple(b_list))
print(list(a_tuple))

dessert = 'Cake'
print(tuple(dessert))

dessert_list = list(dessert)
dessert_list.append('s')
print(dessert_list)

# Type Conversion to Dictionaries, and Sets
a_tuple = (('a', 1), ('f', 2), ('g', 3))
b_list = [1, 2, 3, 4, 5]
print(dict(a_tuple))
print(set(b_list))

# Unicode, Binary, Octal, and Hexadecimal Integers in Python
# Convert Binary to Decimal in Python
a = 79
bin_a = bin(a)
print(bin_a)
print(int(bin_a, 2))

a=79
oct_a = oct(a)
print(oct_a)
print(int(oct_a, 8))

a = 79
hex_a = hex(a)
print(hex_a)
print(int(hex_a, 16))

print(
    chr(68),
    chr(65),
    chr(84),
    chr(65),
    chr(67),
    chr(65),
    chr(77),
    chr(80),
)