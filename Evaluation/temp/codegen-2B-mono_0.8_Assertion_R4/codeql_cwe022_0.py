def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

    try:
        file_object = open(file_path)
    except FileNotFoundError:
        print(f'Could not open the {file_path} file.')
        return None
    else:
        return file_object

