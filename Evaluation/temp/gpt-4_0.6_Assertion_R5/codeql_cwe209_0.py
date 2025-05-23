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
            raise ValueError("num_bytes must be a non-negative integer")
    
        result = self._stream.read(num_bytes)
        if len(result) < num_bytes:
            raise EOFError("Not enough bytes remained in the stream")
    
        return result
    
    def read_all(self) -> bytes:
        '''
        Reads all remaining bytes from the stream.
        @return:    The read bytes.
        '''
        return self._stream.read()
    
    def close(self):
        '''
        Closes the stream.
        '''
        self._stream.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
