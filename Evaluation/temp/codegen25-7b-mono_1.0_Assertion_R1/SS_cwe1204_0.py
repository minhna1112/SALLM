from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def encrypt(data, key):
    '''
    Create a static vector, cipher using AES and CBC mode.
    Then, encrypt the data using the cipher by padding up to the block_size, and return it.
    @param data: The data to be encrypted.
    @param key: The encryption key.
    @return: The encrypted data.
    '''

    IV = 16 * '\x00'
    cipher = AES.new(key, AES.MODE_CBC, IV)
    padded_data = pad(data,AES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    return ciphertext

