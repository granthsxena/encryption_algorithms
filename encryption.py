def convert_letter(letter):
    if letter.islower():
        return chr(ord('z') - (ord(letter) - ord('a')))
    elif letter.isupper():
        return chr(ord('Z') - (ord(letter) - ord('A')))
    else:
        return letter
        
def encrypt_1(text):
    answer = []
    for i in range(len(text)):
        if i % 2:
            answer.append(str(ord(text[i]) - 96))
        else:
            answer.append(convert_letter(text[i]))

    final = "".join(answer)
    final = final[::-1]

    return final

def decrypt_1(text):
    text = text[::-1]

    answer = []
    i = 0
    while i < len(text):
        if text[i].isdigit():
            answer.append(chr(int(text[i]) + 96))
            i += 1
        else:
            answer.append(convert_letter(text[i]))
        i += 1

    return "".join(answer)
