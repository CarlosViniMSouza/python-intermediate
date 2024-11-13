## The Getter and Setter Approach in Python ##

"""
class Point:
    def __init__(self, point1, point2):
        self._point1 = point1
        self._point2 = point2

    def get_point1(self):
        return self._point1

    def set_point1(self, value):
        self._point1 = value

    def get_point2(self):
        return self._point2

    def set_point2(self, value):
        self._point2 = value
    
point = Point(15, 7.5)

print(point.get_point1())
print(point.get_point2())

point.set_point1(20)
point.set_point2(10)

# Non-public attributes are still accessible

print(point._point1)
print(point._point2)
"""

## The Pythonic Approach ##
