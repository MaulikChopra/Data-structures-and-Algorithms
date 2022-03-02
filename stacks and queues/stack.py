import collections


class stack:
    def __init__(self):
        self.array = collections.deque()

    def push(self, value):
        self.array.append(value)

    def pop(self):
        return self.array.pop()

    def peek(self):
        try:
            return self.array[-1]
        except IndexError:
            pass

    def is_empty(self):
        return len(self.array) == 0

    def size(self):
        return len(self.array)

    def __repr__(self):
        string = 'First->'
        for i in self.array:
            string += str(i) + "->"
        string += "Last"
        return string


if __name__ == "__main__":
    stack = stack()
    for i in range(0, 11):
        stack.push(i)
    print(stack.peek())
    stack.is_empty()
    stack.size()
    print(stack)
    stack.pop()
    print(stack.peek())
    print(stack)
