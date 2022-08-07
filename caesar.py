def encode(plaintext, key):
    start_num = ''
    end_num = ''
    for i in plaintext:
        start_num += i
    for i in (start_num[0:len(start_num)]):
        i = ord(i)
        if 97 <= i <= 122:
            if i + key <= 122:
                end_num += chr(i + key)
            else:
                end_num += chr(i + key - 26)
        elif 65 <= i <= 90:
            if i + key <= 90:
                end_num += chr(i + key)
            else:
                end_num += chr(i + key - 26)
        else:
            end_num += chr(i)
    return end_num


def decode(ciphertext, key):
    start_num = []
    end_num = []
    cipher = ''
    for i in ciphertext:
        start_num.append(ord(i))
    for i in start_num:
        if 97 <= i <= 122:
            if i - key >= 97:
                end_num.append(i - key)
            else:
                end_num.append(i + 26 - key)
        elif 65 <= i <= 90:
            if i - key >= 65:
                end_num.append(i - key)
            else:
                end_num.append(i + 26 - key)
        else:
            end_num.append(i)

    for i in end_num:
        cipher += (chr(i))
    return cipher


print(encode('aaa', 3))
