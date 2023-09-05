from math import factorial as fl


def combination(n, k):
    return (fl(n) / (fl(k) * fl(n-k)))

