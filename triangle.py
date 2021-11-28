from targil import shape

class triangle(shape):
    def __init__(self, name,  a, b, c, h_to_b):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c
        self.h_to_b = h_to_b

    def get_area(self):
        return self.b * self.h_to_b / 2.0

    def print_area(self):
        print(f'area= {self.get_area()}')

    def __str__(self):
        return f' Triangle -the base is is {self.b}, the height is {self.h_to_b}, the sides are {self.a} {self.c} the area is {self.get_area}|' + super().__str__()

