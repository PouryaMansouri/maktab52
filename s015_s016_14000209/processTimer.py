import datetime
from time import sleep


class ProcessTimer:

    @property
    def elapsed_time(self):
        return self.__exit_time - self.__enter_time

    def __enter__(self):
        self.__enter_time = datetime.datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f">>> Error: {exc_type=} : {exc_val=} : {exc_tb}")
        else:
            self.__exit_time = datetime.datetime.now()
        return True


p_timer = ProcessTimer()
with p_timer:
    # assert 4 > 13
    # s = int("Asdasd")
    a = int("3")
    print("RUN")
    sleep(2)

print(p_timer.elapsed_time)
