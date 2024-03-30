f = open("products.csv")
x = 0
sp = []
count = 0
sp1 = f.readline()
sp.append(sp1.split(";"))
sp2 = []
n = 2
for i in range(199):
    sp = f.readline().split(";")
    if sp[0] == "Закуски":
        x = (float(sp[4]) * float(sp[3]))
        count += x
        n+=1
print(count)