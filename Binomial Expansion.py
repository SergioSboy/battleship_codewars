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