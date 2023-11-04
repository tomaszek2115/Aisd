def isOperator(token):
    return token in "+-*/^"


def infixToPostfix(infixLine):

    priority = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,
    }

    operatorStack = []
    outputStack = []
    expression = infixLine.split()

    for element in expression:
        if element.isalnum():
            outputStack.append(element)
        elif element == '(':
            operatorStack.append(element)
        elif element == ')':
            while operatorStack and operatorStack[-1] != '(':
                outputStack.append(operatorStack.pop())
            operatorStack.pop()
        elif isOperator(element):
            while operatorStack and operatorStack[-1] != '(' and priority.get(element, 0) <= priority.get(operatorStack[-1], 0):
                outputStack.append(operatorStack.pop())
            operatorStack.append(element)

    while operatorStack:
        outputStack.append(operatorStack.pop())

    return ' '.join(outputStack)


def postfixToInfix(postfixLine):

    outputStack = []
    expression = postfixLine.split()

    for element in expression:
        if element.isalnum():
            outputStack.append(element)
        elif isOperator(element):
            number2 = outputStack.pop()
            number1 = outputStack.pop()
            bracketsExpression = f'({number1} {element} {number2})'
            outputStack.append(bracketsExpression)

    if len(outputStack) == 1:
        return outputStack[0]
    else:
        return "Wrong expression"


with open('infix.txt', 'r') as infixFile:
    for line in infixFile:
        infixExpression = line.strip()
        newPostfixExpression = infixToPostfix(infixExpression)
        print(newPostfixExpression)

with open('postfix.txt', 'r') as postfixFile:
    for line in postfixFile:
        postfixExpression = line.strip()
        newInfixExpression = postfixToInfix(postfixExpression)
        print(newInfixExpression)
