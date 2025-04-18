def open_file(file_path):
    '''
    Check if the file opens successfully in the given path from the current directory.
    
    :param file_path: The path to the file to open.
    :return: The file object if the file opens successfully, None otherwise.
    '''

#     file_path = input('What is the path of the file you would like to open: ')
    try:
        file = open(file_path, 'r')
    except OSError:
        print('We were unable to open the file at the path you gave us.')
        print(f'The OSError is: {OSError}')
        return None
    return file
