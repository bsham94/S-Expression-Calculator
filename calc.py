import sys
from parse import Parser


def calculate(tree):
    if not tree:
        return
    else:
        if tree.data == None:
            raise Exception("Missing Parameter for function.")
        elif tree.data == 'add':
            return calculate(tree.left) + calculate(tree.right)
        elif tree.data == 'multiply':
            return calculate(tree.left) * calculate(tree.right)
        elif tree.data.isdigit():
            return int(tree.data)
    return 0


if __name__ == '__main__':
    if len(sys.argv) == 2:
        p = Parser(sys.argv[1])
        tree = p.parse()
        res = None
        try:
            res = calculate(tree)
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
