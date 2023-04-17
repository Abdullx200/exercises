from abc import ABC, abstractclassmethod

class A(ABC):
    
    def a(self):
        self.b()
    
    def e(self):
        self.c()

    @abstractclassmethod
    def b(self):
        ...
    
    @abstractclassmethod
    def c(self):
        ...


class B(A):
    def b(self):
        self.a()

    def c(self):
        self.e()


class C(B):
    def f(self):
        pass


class D(A,ABC):
    def b(self):
        self.f()
    @abstractclassmethod
    def f(self):
        ...

class E(D):
    def c(self):
        self.a()

    def f(self):
        self.e()

    def g(self):
        self.f()

class F(ABC):
    def a(self):
        self.b()
        self.f()

    def b(self):
        ...

    @abstractclassmethod
    def f(self):
        ...
