while True:
    n, x = map(int, input().split())

    if n == 0 and x == 0:
        break

    ans = 0

    for i in range(1, n):
        for j in range(i + 1, n):
            if x - i - j > j and x - i - j <= n:
                #print(i, j, x - i - j)
                ans += 1

    print(ans)
