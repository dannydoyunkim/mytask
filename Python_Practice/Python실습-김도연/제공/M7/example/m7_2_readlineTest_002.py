fp = open('c:/temp/data2.txt', 'r', encoding='utf-8')

while True:
    sentence = fp.readline()
    if not sentence:
        break
    print(sentence, end='')

fp.close()
