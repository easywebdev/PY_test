from modules.sum import sumVars as sum
from modules.dif import difVars as dif

def varsAction(a, b, action):
    return action(a, b)

def divVars(a, b):
    return a - b

def main():
    res1 = varsAction(3, 6, sum)
    res2 = varsAction(9, 1, dif)
    print(res1, res2)


main()