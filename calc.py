import sys
from parse import Parser


def calculate(tree, res):
    '''
    Recursively Calculates the result of the expression
    tree: syntax tree
    res: the result
    return: result of the expression
    '''
    if tree == None:
        return 0
    elif tree.data == None:
        raise Exception("Missing Parameters for function.")
    elif tree.data == 'add':
        # Calculates the result of all child nodes
        for child in tree.children:
            res += calculate(child, 0)
        return res
    elif tree.data == 'multiply':
        # Calculates the result of all child nodes
        for child in tree.children:
            if child == tree.children[0]:
                res = calculate(child, 0)
            else:
                res *= calculate(child, 0)
        return res
    elif tree.data.isdigit():
        return int(tree.data)
    return 0


if __name__ == '__main__':
    if len(sys.argv) == 2:
        p = Parser(sys.argv[1])
        res = None
        try:
            # Parse input into a tree structure
            tree = p.run_parser()
            # Calculate answer
            res = calculate(tree, 0)
        except Exception as e:
            print(e)
        else:
            if res != None:
                print(res)
    else:
        print("Missing Parameter.")
        print("Usage: ./calc.py <s-expression>")
        print("Example: ./calc.py 123")
        print("Example: ./calc.py \"(add 12 12)\"")
