def f(n):
    n = [int(i) for i in n]
    x = []
    Sn = sorted(n)
    for i in range(len(n)):
        if Sn[i] %2 == 0 and n[i] %2 != 0:
            return "NO"
        elif Sn[i] %2 != 0 and n[i] %2 == 0:
            return "NO"
    return "YES"


u = int(input())
for i in range(u):
    r = input()
    n = input().split()
    print(f(n))

