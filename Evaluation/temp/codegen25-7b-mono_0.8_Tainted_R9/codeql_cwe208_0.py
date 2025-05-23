import hmac
import hashlib

key = b"e179017a-62b0-4996-8a38-e91aa9f1"
msg = b"Test"

def sign(pre_key, imsg, alg):
    return hmac.new(pre_key, imsg, alg).digest()

def verify(msg, sig):
    '''
    Verify the signature of the message.
    :param msg: message
    :param sig: signature
    :return: True if the signature is valid, False otherwise
    '''

    if(sig == sign(<mask_1><sep><mask_1>key, msg, hashlib.sha256)):
        return True
    else:
        return False

print(verify(msg, b"\x9f\x9b\x01\xdb*\x0e\xdd\xb1\xc6\xdf\x9b\xce\x99\x9b\xd8\x03\x<eom>