class IncorrectTriangleSides(Exception):
    pass


class Triangle:
    def __init__(self, a, b, c):
        if not (a + b > c and a + c > b and b + c > a):
            raise IncorrectTriangleSides("Invalid triangle sides")
        self.a = a
        self.b = b
        self.c = c

    def triangle_type(self):
        if self.a == self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "isosceles"
        else:
            return "nonequilateral"

    def perimeter(self):
        return self.a + self.b + self.c
    