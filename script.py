def f(n):
    if n == 1 or n == 0:
        return 1
    return f(n - 1) + f(n - 2)

n = 10
print(1 << n)
#print(f(39))
exit(0)
