class Vector:
    "Vectors in 3D space"

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self): # return string "Vector(x, y, z)"
        return f'Vector({repr(self.x)}, {repr(self.y)}, {repr(self.z)})'        

    def __eq__(self, other):   # v == w
        return (
            self.x == other.x and
            self.y == other.y and
            self.z == other.z
        )   

    def __ne__(self, other):    # v != w
        return not self == other

    def __add__(self, other):   # v + w
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):   # v - w
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):   # return the dot product (number)
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):     # return the cross product (Vector)
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )   

    def length(self):           # the length of the vector
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __hash__(self):         # we assume that vectors are immutable
        return hash((self.x, self.y, self.z))   # recommended

# Exemplary tests.
import math
v = Vector(3, 4, 5)
w = Vector(6, -2, 0.5)
assert v != w
assert v + w == Vector(9, 2, 5.5)
assert v - w == Vector(-3, 6, 4.5)
assert v * w == 12.5
assert v.cross(w) == Vector(12, 28.5, -30)
assert v.length() == math.sqrt(50)
S = set([v, v, w])
assert len(S) == 2

print("Tests passed")