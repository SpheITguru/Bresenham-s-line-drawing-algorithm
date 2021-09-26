print("Enter the value of x1: ")
x1 = int(input())
print("Enter the value of x2: ")
x2 = int(input())
print("Enter the value of y1: ")
y1 = int(input())
print("Enter the value of y2: ")
y2 = int(input())

dx = x2 - x1
dy = y2 - y1

m = dy/dx
if (dx > dy):
    steps = abs(dx)
    pk = 2*dy - dx
    print()
    print("m < 1, increase in x-axis")    
else:
    steps = abs(dy)
    pk = 2*dx - dy
    print()
    print("m > 1, increase in y-axis")

xincrement = dx/steps
yincrement = dy/steps

if m < 1:
    for i in range(steps-2):
        if pk < 0:
            pk1 = pk + 2*dy            
            x1 = x1 + 1
            y1 = y1
            print('{:2d} {:2d} {:2d} {:2d}'.format(pk, pk1, x1, y1))
            pk = pk1
        if pk > 0 or pk == 0:
            pk1 = pk + 2*dy - 2*dx            
            x1 = x1 + 1
            y1 = y1 + 1
            print('{:2d} {:2d} {:2d} {:2d}'.format(pk, pk1, x1, y1))
            pk = pk1
if m > 1:
    for i in range(steps-2):
        if pk < 0:
            pk1 = pk + 2*dx
            x1 = x1 
            y1 = y1 + 1
            print('{:2d} {:2d} {:2d} {:2d}'.format(pk, pk1, x1, y1))
            pk = pk1
        if pk > 0 or pk == 0:
            pk1 = pk + 2*dx - 2*dy
            x1 = x1 + 1
            y1 = y1 + 1
            print('{:2d} {:2d} {:2d} {:2d}'.format(pk, pk1, x1, y1))
            pk = pk1
