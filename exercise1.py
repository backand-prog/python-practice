number1 = 20
number2 = 30

number3 = 40
number4 = 30

def product_or_sum(a, b):
    if a * b <= 1000:
        return a * b
    else:
        return a + b


print(product_or_sum(number1, number2))
print(product_or_sum(number3, number4))
