A, B = map(int, input().split())

def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(A, B))
