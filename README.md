# S-Expression-Calculator
Usage:

$ ./calc.py 123
123

$ ./calc.py "(add 12 12)"
24

# Grammer
```
START = EXPR
EXPR = INTEGER | FUNC
FUNC = ADD | MULTIPLY
INTEGER = DIGIT, {DIGIT}
DIGIT = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
ADD = "(", "a", "d", "d", " ", EXPR, " ", EXPR, ")"
MULTIPLY = "(", "m", "u", "l", "t", "i", "p", "l", "y", " ", EXPR, " ", EXPR, ")"
```
