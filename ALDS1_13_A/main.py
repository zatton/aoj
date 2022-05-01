import itertools

n = int(input())

yoko = set() # a: 0-7
tate = set() # b: 0-7
migiue = set() # a + b: 0-14
migisita = set() # a - b: -7-7
ql = []

for _ in range(n):
    a, b = map(int, input().split())
    tate.add(a)
    yoko.add(b)
    migiue.add(a + b)
    migisita.add(a - b)
    ql.append((a, b))

xl = [x for x in range(8) if x not in tate]
yl = [y for y in range(8) if y not in yoko]


for xll in itertools.permutations(xl):
    for yll in itertools.permutations(yl):
        tmp_tate = set() # a: 0-7
        tmp_yoko = set() # b: 0-7
        tmp_migiue = set() # a + b: 0-14
        tmp_migisita = set() # a - b: -7-7

        ok = True

        for i in range(len(xll)):
            _x = xll[i]
            _y = yll[i]
            if _x not in tate and _y not in yoko and \
                    (_x + _y) not in migiue and (_x - _y) not in migisita and\
                    _x not in tmp_tate and _y not in tmp_yoko and \
                    (_x + _y) not in tmp_migiue and (_x - _y) not in tmp_migisita:
                tmp_tate.add(_x)
                tmp_yoko.add(_y)
                tmp_migiue.add(_x + _y)
                tmp_migisita.add(_x - _y)
            else:
                ok = False
                break

        if ok:
            ans = [['.' for _ in range(8)] for _ in range(8)]
            for q in ql:
                ans[q[0]][q[1]] = 'Q'
            for _x, _y in zip(xll, yll):
                ans[_x][_y] = 'Q'

            for a in ans:
                print(''.join(a))
            exit()
