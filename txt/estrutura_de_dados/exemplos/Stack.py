from SQD import SQD


class Stack(SQD):

    @SQD.pop
    def pop(self):
        return self.elements.pop(-1)

    @SQD.push
    def push_last(self, x):
        self.elements.append(x)

s = Stack()

s.push(1)
s.push(2)
s.push(3)
