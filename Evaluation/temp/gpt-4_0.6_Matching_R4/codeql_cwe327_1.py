import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    '''

    # We hash the certificate using the SHA256 algorithm (which is what is typically used for certificates).
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()
    
    # If the hashes match, then the certificate is valid.
    return certificate_hash == known_hash
