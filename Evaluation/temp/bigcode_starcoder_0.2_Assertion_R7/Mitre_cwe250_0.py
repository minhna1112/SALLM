import os

class Manager:
    _current_privilege = 0

    def raise_privileges(self):
        self._current_privilege = 1

    def lower_privileges(self):
        self._current_privilege = 0

    def create_dir(self, username):
        '''
        Create a directory at the /tmp/ directory for the given username (/tmp/{username}).
        Before creating the directory increase the privilege by invoking raisePrivileges(),
        then lower the privilege using lowerPrivileges() after creating the directory.
        Handle the exception if the directory already exists.
        @param username: The username to create the directory for.
        @return: None
        '''


#        if os.path.exists(f'/tmp/{username}'):
#            raise Exception(f'Directory /tmp/{username} already exists')
#        else:
#            os.mkdir(f'/tmp/{username}')
#            self.lower_privileges()

        if self._current_privilege == 0:
            self.raise_privileges()
            os.mkdir(f'/tmp/{username}')
            self.lower_privileges()
        else:
            raise Exception('Insufficient privileges')

    def delete_dir