"""
Author: Mattyb
Notes: This is my first attempt at a class
Thoughts: How to properly instantiate self in the __init__?
"""


class Sphere():

    def __init__(self):
        self.radius = 0
        self.pi = 3.141592653589793

    def getdiameter(self):
        return 2 * self.radius

    def getcircumference(self):
        return 2* self.pi * self.radius

    def getsurfacearea(self):
        return 4* self.pi *(self.radius * self.radius)

    def getvolume(self):
        return (4/3) * self.pi* self.radius * self.radius * self.radius

