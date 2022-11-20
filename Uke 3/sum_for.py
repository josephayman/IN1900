s = 0
M = 3
for k in range(1, M+1): 
    s += 1/(2*k**2)
print(s)

"""
Wrong code
s = 0
M = 3
for i in range(M):
    s += 1/2*k**2
print(s)

1) The variable k is not defined in the loop. So we change i to k.
2) The loop is not executed M times, but M-1 times. So we change range(M) to range(1, M+1).
3) The formula is wrong. We should use parentheses to make sure that the exponentiation is done first.

"""
