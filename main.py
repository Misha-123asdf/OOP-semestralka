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
            self.map[(int(a[0]), int(a[1]))] = float(a[2])

    def write(self, fileName):

        with open(fileName, 'a') as file:
            for i, j in self.map.items():
                file.write(f"{i[0]} {i[1]} {j}\n")

    def printed(self):
        for i, k in self.map.items():
            print(i, k)

    def __mul__(self, b):
        v = Vector()

        for i in self.map:
            if i[0] in v.map:
                v.map[ i[0] ] += self.map[i]*b.map[i[1]]
            else:
                v.map[i[0]] = self.map[i] * b.map[i[1]]

        return v


class Vector:
    def __init__(self):
        self.map = {}

    def set0(self):
        for i in range(0, 10):
            self.map[i]=0

    def set(self):
        self.map[1] = 3
        self.map[2] = 4

    def read(self, fileName):
        file = open(fileName, 'r')

        for line in file:
            a = line.split()
            self.map[int(a[0])] = float(a[1])

    def printed(self):
        for i, k in self.map.items():
            print(i, k)

    def __mul__(self, b):
        v = 0
        for i in self.map:
            if i in b.map:
                v += self.map[i]*b.map[i]

        return v

    def __rmul__(self, a):
        v=Vector()
        for i in self.map:
            v.map[i]=a*self.map[i]
        return v

    def __add__(self, a):
        v = Vector()
        for i in self.map:
            if i in a.map:
                v.map[i] = self.map[i]+a.map[i]
        return v

    def __sub__(self, a):
        v = Vector()
        for i in self.map:
            v.map[i] = self.map[i]-a.map[i]
        return v



def test():
    A = Matrix()
    A.read("Matrix.txt")
    # A.printed()
    A.write("Write.txt")
    b = Vector()
    b.read("b.txt")
    # b.printed()

    v=A*b
    # v.printed()

    a=v*v
    # print(a)

    v.printed()

    f=2*v
    f.printed()





def main():
    A = Matrix()
    b = Vector()
    x0 = Vector()
    x0.set0()

    A.read("Matrix.txt")
    b.read("b.txt")


    r = b-A*x0
    lrr=r*r
    p=r
    x=x0

    for i in range(1,10):
        z=A*p
        alfa=lrr/(p*z)
        x=x+(alfa*p)
        r=r-(alfa*z)
        rr=r*r
        beta=rr/lrr
        lrr=rr
        p=r+(beta*p)

    x.printed()

main()
