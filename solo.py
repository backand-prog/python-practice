weight, height = 0, 0

while weight == 0 or height == 0:

    weight = int(input())
    height = float(input())

bmi = weight / (height ** 2)
print(bmi)


if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi and bmi < 25:
    print("Normal")
elif 25 <= bmi and bmi < 30:
    print("Overweight")
else:
    print("Obesity")
