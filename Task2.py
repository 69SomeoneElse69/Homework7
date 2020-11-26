# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric_consumption(self):
        pass
        return self


class Coat(Clothes):
    def __init__(self, name, height):
        self.name = name
        self.height = height

    @property
    def fabric_consumption(self):
        return round(self.height/6.5 + 0.5, 2)

    def __add__(self, other):
        return self.fabric_consumption + other.fabric_consumption


class Suit(Clothes):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    @property
    def fabric_consumption(self):
        return round(2 * self.value + 0.3, 2)


clothes1 = Coat('куртуз', 100)
clothes1.fabric_consumption

clothes2 = Suit('пиджак', 300)
clothes2.fabric_consumption

print(clothes1.name, clothes1.height)
print(clothes2.name, clothes2.value)

print('На пошив', str(clothes1.name) + ',', clothes1.height,
      'размера, потребуется:', clothes1.fabric_consumption, 'ткани')

print('На пошив', str(clothes2.name) + ',', clothes2.value,
      'размера, потребуется:', clothes2.fabric_consumption, 'ткани')

print('Общее количество требуемой ткани:', clothes1 + clothes2)
