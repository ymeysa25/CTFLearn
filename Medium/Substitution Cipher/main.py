import json

with open('Substitution.txt', 'r') as f:
    data = f.read()


# LWNDAB = SUNDAY
# FGXTDZTK = NOVEMBER
# RTETDZTK = DECEMBER

with open('decrypt_dict.json', 'r') as f:
    decrypt_dict = json.load(f)

res = ""
for char in data:
    if char not in decrypt_dict.keys():
        res += char
        continue

    dec_char = decrypt_dict[char]

    if dec_char == '':
        res += char

    else:
        res += dec_char


print("=" * 80)
print(res)