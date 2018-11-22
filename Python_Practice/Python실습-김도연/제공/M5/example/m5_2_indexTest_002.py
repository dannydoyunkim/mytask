s1 = "DIGITAL INNOVATION LEADER"

for i in range(len(s1)):
    if( i % 5 == 0):
        print()
    print("[{:2d}]:{} ".format(i,s1[i]), end='')

print("\n")
print("s1[1:5] = ", s1[1:5]) 
print("s1[:6] = ", s1[:6])
print("s1[6:] = ", s1[6:]) 
