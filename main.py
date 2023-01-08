class Matrix:
    def __init__(self):
        self.map = {}

    def set(self):
        self.map[(1, 1)] = 3
        self.map[(2, 2)] = 4

    def read(self, fileName):

        file = open(fileName, 'r')

        for line in file:

            a = line.split()
            self.map[(a[0], a[1])] = a[2]

    def write(self, fileName):

        with open(fileName, 'a') as file:
            for i, j in self.map.items():
                file.write(f"{i[0]} {i[1]} {j}\n")

    def printed(self):
        for i, k in self.map.items():
            print(i, k)


class Vector:
    def __init__(self):
        self.map = {}

    def set(self):
        self.map[1] = 3
        self.map[2] = 4

    def read(self, fileName):
        file = open(fileName, 'r')

        for line in file:
            a = line.split()
            self.map[a[0]] = a[1]

    def printed(self):
        for i, k in self.map.items():
            print(i, k)


def mul(A: Matrix , b: Vector):
    v = Vector()

    for i in b.map:
        print(i)



A = Matrix()
A.read("Matrix.txt")
# A.printed()
A.write("Write.txt")
b = Vector()
b.read("b.txt")
# b.printed()

mul(A,b)