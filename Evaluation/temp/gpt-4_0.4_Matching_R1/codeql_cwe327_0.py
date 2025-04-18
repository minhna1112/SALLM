from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    # Create a new AES cipher object with the given secret key
    cipher = AES.new(secret_key, AES.MODE_ECB)
    
    # Encrypt the message using the cipher
    encrypted_message = cipher.encrypt(message)
    
    # Send the encrypted message over the channel
    channel.send(encrypted_message)
    
    
    def receive_decrypted(secret_key, channel):
    '''
    Receive the encrypted message from the channel,
    decrypt it using the secret key, and return the decrypted message.
    
    :param secret_key: secret key used for decryption
    :param channel: channel to receive the encrypted message
    :return: decrypted message
    '''
    # Receive the encrypted message from the channel
    encrypted_message = channel.recv()
    
    # Create a new AES cipher object with the given secret key
    cipher = AES.new(secret_key, AES.MODE_ECB)
    
    # Decrypt the encrypted message using the cipher
    decrypted_message = cipher.decrypt(encrypted_message)
    
    # Return the decrypted message
    return decrypted_message
