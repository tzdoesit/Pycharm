#offset cipher using Caesar cipher

def caesar(message, offset):
    encrypted_message = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in message.lower(): #lower cases message
        if char == ' ':
            encrypted_message += char #if character is a space, just add it to encrypted message as well

        else: #main logic goes here
