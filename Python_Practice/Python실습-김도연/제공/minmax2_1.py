tmp ="CNS_34 CNS_12 CNS1 CNS78 CNS90 CNS45 CNS66 CNS10 CNS4 CNS56 CNS78 CNS19 CNS10 CNS66 CNS33 CNS90"


strlist = tmp.split()

max = int(strlist[0][3:])
min = int(strlist[0][3:])
for i in range(1, len(strlist)):
    if int(strlist[i][3:]) > max:
        max = int(strlist[i][3:])
    if int(strlist[i][3:]) < min:
        min = int(strlist[i][3:])

print("최대값: ", max)
print("최소값: ", min)
