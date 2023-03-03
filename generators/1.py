def f(n):
    cnt = 0
    while(cnt <= n):
        yield cnt*cnt
        cnt += 1
        

for i in f(5):
    print(i)