class Clock:
    # __init__ method is called whenever new time is set
    # object is created.
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    #str method that returns the current state of the clock as a string
    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self.hours, self.minutes, self.seconds)
    #tick method which measures the time in seconds minutes and hours
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
        if self.hours == 24:
            self.hours = 0



