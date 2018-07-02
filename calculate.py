import re

def calculate(operation):
    result = 0
    sumlist = operation.replace('-','+-').split('+')
    for i in sumlist:
        if i == '':
            continue
        else:
            result += mutidiv(i)
    return result


def mutidiv(s):

    if '*' not in s and '//' not in s:
        return int(s)
    elif '*' in s:
        return mutidiv(s.split('*',1)[0]) * mutidiv(s.split('*',1)[1])
    else:
        return mutidiv(s.split('//',1)[0]) // mutidiv(s.split('//',1)[1])



def calculate_(s):
    flag = re.compile('[\+\-\*]|//')
    operands = flag.split(s)
    operators = flag.findall(s)

    for i in range(len(operands)):
        if operands[i] != '':
            operands[i] = int(operands[i])
        else:
            operands[i] = 0

    while(len(operands)>1):    
        if '*' in operators and '//' in operators:
            if operators.index('*') < operators.index('//'):
                operands[operators.index('*')] = operands[operators.index('*')] * operands[operators.index('*') + 1]
                operands.pop(operators.index('*') + 1)
                operators.remove('*')
            else:
                operands[operators.index('//')] = operands[operators.index('//')] // operands[operators.index('//') + 1]
                operands.pop(operators.index('//') + 1)
                operators.remove('//')
        elif '*' in operators and '//' not in operators:
            operands[operators.index('*')] = operands[operators.index('*')] * operands[operators.index('*') + 1]
            operands.pop(operators.index('*') + 1)
            operators.remove('*')
        elif '*' not in operators and '//' in operators:
            operands[operators.index('//')] = operands[operators.index('//')] // operands[operators.index('//') + 1]
            operands.pop(operators.index('//') + 1)
            operators.remove('//')
        else:
            if operators[0] == '+':
                operands[0] += operands[1]
                operands.pop(1)
            else:
                operands[0] -= operands[1]
                operands.pop(1)

    return operands[0]





