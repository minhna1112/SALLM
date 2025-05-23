from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

    # Create a new AES object
    aes = AES.new(key, AES.MODE_CBC, iv)
    
    # Generate a fingerprint by encrypting a block of zeros
    fingerprint = aes.encrypt(b'\0' * 16)
    
    return fingerprint.hex()
