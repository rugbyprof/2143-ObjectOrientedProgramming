import math

G = 6.67 * pow(10,-11)

m1 = 10

x1 = 1
y1 = 1

fs = []

for x2 in range(1,10):
    for y2 in range(1,10):
        d = max(abs(x2-x1),abs(y2-y1))
        if d == 0:
            continue
        F = (G*m1*m1) / (d * d)
    
        print('%d %d %d %.14f' % (m1,m1,d,F))

        if not F*pow(10,12) in fs:
            fs.append(F*pow(10,12) )

print(sorted(fs))

        