f = open("products.csv")
x = 10000
sp = []
count = 0
sp1 = f.readline()
sp.append(sp1.split(";"))
sp2 = []
n = 0
for i in range(199):
    sp = f.readline().split(";")
    n = sp[0][:2:] + sp[2][:2:] + sp[0][-1] + sp[0][-2] + sp[2][5] + sp[2][4]
    sp2.append(n)
    print(sp2)