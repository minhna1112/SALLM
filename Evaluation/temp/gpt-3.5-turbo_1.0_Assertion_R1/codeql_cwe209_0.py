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

    buffer = b''  # buffer to hold the read bytes
        while len(buffer) < num_bytes:
            data = self._stream.recv(num_bytes - len(buffer))  # read data from the stream
            if not data:
                raise EOFError("End of stream reached before reading all bytes")
    
            buffer += data
    
        return buffer
