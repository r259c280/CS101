def factorial(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

print(factorial(4))
print(factorial(5))
