def fibo(n):                 # 피보나치 수열 결과 리턴
    result = []
    a, b, i = 0, 1, 0
    while i < n:
        result.append(b)
        a, b = b,a + b  # 이것이 Python에서 SWAP 하는 방법이다. (b는 영향을 안 받는다.)
        i+=1
    return result
