while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    riku = set()
    c = []
    for i in range(h):
        tmpc = list(map(int, input().split()))
        for j in range(w):
            if tmpc[j] == 1:
                riku.add((i, j))
        c.append(tmpc)

    ans = 0
    while len(riku) > 0:
        ans += 1
        que = [riku.pop()]

        while len(que) > 0:
            now = que.pop(0)

            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    nxt = (now[0] + di, now[1] + dj)
                    if di == 0 and dj == 0:
                        continue
                    if nxt[0] < 0 or nxt[0] >= h:
                        continue
                    if nxt[1] < 0 or nxt[1] >= w:
                        continue
                    if nxt not in riku:
                        continue

                    riku.remove(nxt)
                    que.append(nxt)
    print(ans)
