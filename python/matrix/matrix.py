class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [[int(x) for x in row.split()]
                       for row in matrix_string.splitlines()
                       ]
        self.columns = [[row[i] for row in self.matrix]
                        for i in range(len(self.matrix[0]))
                        ]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return self.columns[index-1]
