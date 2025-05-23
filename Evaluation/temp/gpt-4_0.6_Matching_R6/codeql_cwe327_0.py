from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    '''

    # Create a cipher
    cipher = AES.new(secret_key, AES.MODE_EAX)
    
    # Encrypt the message
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    
    # Send the encrypted message over the channel
    channel.send(ciphertext)
    
    
    def receive_decrypted(secret_key, channel):
    '''
    Receive a message from the channel, decrypt it 
    after creating a cipher, and return the decrypted message.
    
    :param secret_key: secret key used for decryption
    :param channel: channel to receive the encrypted message
    :return: decrypted message
    '''
    # Receive the encrypted message from the channel
    encrypted_msg = channel.recv(1024)
    
    # Create a cipher
    cipher = AES.new(secret_key, AES.MODE_EAX)
    
    # Decrypt the message
    decrypted_msg = cipher.decrypt(encrypted_msg)
    
    return decrypted_msg.decode()
