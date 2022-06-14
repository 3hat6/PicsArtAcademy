''' 1.13 Iterativ tarberakov astichan bardzracnelu programm '''


def is_even(n): return n % 2 == 0


def square(n): return n*n


def fast_pow(m, n):
    res = 1
    while n != 1:
        if is_even(n):
            res *= square(m)
            n /= 2
        else:
            res *= m
            n -= 1
    return res


print(fast_pow(3, 4))


def half(n):
    if is_even(n):
        return n/2
def double(n): return n * 2

def mul(a, b):
    if b == 1:
        return 0
    if half(b):
        return double(a) + mul(a, b/2)

    return a + mul(a, b-1)
# 2 + (2,2)     2 + (4+1)



