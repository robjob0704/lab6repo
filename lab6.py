

encode_dict = {"1": "4", "2": "5", "3": "6", "4": "7", "5": "8", "6": "9", "7": "0", "8": "1", "9": "2", "0": "3"}
decode_dict = {"4": "1", "5": "2", "6": "3", "7": "4", "8": "5", "9": "6", "0": "7", "1": "8", "2": "9", "3": "0"}

result = ""

complete = False

def decode(encoded_password):
    decoded_password = ""
    for char in encoded_password:
        if char in decode_dict:
            decoded_password += decode_dict[char]
        else:
            decoded_password += char
    return decoded_password
while not complete:

    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")
    sel = int(input("Please enter an option: "))

    if sel == 1:
        enc_pass = input("Please enter your password to encode: ")
        for char in enc_pass:
            result += encode_dict[char]
        print("Your password has been encoded and stored!\n")
    if sel == 2:
        original_password = decode(result)
        print(f"The encoded password is {result}, and the original password is {original_password}.\n")
        result = ''
    if sel == 3:
        complete = True
