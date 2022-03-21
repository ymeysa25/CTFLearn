with open('TheMessage.txt', 'r',encoding="utf8") as f:
    data = f.read()

def BinaryToText(binary_string):
    # Convert Our binary to string
    bit = 8
    string_text = ""
    for i in range(0, len(binary_string), bit):
        eigth_bit = binary_string[i : i + bit]

        char = chr(int(eigth_bit, 2))
        string_text += char

    print("\nConvert To String:\n")
    print(string_text)
    return string_text

string_dot_as_one = ""
string_dot_as_zero = ""
for char in data:
    if ord(char) == 32:
        string_dot_as_one += "0"
        string_dot_as_zero += "1"
    else:
        string_dot_as_one += "1"
        string_dot_as_zero += "0"

print(". represents 0 and [space] represents 1\n")
print(string_dot_as_zero)
BinaryToText(string_dot_as_zero)
print("=" * 80)
print(". represents 1 and [space] represents 0\n")
print(string_dot_as_one)
BinaryToText(string_dot_as_one)
