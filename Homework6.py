class Matrix:
    def __init__(self, *args, **kwargs):
        """
                Takes 2 keyword arguments: filename or list. If filename is given
                read the matrix from file. Else, read it directly from list.
                """
        if 'filename' in kwargs:
            self.read_from_file(kwargs['filename'])
        elif 'list' in kwargs:
            self.read_as_list(kwargs['list'])

    def read_as_list(self, matrix_list):
        if len(matrix_list) == 0:
            self._matrix = []
            self._columns = 0
            self._rows = 0
            return

        columns_count_0 = len(matrix_list[0])
        if not all(len(row) == columns_count_0 for row in matrix_list):
            raise ValueError('Got incorrect matrix')

        self._matrix = matrix_list
        self._rows = len(self._matrix)
        self._columns = columns_count_0

    def read_from_file(self, filename):
        with open(filename, 'r') as f:
            matrix_list = f.readlines()
        matrix_list = [list(map(float, row.split())) for row in matrix_list]
        self.read_as_list(matrix_list)

    def write_to_file(self, filename):
        """
        Write the matrix to the given filename.
        TODO: implement
        """

    @property
    def traspose(self):
        """
        Transpose the matrix.
        TODO: implement
        """
        if len(self._matrix) != 0:
            trans_list = [[self._matrix[j][i] for j in range(len(self._matrix))] for i in range(len(self._matrix[0]))]
        else:
            trans_list = []
        s = '---------Traspose---------\n'
        for value in trans_list:
            s += str(value)
            s += '\n'
        s += '--------------------------\n'
        return s

    @property
    def shape(self):
        s = "\n--------------------------\n"
        s += "Shape: " + str(self._rows) + "x" + str(self._columns)
        s += "\n--------------------------\n"
        return s

    def __add__(self, other):
        """
        The `+` operator. Sum two matrices.
        TODO: implement
        """
        add_matrix = []
        if self._columns == other._columns and self._rows == other._rows:
            for i, value1 in enumerate(self._matrix):
                add_matrix.append([])
                for j, value2 in enumerate(value1):
                    add_matrix[i].append(self._matrix[i][j] + other._matrix[i][j])

        s = '---------Traspose---------\n'
        for value in add_matrix:
            s += str(value)
            s += '\n'
        s += '--------------------------\n'
        return s

    def __mul__(self, other):
        """
        The `*` operator. Element-wise matrix multiplication.
        Columns and rows sizes of two matrices should be the same.
        If other is not a matrix (int, float) multiply all elements of the matrix to other.
        TODO: implement
        """
        mul_matrix = []
        if isinstance(other, (int, float)):
            for i, value1 in enumerate(self._matrix):
                mul_matrix.append([])
                for j, value2 in enumerate(value1):
                    mul_matrix[i].append(self._matrix[i][j] * other)
        elif isinstance(other, Matrix):
            if self._columns == other._columns and self._rows == other._rows:
                for i, value1 in enumerate(self._matrix):
                    mul_matrix.append([])
                    for j, value2 in enumerate(value1):
                        mul_matrix[i].append(self._matrix[i][j] * other._matrix[i][j])

        s = '---------Mul_matrix-------\n'
        for value in mul_matrix:
            s += str(value)
            s += '\n'
        s += '--------------------------\n'
        return s

    def __matmul__(self, other):
        """
        The `@` operator. Mathematical matrix multiplication.
        The number of columns in the first matrix must be equal to the number of rows in the second matrix.
        TODO: implement
        """
        other_trans_list = []
        s = '---------Math_Mull------\n'
        if self._columns == other._rows:
            if len(other._matrix) != 0:
                other_trans_list = [[other._matrix[j][i] for j in range(len(other._matrix))] for i in
                                    range(len(other._matrix[0]))]
            print(other_trans_list)
            result = []
            for i in range(self._rows):
                result.append([])
                for j in range(other._columns):
                    tiv = 0
                    for x, value1 in enumerate(self._matrix[i]):
                        tiv += value1 * other_trans_list[j][x]
                    result[i].append(tiv)

            for value in result:
                s += str(value)
                s += '\n'
            s += '--------------------------\n'
            return s
        else:
            raise ValueError("Got incorrect matrix, for Mathmul")

    @property
    def trace(self):
        """
        Find the trace of the matrix.
        TODO: implement
        """
        sum_m = 0
        if self._columns == self._rows:
            for x in range(len(self._matrix)):
                sum_m += self._matrix[x][x]
            s = '---------Trace-------------\n'
            s += str(sum_m)
            s += '\n--------------------------\n'
            return s
        else:
            s = "\n--------------------------\n"
            s += "No Trace!"
            s += "\n--------------------------\n"
            return s

    @property
    def determinant(self):
        """
        Check if the matrix is square, find the determinant.
        TODO: implement
        """

    def __str__(self):

        s = '\n---------MATRIX---------\n'
        for x in self._matrix:
            for y in x:
                s += str(y) + " "
            s += '\n'
        s += '\n'
        s += f'colums = {self._columns}\nrows = {self._rows}'
        s += '\n------------------------\n'
        return s


m1 = Matrix(filename='file.txt')
m2 = Matrix(filename='file1.txt')
# print(m1.traspose)
# print(m1.trace)
# print(m1.shape)
# print(m1)
print(m1 @ m2)
# print(m1 @ m2)
