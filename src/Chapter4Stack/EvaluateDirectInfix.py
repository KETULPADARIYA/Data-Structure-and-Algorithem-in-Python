from src.Chapter4Stack.implementation.Stack import Stack

def evaluate_direct_infix(expression):
    
    pres = {'*':3,'/':3,'+':2,'-':1,'(':1}
    operator_stack = Stack()
    operand_stack = Stack()

    for element in expression:
        if element  in 'QWERTYUIOPASDFGHJKLLZXCXVVBNNM1234567890':
            operand_stack.push(element)
        else:
            if element == ')':
                top_token = operator_stack.pop()
                while top_token != '(':
                    B = operand_stack.pop()
                    A = operand_stack.pop()
                    operand_stack.push(str(eval(A+top_token+B)))
                    print(B,top_token,A)

                    top_token = operator_stack.pop()
            else:
                while ( (not operator_stack.IsEmpty() )and
                    (pres[element]<=pres[operator_stack.top()])):
                    op = operator_stack.pop()
                    B = operand_stack.pop()
                    A = operand_stack.pop()
                    print(B,op,A)
                    operand_stack.push(str(eval(A+op+B)))
                operator_stack.push(element)

    while not operator_stack.IsEmpty():
        op = operator_stack.pop()
        B = operand_stack.pop()
        A = operand_stack.pop()

        operand_stack.push(str(eval(A + op + B)))
        print(B, op, A)

    return int(operand_stack.pop())