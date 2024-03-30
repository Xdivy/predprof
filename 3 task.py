f = open("products.csv")
x = 10000
sp = []
count = 0
sp1 = f.readline()
sp.append(sp1.split(";"))
sp2 = []
n = 0
cat = input()
prod = input()
for i in range(199):
    sp = f.readline().split(";")
    if sp[0] == cat and sp[1] == prod:
        sp2.append(sp[4])
        n = 1
    else:
        x = 1

if n != 1:
    print("Такой категории не существует в нашей БД")
else:
    print(min(sp2))
