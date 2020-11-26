# Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
# обычное (не целочисленное) деление клеток, соответственно.


# В методе деления должно осуществляться округление значения до целого числа.
class Cell:
    def __init__(self, cell):
        self.count_cell = cell

    # Сложение. Объединение двух клеток.
    # При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
    def __add__(self, other):
        self.count_cell = self.count_cell + other.count_cell
        return self.count_cell

    # # Вычитание. Участвуют две клетки.
    # # Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
    # # иначе выводить соответствующее сообщение.
    def __sub__(self, other):
        if (self.count_cell - other.count_cell) > 0:
            self.count_cell = self.count_cell - other.count_cell
            return self.count_cell
        else:
            return '\n================================\nпроизвести вычитание невозможно!' \
                   '\n================================'


    # # Умножение. Создается общая клетка из двух.
    # # Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
    def __mul__(self, other):
        self.count_cell = self.count_cell * other.count_cell
        return self.count_cell
    #
    # # Деление. Создается общая клетка из двух.
    # # Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
    def __truediv__(self, other):
        self.count_cell = (self.count_cell + other.count_cell) // 2
        return self.count_cell
    #
    # # В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
    # # Данный метод позволяет организовать ячейки по рядам.
    # # Метод должен возвращать строку вида *****\n*****\n*****...,
    # # где количество ячеек между \n равно переданному аргументу.
    # # Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
    # # Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
    # # Тогда метод make_order() вернет строку: *****\n*****\n**.
    # # Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
    # # Тогда метод make_order() вернет строку: *****\n*****\n*****.

    def make_order(self, in_row):
        self.in_row = in_row
        __out = []
        z = 0
        for i in range(self.count_cell):
            if z == in_row:
                __out.append('|')  # эта реализация выведет в одну строку разделяя группы символом "|"
                # __out.append('\n')  # эта реализация будет выводить каждую группу с новой строки
                z = 0

            __out.append('*')
            z = z+1
        return "".join(__out)


cell1 = Cell(5)
cell2 = Cell(10)
# Важен порядок действий и порядок элементов операций
# Результат операции принимает первый аргумент.
# Например: A+B где A=1, B=2; в результате A примет значение A=3
print('cell1:', cell1.count_cell, '\ncell2:', cell2.count_cell)
print('сложение равно:', cell1 + cell2)
print('cell1:', cell1.count_cell, '\ncell2:', cell2.count_cell)
print('вычитание равно:', cell2 - cell1)
print('cell1:', cell1.count_cell, '\ncell2:', cell2.count_cell)
print('умножение равно:', cell1 * cell2)
print('cell1:', cell1.count_cell, '\ncell2:', cell2.count_cell)
print('деление равно:', cell1 / cell2)
print('cell1:', cell1.count_cell, '\ncell2:', cell2.count_cell)

print('cell1:', cell1.make_order(3))
print('cell2:', cell2.make_order(5))
