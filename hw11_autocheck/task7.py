'''Реализуйте для класса Vector операции сложения и вычитания векторов.
Т.е. переопределите для него математические операторы __add__ и __sub__

Есть два вектора: a с координатами (x1, y1) и b с координатами (x2, y2).

Тогда сложение векторов b + a — это новый вектор с координатами (x2 + x1, y2 + y1).
Вычитание — обратная операция, b - a — это новый вектор с координатами (x2 - x1, y2 - y1)'''


class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        x = self.coordinates.x + vector[0]
        y = self.coordinates.y + vector[1]
        return Vector(Point(x, y))

    def __sub__(self, vector):
        x = self.coordinates.x - vector[0]
        y = self.coordinates.y - vector[1]
        return Vector(Point(x, y))

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"