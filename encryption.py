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
        if i % 2:  # odd
            answer.append(str(ord(text[i]) - 96))
        else:
            answer.append(convert_letter(text[i]))

    final = "".join(answer)
    final = final[::-1]  # Flip the final string

    return final


print(encrypt_1("cant read this even if you tried"))
