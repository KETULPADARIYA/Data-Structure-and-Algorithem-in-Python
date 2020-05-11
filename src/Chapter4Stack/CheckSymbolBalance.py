from src.Chapter4Stack.implementation.Stack import Stack


def check_symbol_balance(array):
    stk = Stack()
    symbols_dictionary = {'(':')','[':']','{':'}'}
    for element in array:
        if element in ['[','{','(']:
            stk.push(element)
        elif element in [']','}',')']:
            if not stk.stack:
                return False
            if symbols_dictionary.get(stk.pop()) != element:
                return False

    else:
         return False if stk.stack else True

if __name__ =='__main__':
    print(check_symbol_balance('(A+B)+(C+D)'))