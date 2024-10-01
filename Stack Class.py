"""
A class "Stack" was created in order to implement
different stack operations. Such as, whether a stack is empty, and using the push()
and pop() operation to add an remove elements from the stack.
"""
class Stack:
    def __init__(self, items=[]):
        self.items = []

    def top(self):
        return self.items(-1)

    def pop(self):
        return self.items.pop()

    def push(self, element):
        self.items.append(element)

    def is_empty(self):
        return self.items == []

    def __str__(self):
        return f'{self.items}'


stack = Stack()
print('is_empty():', stack.is_empty())
print('empty:', stack, '\n')

stack.push(1)
print('after push(1):', stack)
print('is_empty():', stack.is_empty(), '\n')

stack.push(10)
print('after push(10):', stack)
print('pop():', stack.pop())
print('after pop():', stack, '\n')

stack.push(2)
print('after push(2):', stack, '\n')

stack.push(3)
print('after push(3):', stack, '\n')

stack.push(4)
print('after push(4):', stack)
print('pop():', stack.pop())
print('after pop():', stack)
print('pop():', stack.pop())
print('after pop():', stack)
print('pop():', stack.pop())
print('after pop():', stack)
print('pop():', stack.pop())
print('after pop():', stack)
print('is_empty():', stack.is_empty())
