# https://codeforces.com/problemset/problem/476/B
import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom


def probToReachDest(ds, dr):
    if len(ds) != len(dr):
        return 0.0
    prob = 1
    sent_pos = ds.count('+')
    sent_neg = ds.count('-')
    received_pos = dr.count('+')
    received_neg = dr.count('-')
    unknown = dr.count('?')
    if sent_pos == received_pos and sent_neg == received_neg:
        return prob
    if sent_pos < received_pos or sent_neg < received_neg:
        return 0.0
    prob = ncr(unknown, sent_pos - received_pos) / (2 ** unknown)
    return prob


if __name__ == "__main__":
    drazil_sent = input()
    dreamoon_received = input()
    print(probToReachDest(drazil_sent, dreamoon_received))
