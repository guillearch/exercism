class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [[int(x) for x in row.split()]
                       for row in matrix_string.splitlines()
                       ]
        self.columns = [list(column) for column in zip(*self.matrix)]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return self.columns[index-1]
