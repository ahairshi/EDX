class QueueMin:
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

    def queueMin(self):
        return min(self.items)

q=QueueMin()
with open('queuemin.out', 'w') as output:
    with open('queuemin.in', 'r') as input:
        n = int(input.readline())
        for i in range(n):
            line=input.next().strip()
            if line.startswith('+'):
                element = int(line.split()[1])
                q.enqueue(element)
            if line.startswith('-'):
                q.dequeue()
            if line.startswith('?'):
                output.write(str(q.queueMin()))
                output.write("\n")
