from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name
        print(f" creating new shape")

    def __str__(self, name):
        return f'you just created a shape named {self.name}'









