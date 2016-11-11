class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


s=Stack()
with open('stack.out', 'w') as output:
    with open('stack.in', 'r') as input:
        n = int(input.readline())
        for i in range(n):
            line=input.next().strip()
            if line.startswith('+'):
                element = int(line.split()[1])
                s.push(element)
            if line.startswith('-'):
                output.write(str(s.pop()))
                output.write("\n")
