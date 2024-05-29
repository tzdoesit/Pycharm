# offset cipher

message = "Hello World"
offset = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#caesar cipher
def caesar(message, offset):
    encrypted_message = ''

    for char in message.lower():
        if char == ' ':
            encrypted_message += char
        else:
            index = alphabet.find(char)
            # add modulo (#) here so that if offset makes index over 26, it cuts off the trunk.
            new_index = (index + offset) % len(alphabet)
            encrypted_message += alphabet[new_index]

        print('plain message:', message)
        print('encrypted message:', encrypted_message)

caesar(message, offset)