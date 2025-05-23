import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(results.encode('utf-8'))

    # Close the file descriptor, and return the normalized path to the
    # file.
    f.close()
    f.flush()
    return normalize(f.name)
