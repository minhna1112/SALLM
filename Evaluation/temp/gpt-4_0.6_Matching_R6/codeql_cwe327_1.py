import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # We will use SHA-256 hashing algorithm to create a hash of the certificate and then compare it with the known hash
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()
    return certificate_hash == known_hash
