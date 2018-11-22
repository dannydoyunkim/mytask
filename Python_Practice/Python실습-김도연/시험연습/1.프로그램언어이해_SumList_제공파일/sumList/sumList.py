def addList(result, input1, input2):

    # input1_value = 0
    # input2_value = 0
    #
    # for i in range(len(input1)) :
    #     input1_value = input1_value *10 + input1[len(input1)-i-1]
    #
    # for i in range(len(input2)) :
    #     input2_value = input2_value *10 + input2[len(input2)-i-1] # 1의 자리는 10의 0승, 2의 자리는 10의 1승, 3의 자리는 10의 2승 잊지말자.
    #
    # result_value = input1_value + input2_value
    # result[0] = result_value % 10
    # result[1] = ( result_value // 10 ) % 10
    # result[2] = result_value // 100
    #
    # return result

#### 정답
    input1 = input1[::-1]
    input2 = input2[::-1]

    num1, num2 = "", ""

    for i in range(len(input1)) :
        num1 += str(input1[i])  # 문자로 변환하여 더하면 쉽게 변환됨
        num2 += str(input2[i])  # 문자로 변환하여 더하면 쉽게 변환됨

    num = int(num1) + int(num2)

    numlist = list(str(num))[::-1]

    for i in range(3) :
        result[i] = int(numlist[i])

    # return result # 이건 불필요하다, 들어온 값이 mutable object such as List, Dictionary, Set 라서 return하지 않아도 공유된다.


def printList(listvalue):
    print("[", end='')

    # TODO
    for i in range(len(listvalue)) :
        print("%d" % listvalue[i],end='')
        if i < len(listvalue)-1 :
            print(', ',end='')

    print("]")
