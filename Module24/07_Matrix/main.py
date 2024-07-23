class Matrix:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.data = [[0 for _ in range(column)] for _ in range(row)]


    def __str__(self):
        output = ""
        for row in self.data:
            output += "\t".join(str(element) for element in row)
            output += "\n"
        return output

    def add(self, matrix2):
        matrix_result = Matrix(self.row, self.column)
        for i in range(self.row):
            for j in range(self.column):
                matrix_result.data[i][j] = self.data[i][j] + matrix2.data[i][j]
        return matrix_result

    def subtract(self, matrix2):
        matrix_result = Matrix(self.row, self.column)
        for i in range(self.row):
            for j in range(self.column):
                matrix_result.data[i][j] = self.data[i][j] - matrix2.data[i][j]
        return matrix_result

    def multiply(self, matrix2):
        matrix_result = Matrix(self.row, matrix2.column)
        for i in range(self.row):
            for j in range(matrix2.column):
                for k in range(self.column):
                    matrix_result.data[i][j] += self.data[i][k] * matrix2.data[k][j]
        return matrix_result

    def transpose(self):
        matrix_result = Matrix(self.column, self.row)
        for i in range(self.row):
            for j in range(self.column):
                matrix_result.data[j][i] = self.data[i][j]
        return matrix_result


m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())
