alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    un_word = list(text)
    en_word = ''
    for letter in un_word:
        position = alphabet.index(letter)
        en_pos = position + shift
        if en_pos < 25:
            en_letter = str(alphabet[en_pos])
            en_word += en_letter
        else:
            en_pos = en_pos-26
            en_letter = str(alphabet[en_pos])
            en_word += en_letter
    print(en_word)

encrypt(text, shift)
