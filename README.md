# S-Expression-Calculator

## Python Version

3.8

## Usage:

```
$ ./calc.py 123
123

$ ./calc.py "(add 12 12)"
24

$ ./calc.py "(add 12 12 12 12 12)"
60

$ ./calc.py "(add 12 (multiply 2 2))"
16
```

## Supported Functions

```
ADD
SUBTRACT
DIVIDE
MULTIPLY
```

## Grammer

```
START = EXPR
EXPR = INTEGER | FUNC
FUNC = ADD | MULTIPLY
INTEGER = DIGIT, {DIGIT}
DIGIT = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
ADD = "(", "a", "d", "d", " ", EXPR, " ", EXPR, ")"
MULTIPLY = "(", "m", "u", "l", "t", "i", "p", "l", "y", " ", EXPR, " ", EXPR, ")"
```
