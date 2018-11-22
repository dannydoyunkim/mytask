multiple = [ (i, j, i*j)
             for i in range(2,20,2)
             for j in range(3,20,3)
             if (i+j) % 7 == 0 ]

for step in multiple:
    print(step)
