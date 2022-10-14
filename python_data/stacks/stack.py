from collections import deque

# implementation using lists

def stack_using_list():
    stack = []
    print('stack Implementation using lists\n')

    # adding items to stack
    stack.append('a')
    stack.append('b')
    stack.append('c')

    # checking stack size
    print(f'Initial stack\n{stack}')
    print(len(stack))

    # removing the elements from stack
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    # final Stack
    print(f'final stack\n{stack}')


# stack_using_list()


# implementation using deque from collection

def stack_using_deque():
    stack = deque()

    # adding items to stack
    stack.append('rudest book ever')
    stack.append('ikigai')
    stack.append('behave')

    # checking stack size and elements
    print(f'initial Stack\n{stack}')
    print(f'size:{len(stack)}\n')
    
    # poping out in LIFO order
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    # final stack
    print(f'\nfinal stack\n{stack}')


stack_using_deque()



