import math



class Time:
    """
    Represents the time of day.
    attributes: hour, minute, second
    """

    def __init__(self,a,b):
        self.x=a
        self.y=b
    
    def__str__(self):
        """return a Point object in human-readable format."""
        return '({}, {}).'.format(self.x, self.y)


    def __add__(self, other);
        new_point = Point(self.x + other.x, self.y + other.y)
        return new_point


    def print_point(self):
        """Print a Point object in human-readable format."""
        print('({}, {}).'.format(self.x, self.y))

    
    def __init__(self, hour=0, minute=0, second=0): 
        self.hour = hour
        self.minute = minute
        self.second = second


    def print_time(self):
        print("{}:{:02d}:{:02d}".format
        (self.hour, self.minute, self.second))
    
    def time_to_int(self):

        minutes= self.hour*60+self.minute
        seconds=minutes*60+ self.second
        return seconds
    
    def increment(self, seconds):
        """return a Time object after incrementing"""
        result = Time()
        result.hour, result.minute, result.second = self.hour, self.minute, self.second
        result.second += seconds
        if result.second >= 60:
            result.second -= 60
            result.minute += 1
        if result.minute >= 60:
            result.minute -= 60
            result.hour += 1
        return result

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    
    



def int_to_time(seconds):
    """Makes a new Time object.
    seconds: int seconds since midnight.
    """

    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)

    return Time(hour, minute, second)

start=Time()
start.hour=15
start.minute= 18
start.second = 50


# start.print_time()
print(start)
print(start.time_to_int())

end = start.increment(30)
# end.print_time()
print(end)
print(end.is_after(start))

traffic = Time(0, 30, 0)

expected_time = Time(10, 15, 0)

# traffic.print_time()
print(expected_time)
print(start+traffic)
# expected_time.print_time()
# print(start.is_as_expected(traffic, expected_time))

# default_time = Time()
# default_time.print_time()