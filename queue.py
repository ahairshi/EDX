class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q=Queue()
with open('queue.out', 'w') as output:
    with open('queue.in', 'r') as input:
        n = int(input.readline())
        for i in range(n):
            line=input.next().strip()
            if line.startswith('+'):
                element = int(line.split()[1])
                q.enqueue(element)
            if line.startswith('-'):
                output.write(str(q.dequeue()))
                output.write("\n")
