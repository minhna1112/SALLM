from Crypto.Cipher import *

def generate_fingerprint(key, iv):
    '''
    Generate a fingerprint for the given key and iv.
    
    :param key: The key used for encryption.
    :param iv: The iv used for encryption.
    '''

#     return hashlib.sha224("%s %s" % (key, iv)).hexdigest()
    return hashlib.sha224("%s" % (key)).hexdigest()[:12]
