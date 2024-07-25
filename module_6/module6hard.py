
class Figure:

    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = self.set_sides(*sides)
        self.__color = list(color)
        self.filled = True

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(i, int) and i > 0 for i in new_sides)

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):

    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * 3.14159) if self.get_sides() else 1

    def get_square(self):
        return 3.14159 * (self.__radius ** 2)

    def set_sides(self, *new_sides):
        if self._Figure__is_valid_sides(*new_sides):
            super().set_sides(*new_sides)
            self.__radius = self.get_sides()[0] / (2 * 3.14159)


class Triangle(Figure):

    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = self.calculate_height()

    def get_square(self):
        s = sum(self.get_sides()) / 2
        return (s * (s - self.get_sides()[0]) * (s - self.get_sides()[1]) * (s - self.get_sides()[2])) ** 0.5


    def calculate_height(self):
        return (2 * self.get_square()) / self.get_sides()[0] if self.get_sides() else 1


class Cube(Figure):

    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        side_length = sides[0] if len(sides) > 0 else 1
        self.set_sides(*[side_length] * self.sides_count)


    def get_volume(self):
        return self.get_sides()[0] ** 3



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
