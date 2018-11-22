# total = 0
#
# for i in range(1,11) :
#     total = total +1
# 와 같은 코드를 While로 해보자

total = 0
i = 0

#while i < 10 : # i = 0, i < 10 까지 이므로, 0 - 9까지만 돈다.
while i <= 10:                # i = 0, i <= 10 으로하면, 0 ~ 10까지 돈다.
    total = total + i
    i += 1

print('totla = {} '.format(total) )

