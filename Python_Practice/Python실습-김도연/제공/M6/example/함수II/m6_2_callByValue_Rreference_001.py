def Calc1(data):
    data = data + 1
    
def Calc2(data):    
    data[0] = data[0] + 1

def Calc3(data):
    sum = 0;
    for item in data:
        sum += item
    return sum 

data1 = 1
data2 = [1,3,5,7]
    
# Call by Value
Calc1(data1)
print('data1 : ', data1)

print('원본 data2 : ', data2)
    
# Call by Reference
Calc2(data2)  #data2가 리스트 이므로 call by reference가 됨.
print('data2 : ', data2)

sum = Calc3(data2)
print('sum of data2 : ', sum)
