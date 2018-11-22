fp = open('c:/temp/data1.txt', 'r')

while True:
    sentence = fp.readline()
    fp.close()
    if not sentence:
        break
    print(sentence, end='')

#fp.close()
