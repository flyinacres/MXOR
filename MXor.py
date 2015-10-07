__author__ = 'rfischer'


def maxXor(l, r):
    result = 0
    v = 1
    while v <= r ^ l:
        result += v
        v *= 2
    return result


_l = int(raw_input())

_r = int(raw_input())

res = maxXor(_l, _r)

print(res)