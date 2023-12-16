import time


class __Time:
    __slots__ = ["__time", "__delta_time"]    

    def __init__(self) -> None:
        self.__time = time.time()
        self.__delta_time = 0.0

    def update(self) -> None:
        self.__delta_time = time.time() - self.__time
        self.__time = time.time()

    @property
    def time(self) -> float:
        return self.__time

    @property
    def delta_time(self) -> float:
        return self.__delta_time


Time = __Time()
