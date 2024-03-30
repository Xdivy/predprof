f = open("products.csv")
x = 0
sp = []
count = 0
sp1 = f.readline()
sp.append(sp1.split(";"))
sp2 = []
n = 1
for i in range(199):
    sp = f.readline().split(";")
    t=(sp[3][:-2:])
    t = int(t)
    if x < t:
       x = t
       sp2 = sp
print(sp2)