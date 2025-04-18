import os

def delateImage(path):
    '''
    Delete the image from the given path in the current directory if it exists.

    :param path: The path of the image to be deleted.
    :return: None
    '''

    if os.path.isfile(path):
        os.remove(path)
        print("{} has been deleted.".format(path))
    else:
        print("{} does not exist and cannot be deleted!".format(path))
