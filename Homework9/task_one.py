class Triangle:

    def __init__(self, a, b, c):
        self._check_if_exists(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def _check_if_exists(self, a, b, c):
        if a + b <= c:
            raise ValueError(
                'the sum of sides a and b must be greate or equal to side c'
                )

    def is_right_angled(self):
        if self.a**2 + self.b**2 == self.c**2:
            return True
        else:
            return False

    def perimetr(self):
        return self.a + self.b + self.c

    def __eq__(self, other):
        if not isinstance(other, Triangle):
            raise TypeError('Second argument is not Triangle')

        perimetr1 = self.perimetr()
        perimetr2 = other.perimetr()
        return perimetr1 == perimetr2


t1 = Triangle(3, 4, 5)
print(t1.is_right_angled())


try:
    t2 = Triangle(10, 10, 22)
    print(t2)

except ValueError as e:
    print(e)

t3 = Triangle(11, 11, 20)
print(t3.is_right_angled())

print(t1 != t3)

try:
    print(t1 == t3)
except TypeError as e:
    print(e)
