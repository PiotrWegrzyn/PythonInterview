class A:
    x = 1

    def print_x(self):
        print(self.x)


class B(A):
    x = 2

    def print_x(self):
        print(self.x)
        super().print_x()


class C:
    x = 3


class D(B, C):
    def print_x(self):
        super().print_x()


B().print_x()
D().print_x()
