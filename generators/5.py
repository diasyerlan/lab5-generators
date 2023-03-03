def f(n):
    cnt = int(n)
    yield cnt
    while(cnt > 0):
        cnt -= 1
        yield cnt
        
n = input()
vals = []
for i in f(n):
    vals.append(str(i))
print(",".join(vals))