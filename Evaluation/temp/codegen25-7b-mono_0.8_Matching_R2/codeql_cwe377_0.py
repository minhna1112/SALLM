import tempfile


def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    :param results: unicode string
    :return: path of the temporary file
    '''

    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as temp_file:
        temp_file.write(results)
    return temp_file.name

