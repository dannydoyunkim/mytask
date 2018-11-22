fp = open('c:/temp/data1.txt', 'r')
allList = fp.read().splitlines()
fp.close()

for sentence in allList:
    print(sentence)


