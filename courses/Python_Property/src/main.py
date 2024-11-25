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

"""
class Point:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2


point = Point(1, 2)

print(point.point1)
print(point.point2)

point.point1 = 10
point.point2 = 20

print(point.point1)
print(point.point2)
"""

# Using lambda as Get() Method #

"""
class Circle:
    def __init__(self, radius):
        self.radius = radius
    radius = property(lambda self: self.radius)

circle = Circle(40.0)
print(circle.radius) # output: 40.0
"""

## Creating Attributes With property() ##

"""
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def _getradius(self):
        return self.radius

    def _setradius(self, value):
        self.radius = value

    def _delradius(self):
        del self.radius

    radius = property(
        fget=_getradius,
        fset=_setradius,
        fdel=_delradius,
        doc="Radius operations"
    )

circle = Circle(30.0)

print(circle.radius) # output: 30.0

circle.radius = 36.9
print(circle.radius) # output: 36.9

del circle.radius
print(circle.radius) # ERROR
"""

## Using property() as a Decorator ##

"""
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius

circle = Circle(33.0)

print(circle.radius) # output: 30.0

circle.radius = 36.9
print(circle.radius) # output: 36.9

#del circle.radius
#print(circle.radius) # ERROR
"""

"""
## Deciding When to Use Properties ##

In general, you should avoid using properties for attributes that don't require extra functionality or processing. If you do use properties this way, then you'll make your code:

1. Unnecessarily verbose
2. Confusing to other developers
3. Slower than code based on regular attributes
"""

## Providing Read-Only Attributes ##