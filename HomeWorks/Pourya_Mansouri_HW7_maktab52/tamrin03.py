class BackupOpen():
    def __init__(self, file, mode='r', *args, **kwargs):
        self.__backup_file = self._backup(file)
        self.file = file
        self.mode = mode
        self.args = args
        self.kwargs = kwargs
        self.open_file = open(self.file, mode=self.mode, *self.args, *self.kwargs)

    @staticmethod
    def _backup(file):
        with open(file, mode='r') as reader:
            backup = reader.read()
        return backup

    def __enter__(self):
        return self.open_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:  # When exception Raised!
            self.open_file.close()
            with open(self.file, 'w') as f:
                f.write(self.__backup_file)
            print(f">>> Error: {exc_type=} : {exc_val=} : {self.file}")
        else:
            self.open_file.close()


path = 'test.txt'
print("First file:")
with BackupOpen(path, 'r') as f:
    print(f.read())

print("*****************************")

path2 = 'test2.txt'
count = 0
print("write second file on first file with error:")
with BackupOpen(path2, 'r') as file_for_read:
    with BackupOpen(path, 'w') as file_for_write:
        for _ in file_for_read.readlines():
            print(_, end='')
            assert count < 5, "raise error"
            file_for_write.write(_)
            count += 1
