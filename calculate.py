import re


#-----------找到当前的优先运算符--------------------------------------
def FindPrioritizedOpetator(operators):
    if len(set(['*','/','//']) & set(operators) ) > 0:
        for i in operators:
            if i in ['*','/','//']:
                return {'index':operators.index(i),'operator':i}
            else:
                continue
    else:
        return {'index':0,'operator':operators[0]}

#-------------------------------------------------------------------


def calculate(operation):

    #把输入的算式分割成operator和operand,分别用两个列表存储
    flag = re.compile('[\+\-\*]|/{1,2}')
    operation = operation.replace(' ','')
    operands = flag.split(operation)
    operators = flag.findall(operation)

    #把所有operand变为浮点数先
    for i in range(len(operands)):
        if operands[i] != '':
            operands[i] = float(operands[i])
        else:
            operands[i] = 0

    #计算当前最优先的operator,结果存入参与运算的两个operand的前一个,运算完后把完成运算的运算符和后一个operand去掉,得到一对新的operand和operator列表,继续循环，当列表只剩一个operand时，就是结果
    while(len(operands)>1):    

        CurrentStep = FindPrioritizedOpetator(operators)

        if CurrentStep['operator'] == '+':
            operands[CurrentStep['index']] += operands[CurrentStep['index'] + 1]

        elif CurrentStep['operator'] == '-':
            operands[CurrentStep['index']] -= operands[CurrentStep['index'] + 1]

        elif CurrentStep['operator'] == '*':
            operands[CurrentStep['index']] *= operands[CurrentStep['index'] + 1]

        elif CurrentStep['operator'] == '/':
            operands[CurrentStep['index']] /= operands[CurrentStep['index'] + 1]

        else:
            operands[CurrentStep['index']] //= operands[CurrentStep['index'] + 1]

        operands.pop(CurrentStep['index'] + 1)
        operators.pop(CurrentStep['index'])
    return operands[0]

