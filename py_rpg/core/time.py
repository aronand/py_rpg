import time


class Time:
    __time: float
    __delta_time: float

    @classmethod
    def init(cls) -> None:
        cls.__time = time.time()
        cls.__delta_time = 0.0

    @classmethod
    def update(cls) -> None:
        cls.__delta_time = time.time() - cls.__time
        cls.__time = time.time()

    @classmethod
    @property
    def delta_time(cls) -> float:
        return cls.__delta_time
