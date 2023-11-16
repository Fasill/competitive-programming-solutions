# # s = []
# #
# # s.append('https://edition.cnn.com/')
# # s.append('https://edition.cnn.com/india')
# # s.append('https://edition.cnn.com/world')
# # s.append('https://edition.cnn.com/china')
#
from collections import deque
#
# stack = deque()
# dir(stack)
# stack.append('https://edition.cnn.com/')
#
# stack.append('https://edition.cnn.com/world')
# stack.append('https://edition.cnn.com/china')
# stack.append('https://edition.cnn.com/ethiopia')
# print(stack.pop())
#
class Stack:
    def __init__(self):
        self.container = deque()

        def push(self,val):
            self.container.append(val)

        def pop(self):
            return self.container.pop()

        def peek(self):
            return self.container[-1]

        def size(self):
            return len(self.container)
s = Stack()
s.push("fasil")
print(s.peek())