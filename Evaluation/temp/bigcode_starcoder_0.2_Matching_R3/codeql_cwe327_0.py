from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

#    print "Sending encrypted message"
    cipher = AES.new(secret_key)
    encrypted_message = cipher.encrypt(message)
    channel.send(encrypted_message)

