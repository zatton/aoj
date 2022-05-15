n = int(input())

vl = []

for _ in range(n):
    v = list(map(int, input().split()))
    v = [_v - 1 for _v in v[2:]]
    vl.append(v)

seen = set()
remain = set()

for i in range(n):
    remain.add(i)

ft = [0 for _ in range(n)]
st = [0 for _ in range(n)]

def dfs(now, t):
    #print(ft)
    now_t = t + 1
    ft[now] = now_t

    seen.add(now)
    remain.remove(now)

    for v in vl[now]:
        if v not in seen:
            now_t = dfs(v, now_t)

    now_t += 1
    st[now] = now_t

    return now_t

t = dfs(0, 0)

while len(remain) > 0:
    st_v = min(remain)
    t = dfs(st_v, t)

for i in range(n):
    print(f"{i + 1} {ft[i]} {st[i]}")
