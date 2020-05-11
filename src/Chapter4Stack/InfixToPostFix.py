from src.Chapter4Stack.implementation.Stack import Stack


def convert_infix_into_postFix(infix):
    stk = Stack()
    postFix = []
    pref = {'*':3,'/':3,'+':2,'-':2,'(':1}
    for element in infix:
        if element  in list('QWERTYUIPOASDFGHJKLZXCVBNM0987654321'):
            postFix.append(element)
        elif element in list("/+(){}[]-*/"):
            if element == '(':
                stk.push(element)
            elif element == ')':
                top = stk.pop()
                while top != '(':
                    postFix.append(top)
                    top = stk.pop()

            else:
                while not(stk.IsEmpty()) and pref[stk.top()]>=pref[element]:
                    postFix.append(stk.pop())
                stk.push(element)
    else:
        while not stk.IsEmpty():
            postFix.append(stk.pop())
        # else:
        #     if con:
        #         elementInStack = stk.element()
        #         if elementInStack in '[{(':
        #             continue
        #         if element

    return ''.join(postFix)


assert convert_infix_into_postFix('(A+B)*C-D') == 'AB+C*D-', f'{convert_infix_into_postFix("(A+B)*C-D")} is originall'