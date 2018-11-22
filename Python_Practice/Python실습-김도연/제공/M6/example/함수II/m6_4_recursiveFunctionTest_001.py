def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n-1)

print("5! = ", end='')
print(factorial(5))
    

