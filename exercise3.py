# Write a program to accept a string from the user and display characters that are present at an even index number.

str = "pynative"
j = 0
for i in str:
    if not (j % 2):
        print(str[j])
    j += 1
