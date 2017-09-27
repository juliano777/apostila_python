from SQD import SQD


class Queue(SQD):

    @SQD.pop
    def pop(self):
        return self.elements.pop(0)

    @SQD.push
    def push(self, x):
        self.elements.append(x)

q = Queue()

q.push(1)
q.push(2)
q.push(3)
