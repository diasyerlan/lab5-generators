def f(n):
    cnt = 1
    while(cnt <= int(n)):
        if cnt%3 == 0 or cnt%4 == 0:
            yield cnt
        cnt += 1
        
n = input()
vals = []
for i in f(n):
    vals.append(str(i))
print(",".join(vals))