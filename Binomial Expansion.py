# The purpose of this kata is to write a program that can do some algebra.
# Write a function expand that takes in an expression with a single, one character variable, and expands it.
# The expression is in the form (ax+b)^n where a and b are integers which may be positive or negative,
# x is any single character variable, and n is a natural number. If a = 1, no coefficient will be placed in front of the variable.
# If a = -1, a "-" will be placed in front of the variable.
# The expanded form should be returned as a string in the form ax^b+cx^d+ex^f... where a, c, and e are the coefficients of the term,
# x is the original one character variable that was passed in the original expression and b, d, and f,
# are the powers that x is being raised to in each term and are in decreasing order.
# If the coefficient of a term is zero, the term should not be included.
# If the coefficient of a term is one, the coefficient should not be included.
# If the coefficient of a term is -1, only the "-" should be included.
# If the power of the term is 0, only the coefficient should be included.
# If the power of the term is 1, the caret and power should be excluded.
# ----------------------------------------------------------------------------
# expand("(x+1)^2")      # returns "x^2+2x+1"
# expand("(p-1)^3")      # returns "p^3-3p^2+3p-1"
# expand("(2f+4)^6")     # returns "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"
# expand("(-2a-4)^0")    # returns "1"
# expand("(-12t+43)^2")  # returns "144t^2-1032t+1849"
# expand("(r+0)^203")    # returns "r^203"
# expand("(-x-1)^2")     # returns "x^2+2x+1"
import math
# ----------------------------------------------------------------------------
def s(x1, x2, y2, f, k, n):
    fact = 0
    fact = (math.factorial(n)) // (math.factorial(k) * math.factorial(n - k))
    m = 0
    if abs(int(x1)) > 1 and abs(int(y2)) > 1:
        m = (int(x1) ** (n - k)) * (int(y2) ** (k))
    elif abs(int(x1)) == 1 and abs(int(y2)) == 1:
        if int(x1) < 0 or int(y2) < 0:
            m = (int(x1) ** (n-k)) * (int(y2) ** k)
        else:
            m = 1
    elif abs(int(x1)) > 1 and abs(int(y2)) == 1:
        m = (int(x1) ** (n - k)) * (int(y2) ** (k))
    elif abs(int(x1)) == 1 and abs(int(y2)) > 1:
        m = (int(x1) ** (n - k)) * (int(y2) ** (k))
    t = fact * m
    if abs(t) > 1 and n % 2 == 0:
        if t > 0 and f != n:
            return f'+{t}'
        else:
            return f'{t}'
    elif abs(t) > 1 and n % 2 == 1:
        if t > 0 and f != n:
            return f'+{t}'
        else:
            return t
    elif abs(t) == 1 and f == 0:
        if (n%2 == 0 and t > 0) or (n%2 == 1 and t >0):
            return f'+{t}'
        else:
            return '-1'
    else:
        return ''
# ------------------------------------------------------------------------------
def st(x2, n, k):
    if n - k == 1:
        return x2
    if n - k == 0:
        return 1
    else:
        return f'{x2}^{n - k}'
# ------------------------------------------------------------------------------
def expand(expr):
    print(expr)
    i1 = i2 = i3 = i4 = 0
    x = ''
    y = ''
    n = ''
    result = ''
    k = 0
    # ------------------------------------------------------------------------------
    for i in range(len(expr)):

        if expr[i] == '(':
            i1 = i

        elif expr[i] == '+' or expr[i] == '-':
            i2 = i

        elif expr[i] == ')':
            i3 = i

        elif expr[i] == '^':
            i4 = i
    # ------------------------------------------------------------------------------
    x = expr[i1 + 1:i2]
    n = expr[i4 + 1:]
    if len(x) == 2:
        if x[0] == '-':
            x1 = -1
            x2 = x[1]
        else:
            x1 = x[0]
            x2 = x[1]

    elif len(x) > 2:
        x1 = expr[i1 + 1:i2 - 1]
        x2 = expr[i2 - 1]

    else:
        x1 = 1
        x2 = x[0]
    if expr[i2] == '-':
        y2 = expr[i2 - 1 + 1:i3]
    else:
        y2 = expr[i2 + 1:i3]
    # ------------------------------------------------------------------------------
    f = int(n)
    if n == '0':
        return '1'
    elif n == '1':
        return expr[i1+1:i3]
    # ------------------------------------------------------------------------------
    elif int(y2) > 0 and int(x1) > 0:
        while f >= 0:
            if f > 0:
                result = result + f'{s(x1, x2, y2, f, k, int(n))}' + f'{st(x2, int(n), k)}'
            elif f == 0 or f == 1:
                result = result + f'{s(x1, x2, y2, f, k, int(n))}'
            k += 1
            f -= 1

    # ------------------------------------------------------------------------------
    elif (int(y2) < 0 or int(x1) < 0) and int(n) % 2 == 0:
        while f >= 0:
            if f > 0:
                result = result + f'{s(x1, x2, y2, f, k, int(n))}' + f'{st(x2, int(n), k)}'
            elif f == 0:
                result = result + f'{s(x1, x2, y2, f, k, int(n))}'
            k += 1
            f -= 1

    # ------------------------------------------------------------------------------
    elif (int(y2) < 0 and int(x1) < 0) and int(n) % 2 == 0:
        while f >= 0:
            if f > 0:
                result = result + f'{s(x1, x2, y2, f, k, int(n))}' + f'{st(x2, int(n), k)}'
            elif f == 0:
                result = result + f'{s(x1, x2, y2, f, k, int(n))}'
            k += 1
            f -= 1
        result = result.replace('-','+')
        # ------------------------------------------------------------------------------
    elif (int(y2) < 0 or int(x1) < 0) and int(n) % 2 == 1:
        while f >= 0:
            if f > 0:
                result = result + f'{s(x1, x2, y2, f, k, int(n))}' + f'{st(x2, int(n), k)}'
            elif f == 0:
                result = result + f'{s(x1, x2, y2, f, k, int(n))}'
            k += 1
            f -= 1
    return result

print(expand(('(9x-1)^4')))