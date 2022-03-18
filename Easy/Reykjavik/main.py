from binascii import a2b_hex, unhexlify

#XOR-ed Flag
one = unhexlify("C5D9CACEC7EDFFE8")
two = unhexlify("DD9BE7F4CED2EED0")
three = unhexlify("C5CAC7CEC8E2F4CE")
four = "\xCF\xF4\xD6"

#XOR key
xorKey1 = "\xAB\xAB\xAB\xAB\xAB\xAB\xAB\xAB"
xorKey2 = "\xAB\xAB\xAB"

#Store part 1-4 flag
temp1 = ""
temp2 = ""
temp3 = ""
temp4 = ""

#XOR functions
for x in range(len(one)):
    temp1 += chr((one[x])^ord(xorKey1[x])) # one XOR xorkey1 .. and so on
    temp2 += chr((two[x])^ord(xorKey1[x])) 
    temp3 += chr((three[x])^ord(xorKey1[x]))

for y in range(len(four)):
    temp4 += chr(ord(four[y])^ord(xorKey2[y]))
    print(ord(four[y]), ord(xorKey2[y]))

print(temp1)
print(temp2)
print(temp3)
print(temp4)
flag = temp4+temp3+temp2+temp1

print(temp1 + temp2 + temp3 + temp4)

print(flag[::-1]) #Reverse Print Flag 