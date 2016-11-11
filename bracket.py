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


def parChecker(symbolString):
    s = Stack()
    balanced = True
    current = ''
    previous = ''
    result = "YES"
    i = 0
    while i < len(symbolString):
        current = symbolString[i]
        if current == '(' or current == '[':
            s.push(current)
        else:
            if s.isEmpty():
                balanced = False
            else:
                previous = s.peek()
                if (current == ')' and previous == '(') or (current == ']' and previous == '['):
                    s.pop()
                else:
                    balanced = False
        i = i + 1

    if not s.isEmpty():
        balanced = False

    result = "YES" if balanced else "NO"
    return result

                    
with open('brackets.out', 'w') as output:
    with open('brackets.in', 'r') as input:
        for line in input:
            
            output.write(str(parChecker(line.strip())))
            output.write("\n")

