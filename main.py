message = 'Hello Zaira'
offset = 3

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_message = ''

    for char in message.lower():
        if char == ' ':
            encrypted_message += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_message += alphabet[new_index]
    print('plain message:', message)
    print('encrypted message:', encrypted_message)

caesar(message, offset)