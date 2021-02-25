def factorial(n):
    if n <= 1:
        return 1

    return factorial(n-1) * n


if __name__ == "__main__":
    n = 5
    print(f"Teh factorial of {n} is {factorial(n)}")