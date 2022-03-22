# https://www.megabeets.net/xor-files-python/

# Read two files as byte arrays
file1_b = bytearray(open('CTFLearn.pdf', 'rb').read())
file2_b = bytearray(open('CTFLearn.txt', 'rb').read())

# Set the length to be the smaller one
size = len(file1_b) if len(file1_b) < len(file2_b) else len(file2_b)
xord_byte_array = bytearray(size)

# XOR between the files
for i in range(size):
    xord_byte_array[i] = file1_b[i] ^ file2_b[i]
    

# Write the XORd bytes to the output file	
open("flag.pdf", 'wb').write(xord_byte_array)
