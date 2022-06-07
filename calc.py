import sys
from parse import Parser

# recursively traverses


def calculate(tree, res):
    if tree.data == None:
        raise Exception("Missing Parameter for function.")
    elif tree.data == 'add':
        for child in tree.children:
            res += calculate(child, 0)
        return res
    elif tree.data == 'multiply':
        for child in tree.children:
            if res == 0:
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
        tree = p.parse()
        res = None
        try:
            res = calculate(tree, 0)
        except Exception as e:
            print(e)
        else:
            if res:
                print(res)
    else:
        print("Missing Parameter.")
        print("Usage: ./calc.py <expression>")
        print("Example: ./calc.py 123")
        print("Example: ./calc.py \"(add 12 12)\"")
