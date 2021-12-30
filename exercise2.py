# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

for i in range(10):
    if i == 0:
        previous_num = 0
    else:
        current_num = i
        previous_num = i - 1
        sum = current_num + previous_num
        print("Current number: " + str(current_num) + " previous number: " + str(previous_num) + " Sum: " + str(sum))
