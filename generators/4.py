def f(a, b):
    for i in range(int(a), int(b) + 1):
        yield i*i
        
a = input()
b = input()
vals = []
for i in f(a, b):
    vals.append(str(i))
print(",".join(vals))