def divide(a, b):
    if b == 0:
        print("Division by zero not allowed")
        return
    count = 0
    sign = 1

    if a < 0:
        a = -a
        sign = -sign
    if b < 0:
        b= sign = -sign
    while a >= b:
        a = a-b
        count += 1
    print("Quotient:", sign *count)
    print("Remeinder:", a)
divide(10,3)