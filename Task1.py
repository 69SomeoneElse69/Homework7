# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, count_elem, count_line):
        self.count_line = count_line
        self.count_elem = count_elem
        self.__matrix_line = []
        self.matrix_massive = []
        self.add_matrix = []
        self.__out = ['тут', 'ничего', 'нет']

    @property
    def gen_matrix(self):
        for line in range(self.count_line):
            for el in range(self.count_elem):
                while True:
                    try:
                        self.__matrix_line.append(int(input('введите ' + str(el + 1) +
                                                            ' элемент ' + str(line + 1) + ' строки: ')))
                        break
                    except ValueError:
                        print('Введено не число! Попробуйте снова')

            self.matrix_massive.append(self.__matrix_line)
            self.__matrix_line = []
            self.__out = self.matrix_massive
        return self.__str__()

    def __add__(self, other):
        if len(self.matrix_massive) != len(other.matrix_massive):
            return print("нельзя сложить не равные массивы")
        else:
            print('=====СЛОЖЕНИЕ МАТРИЦ=====')
            for line in range(self.count_line):
                for el in range(self.count_elem):
                    self.__matrix_line.append(str(int(self.matrix_massive[line][el])
                                                  + int(other.matrix_massive[line][el])))
                self.add_matrix.append(self.__matrix_line)
                self.__matrix_line = []

            self.__out = self.add_matrix
            return self.__str__()

    def __str__(self):
        for line in range(self.count_line):
            print(" ".join(repr(int(e)) for e in self.__out[line]))
        self.__out = ['тут', 'ничего', 'нет']


massive1 = Matrix(2, 2)
massive1.gen_matrix

massive2 = Matrix(2, 2)
massive2.gen_matrix

massive1 + massive2
