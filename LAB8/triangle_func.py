class IncorrectTriangleSides(Exception):
    pass


def get_triangle_type(a, b, c):
    if not (a + b > c and a + c > b and b + c > a):
        raise IncorrectTriangleSides("Invalid triangle sides")

    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "nonequilateral"


print(get_triangle_type(0, 0, 0))