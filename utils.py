from math import sqrt


class Vec2:


    @staticmethod
    def to_vec2(arr):
        return Vec2(arr[0], arr[1])

    @staticmethod
    def div(vec, num):
        return Vec2(vec.x / num, vec.y / num)

    @staticmethod
    def mul(vec, num):
        return Vec2(vec.x * num, vec.y * num)


    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x, self.y = x, y

    def normalize(self):
        self.n_div(self.magnitude())

    def normalized(self):
        return Vec2.div(self, self.magnitude())

    def magnitude(self):
        return sqrt(self.sqrmagnitude())

    def sqrmagnitude(self):
        return self.x ** 2 + self.y ** 2

    def n_div(self, num):
        self.x /= num
        self.y /= num

    def n_mul(self, num):
        self.x *= num
        self.y *= num

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vec2(self.x * other.x, self.y * other.y)

    def __div__(self, other):
        return Vec2(self.x / other.x, self.y / other.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"




