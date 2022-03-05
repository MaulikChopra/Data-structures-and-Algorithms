import collections

"""
The linked list of queue is reversed compared to stack.
We use appendleft instead of append in stack.
So that pop removes the first element unlink stack.
"""


class queue:
    def __init__(self):
        self.array = collections.deque()

    def enqueue(self, value):
        self.array.appendleft(value)

    def dequeue(self):
        return self.array.pop()

    def is_empty(self):
        return len(self.array) == 0

    def size(self):
        return len(self.array)

    def __repr__(self):
        string = 'Last->'
        for i in self.array:
            string += str(i) + "->"
        string += "First"
        return string


if __name__ == "__main__":
    q = queue()
    for i in range(0, 11):
        q.enqueue(i)
    print(q)
    q.dequeue()
    print(q)
    print(q.size())
