import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    hash_object = hashlib.sha1(certificate)
    hash_object = hash_object.hexdigest()
    match = hash_object == known_hash
    return match

