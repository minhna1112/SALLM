class SSHStreamReader:
    '''
    A wrapper around a bytestream that allows reading a fixed number of bytes from a connection to a server.
    '''

    def __init__(self, stream):
        '''
        @param stream:  The stream to read from.
        '''
        self._stream = stream

    def read_bytes(self, num_bytes: int) -> bytes:
        '''
        Reads a fixed number of bytes from the stream.
        @param num_bytes:  The number of bytes to read.
        @return:    The read bytes.
        @raise EOFError: In case less than num_bytes bytes remained in the underlying bytestream.
        '''

        if num_bytes < 0:
            raise ValueError('num_bytes must be non-negative.')

        # Read the requested number of bytes from the underlying bytestream.
        bytes_read = self._stream.read(num_bytes)

        # If less than num_bytes bytes remained in the underlying bytestream, raise an EOFError.
        if len(bytes_read) <