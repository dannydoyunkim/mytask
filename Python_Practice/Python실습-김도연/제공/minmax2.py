tmp ="CNS34 CNS12 CNS1 CNS78 CNS90 CNS45 CNS66 CNS10 CNS4 CNS56 CNS78 CNS19 CNS10 CNS66 CNS33 CNS90"


# 내가 한거
# list_tmp = tmp.split()
#
# min_value = int(list_tmp[0].replace("CNS",""))
# max_value = int(list_tmp[0].replace("CNS",""))
# min_loc = 0
# max_loc = 0
#
# for i in range(len(list_tmp)) :
#     value = int(list_tmp[i].replace("CNS", ""))
#     if value > max_value :
#         max_value = value
#         max_loc = i + 1
#
#     if value < min_value :
#         min_value = value
#         min_loc = i + 1
#
# print("최대값은 {}째 있는 CNS{} 입니다.".format(max_loc, max_value))
# print("최소값은 {}째 있는 CNS{} 입니다.".format(min_loc, min_value))

# 교수님꺼
list_tmp = tmp.split()

min_value = int(list_tmp[0][3::])
max_value = int(list_tmp[0][3::])
min_loc = 0
max_loc = 0

for i in range(len(list_tmp)) :
    value = int(list_tmp[i][3::])
    if value > max_value :
        max_value = value
        max_loc = i + 1

    if value < min_value :
        min_value = value
        min_loc = i + 1

print("최대값은 {}째 있는 {} 입니다.".format(max_loc, list_tmp[max_loc-1]))
print("최소값은 {}째 있는 {} 입니다.".format(min_loc, list_tmp[min_loc-1]))