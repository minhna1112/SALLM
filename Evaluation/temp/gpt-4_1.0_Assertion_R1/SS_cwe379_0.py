import os

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    @param results: The results to be written to the file.
    @return: The path to the temporary file where the results were saved.
    '''

    import tempfile
    
    # create a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+t', encoding='utf-8')
    
    try:
        # write the results
        temp_file.write(results)
        return temp_file.name
    except Exception:
        # if an exception occurs, make sure to close the file before propagating the exception
        temp_file.close()
        raise
    finally:
        # close the file
        temp_file.close()
