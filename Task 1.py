def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


# Call the function with a sample number
sample_number = 5
answer = factorial(sample_number)

print("Factorial of", sample_number, "is:", answer)