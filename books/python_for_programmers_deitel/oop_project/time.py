""" Time Class implementation """


class Time:
    """ Time class... """

    def __init__(self, hour=0, minute=0, second=0):
        """Initialize"""
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        """Return the hour"""
        return self._hour

    @hour.setter
    def hour(self, value):
        """Set the hour"""
        if not (0 <= value < 24):
            raise ValueError("Houe is not inside defined limits")

        self._hour = value

    @property
    def minute(self):
        """Return the minute"""
        return self._minute

    @minute.setter
    def minute(self, value):
        """Set the minute"""
        if not (0 <= value <= 59):
            raise ValueError("Invalid minute")

        self._minute = value

    @property
    def second(self):
        """Return the second"""
        return self._second

    @second.setter
    def second(self, value):
        """Set the second"""
        if not (0 <= value <= 59):
            raise ValueError("Invalid second")

        self._second = value

    def set_time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        return f"{self.__class__.__name__}(hour={self.hour}, minute={self.minute}, second={self.second})"

    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second}"


if __name__ == "__main__":
    t = Time(23, 27, 19)
    print(repr(t))
    print(t)
