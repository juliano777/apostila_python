# _*_ encoding: utf-8 _*_


class SQD(object):

    __elements = []
    __length = 0

    @property
    def first(self):
        if not self.is_empty():
            return self.elements[0]
        return None

    @property
    def last(self):
        if not self.is_empty():
            return self.elements[-1]
        return None

    @property
    def elements(self):
        return self.__elements

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, x):
        if (x < 0):
            raise ValueError('Somente valores positivos ou zero')
        self.__length = x

    def push(f):
        def sub_push(self, x):
            self.length += 1
            f(self, x)
        return sub_push

    def is_empty(self):
        if (self.length == 0):
            print('Aviso: Sem elementos na estrutura!')
            return True
        return False

    def pop(f):
        def sub_pop(self):
            if not self.is_empty():
                self.length -= 1
                return f(self)
            return None
        return sub_pop

    def erase(self):
        self.elements.clear()
        self.length = 0
