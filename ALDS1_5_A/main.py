input()
A = list(map(int, input().split()))

avail = set()

for b in range(2 ** len(A)):
    tmp = 0
    for i in range(len(A)):
        if b >> i & 1:
            tmp += A[i]
    #print(tmp)
    avail.add(tmp)

input()
Q = list(map(int, input().split()))

for q in Q:
    if q in avail:
        print("yes")
    else:
        print("no")
