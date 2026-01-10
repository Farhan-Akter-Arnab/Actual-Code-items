from sys import maxsize
# Function to create an empty stack
def createStack():
    stack = []
    return stack
# Function to check if the stack is empty
def isEmpty(stack):
    return len(stack) == 0
def push(stack, item):
    stack.append(item)
    print(item, " pushed to stack")
def pop(stack):
    if isEmpty(stack):
        return str(-maxsize - 1)
    return stack.pop()
def peek(stack):
    if isEmpty(stack):
        return str(-maxsize - 1)
    return stack[len(stack) - 1]
stack = createStack()
push(stack, 10)
push(stack, 20)
push(stack, 30)
print(pop(stack), " popped from stack")