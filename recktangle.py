from targil import shape

class recktangle(shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def print_area(self):
        print(f'area= {self.width * self.height}')

    def __str__(self):
        return f' Rectangle -the width is {self.width}, the height is {self.height} |' + super().__str__()

