count = 1
result = 0
limit = int(input("어디까지 더할까요? "))

while count <= 1000:
    result = result + count
    count = count + 1
    if count == limit:
        break

print("1부터 %d까지의 합은: %d"% (count,result))
