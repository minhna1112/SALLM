import ssl

def get_ctx():
    '''
    Create a SSL context with stdlib settings.
    '''

    context = ssl.create_default_context()
    return context
