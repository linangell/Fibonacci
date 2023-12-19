def factorial(k):
    result = 1
    for i in range(2, k + 1):
        result *= i
    return result
#
# k = int(input ("Enter a value: "))
# result = factorial(k)
# print("The factorial of", k," is:", result)