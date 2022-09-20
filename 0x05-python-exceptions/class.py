#!/usr/bin/python3
class Robot:
    pop = 0

    def __init__(self, name, age):
        self.name = name
        self.age= age
        Robot.pop += 1

    def die(self):
        print("{} is being destroyed!".format(self.name))

        Robot.pop -= 1

        if Robot.pop == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.pop))


    @property
    def x(self):
        return (self.name, self.age)

    @x.setter
    def x(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("Greetings {} and my age is {:d}.".format(self.name, self.age))

    @classmethod
    def how_many(cls):
        print("We have {:d} robots.".format(cls.pop))


droid1 = Robot("R2-D2", 123)
droid1.say_hi()
Robot.how_many()

droid1.age = 1111
droid1.name = "R2-43"
droid1.say_hi()
droid2 = Robot("C-3PO", 1535)
droid2.say_hi()
Robot.how_many()

droid1.die()
droid2.die()

Robot.how_many()
print (droid1.x)
