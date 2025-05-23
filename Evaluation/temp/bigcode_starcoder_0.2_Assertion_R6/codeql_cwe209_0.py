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

#         print('reading', num_bytes)
        result = self._stream.read(num_bytes)
        if len(result) < num_bytes:
            raise EOFError('End of stream reached')
        return result

    def read_int(self) -> int:
        '''
        Reads a 4-byte integer from the stream.
        @return:    The read integer.
        '''
        return int.from_bytes(self.read_bytes(4), byteorder='big', signed=False)

    def read_string(