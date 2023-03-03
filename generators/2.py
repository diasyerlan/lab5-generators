def f(n):
    cnt = 0
    while(cnt <= int(n)):
        cnt += 2
        yield cnt
        
n = input()
vals = []
for i in f(n):
    vals.append(str(i))
print(",".join(vals))