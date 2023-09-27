#Author - Sachin Jain
#Date - 14 th May, 2023
#File - calculator.py
#Description- it converts infix expression to postifix, postifx then to Exptree, where evalution takes place
from stack import Stack
from tree import ExpTree

def infix_to_postfix(infix):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    operatorstack = Stack()
    postfixstring = ""
    spacingstring = ""
    for character in infix:
        if character.isdigit() or character == ".":
            spacingstring += character
        else:
            if spacingstring:
                postfixstring += spacingstring + " "
                spacingstring = ""
            if character == "(":
                operatorstack.push(character)
            elif character == ")":
                topgun = operatorstack.pop()
                while topgun != "(":
                    postfixstring += topgun + " "
                    topgun = operatorstack.pop()
            else:
                while not operatorstack.isEmpty() and prec[operatorstack.peek()] >= prec[character]:
                    postfixstring += operatorstack.pop() + " "
                operatorstack.push(character)
    if spacingstring:
        postfixstring += spacingstring + " "
    while not operatorstack.isEmpty():
        postfixstring += operatorstack.pop() + " "
    return postfixstring.strip()



def calculate(infix):
    postfix = infix_to_postfix(infix)
    postfix = postfix.split()
    expression_tree = ExpTree.make_tree(postfix)
    forthewin = ExpTree.evaluate(expression_tree)
    return forthewin

if __name__ == '__main__':
    print("Welcome to Calculator Program!")
    while True:
        ask = input("Please enter your expression here. To quit enter 'quit' or 'q': \n")
        if ask == 'q' or ask == 'quit':
            print("Goodbye!")
            break
        else:
            try:
                if ask == "" or ask.isalpha():
                  continue
                else:
                  print(calculate(ask))
            except KeyError:
                continue








# a driver to test calculate module
if __name__ == '__main__':

    #test infix_to_postfix function

    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'

    # test calculate function

    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0


