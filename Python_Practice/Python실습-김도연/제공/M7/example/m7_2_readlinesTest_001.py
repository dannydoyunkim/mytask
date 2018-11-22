fp = open('c:/temp/data1.txt', 'r')
allLines = fp.readlines()
fp.close()

for sentence in allLines:
    print(sentence,end='')


