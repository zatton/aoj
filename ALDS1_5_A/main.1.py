input()
A = list(map(int, input().split()))

avail = set([0])

for a in A:
    tmp_avail = set()
    for b in avail:
        tmp_avail.add(a + b)
    for b in tmp_avail:
        avail.add(b)

input()
Q = list(map(int, input().split()))

for q in Q:
    if q in avail:
        print("yes")
    else:
        print("no")
