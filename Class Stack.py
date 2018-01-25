class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def empty(self):
        if self.size == 0:
            return True
        else:
            return False
        
    def push(self,d):
        self.stack.append(d)
        self.size += 1

    def pop(self):
        x = self.stack[-1]
        self.size -= 1
        del self.stack[-1]
        return x

    def get_size(self):
        return self.size
    
s = Stack()
print s.empty()
print s.get_size()
s.push(1)
s.push(2)
print s.pop()
print s.get_size()
print s.pop()
print s.get_size()
