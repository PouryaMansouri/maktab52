class BackupOpen():
    def __init__(self, file, mode='r', *args, **kwargs):
        self.file = file
        self.__backup_file = ''

    def backup(self):
        return self.

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:  # When exception Raised!
            with open(self.file, 'w') as f:
                f.write(self.__backup_file)
            print(f">>> Error: {exc_type=} : {exc_val=}")


path = 'test.txt'

with BackupOpen(path) as f:
    print(f.file.read())
