#Program for balancing symbols into arithmetic -postfix- expression, with Stack implementation
#evaluation is done in a right to left fashion

class Stack():
    def __init__(self):
        self.items = []

    #method for pushing items into the Stack
    def push(self, new_item):
        self.items.append(new_item)

    #method for checking if the Stack is empty
    def is_empty(self):
        return self.items == []

    #method for removing and returning item from the top of the stack
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        print('--Stack is empty--')

    #method that returns the item from the top of the stack
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        print('--Stack is empty--')

    #method to return items as Str
    def __str__(self):
        return str(self.items)

    def post_fix_eval(self):
        operand_stack = Stack()
        #get list of all tokens in given expression

        for token in self.items:
            # if token is a number, push to stack
            if token in '1234567890':
                operand_stack.push(int(token))
                print(operand_stack)
            else:
                # if token is a symbol, pop 2 numbers from the stack,
                # and evaluate them. Then push result back to stack
                op1 = operand_stack.pop()
                op2 = operand_stack.pop()
                result = self.do_math(op1, token, op2)
                operand_stack.push(result)

        return operand_stack.pop()

    #function that takes two operants and an operator and returns the result
    def do_math(self, op1, optr, op2):
        if optr == '+':
            return op1 + op2
        if optr == '-':
            return op1 - op2
        if optr == '*':
            return op1 * op2
        if optr == '/':
            return op1 / op2

new_stack = Stack()
for token in '4396*+-':
    new_stack.push(token)
print(new_stack.__str__())
print(new_stack.post_fix_eval())
