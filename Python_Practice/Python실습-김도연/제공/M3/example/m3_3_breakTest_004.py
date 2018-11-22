a = 0
allBreak = True

for i in range(100):
    for j in range(100):
        a = j
        print(a)

        if(a == 15):
            allBreak = False
            break
    if(allBreak == False):   
        break                
print("a = ", a)    
