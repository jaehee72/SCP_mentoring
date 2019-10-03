zero = 0
one = 0

def fibonacci(n):
    if n == 0:
        global zero
        zero += 1
        return 0
    elif n == 1:
        global one
        one += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

T = int(input())
for i in range(T):
    n = int(input())
    fibonacci(n)
    print(zero, " ", one)
    zero = 0
    one = 0
import sys
sys.setrecursionlimit(n<41)
