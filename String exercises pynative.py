# https://pynative.com/python-string-exercise/
# Exercise 1
# Create a string made of the first, middle and last character

string1 = "James"
result1 = string1[0] + string1[int(len(string1) / 2)] + string1[len(string1) - 1]
print("Result of the first exercise: " + result1)

# Exercise 1B
# Write a program to create a new string made of the middle three characters of an input string.

# Case1
string2 = "JhonDipPeta"
result2 = string2[int((len(string2) / 2) + - 1)] + string2[int(len(string2) / 2)] + string2[int((len(string2) / 2) + 1)]
print("Result of the first exercise/B Case1: " + result2)

# Case2
string3 = "JaSonAy"
result3 = string3[int((len(string3) / 2) + - 1)] + string3[int(len(string3) / 2)] + string3[int((len(string3) / 2) + 1)]
print("Result of the first exercise/B Case2: " + result3)

# Exercise 2
# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
s1 = "Ault"
s2 = "Kelly"
print("Result of the second exercise: " + s1[:int(len(s1) / 2)] + s2 + s1[int(len(s1) / 2):])


# Exercise 3
# Given two strings, st1 and st2, write a program to return a
# new string made of s1 and s2’s first, middle, and last characters.
st1 = "America"
st2 = "Japan"
st3 = st1[0] + st2[0] + st1[int(len(st1) / 2)] + st2[int(len(st2) / 2)] + st1[int(len(st1)) - 1] + st2[int(len(st2)) - 1]
print("Result of the third exercise: " + st3)

# Exercise 4
# Arrange string characters such that lowercase letters should come first
str1 = "PyNaTive"
new_str1 = ""
for i in str1:
    if i.islower():
        new_str1 = i + new_str1
    else:
        new_str1 = new_str1 + i
print("Result of the fourth exercise: " + new_str1)

# Exercise 4 with the method used on the website
str2 = "PyNaTive"
lower = []
upper = []
for i in str2:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)

sorted_lst = "".join(lower + upper)
print("Result of the fourth exercise using the example of the website: " + sorted_lst)

# Exercise 5
# Count all letters, digits, and special symbols from a given string
str_to_count = "P@#yn26at^&i5ve"
Chars, Digits, Specs = 0, 0, 0
for i in str_to_count:
    if i.isalpha():
        Chars += 1
    elif i.isdigit():
        Digits += 1
    else:
        Specs += 1
print("Result of exercise 5: "
      "Number of characters: " + str(Chars) + " number of digits : "
                                              "" + str(Digits) + " number of spec chars: " + str(Specs))

# Exercise 6
# Create a mixed String using the following rules
# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the
# last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at
# the end of the result.

strng1 = "Abc"
strng2 = "Xyz"
strng3 = ""
for i in strng1:
    strng3 = strng3 + strng1[strng1.index(i)] + strng2[len(strng2) - strng1.index(i) - 1]
print("Result of exercise 6: " + strng3)

# Exercise 7
# Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the
# characters in the s1 are present in s2. The character’s position doesn’t matter.

# Case 1 (supposed to be True)

sg1 = "Yn"
sg2 = "PYnative"

is_balanced = True
for i in sg1:
    if i in sg2:
        continue
    else:
        is_balanced = False
print("Result of exercise 7, case 1: " + str(is_balanced))

# Case 2 (supposed to be False)

srg1 = "Ynf"
srg2 = "PYnative"

is_balanced_2 = True
for i in srg1:
    if i in srg2:
        continue
    else:
        is_balanced_2 = False
print("Result of exercise 7, case 2: " + str(is_balanced_2))


# Exercise 8
# Write a program to find all occurrences of “USA” in a given string ignoring the case.

string_with_usa = "Welcome to USA. usa awesome, isn't it?"

usa_count = string_with_usa.count("USA") + string_with_usa.count("usa")
print("Result of exercise 8 - USA count: " + str(usa_count))

# Exercise 9
# Given a string s1, write a program to return the sum and average of the digits that appear in the string,
# ignoring all other characters.

string_with_digits = "PYnative29@#8496"
sum_of_digits = 0
digit_count = 0
for i in string_with_digits:
    if i.isdigit():
        sum_of_digits = sum_of_digits + int(i)
        digit_count += 1

print("Result of exercise 9 - sum: " + str(sum_of_digits) + ", average: " + str(sum_of_digits / digit_count))

# Exercise 10
# Write a program to count occurrences of all characters within a string

st_occurences = "Apple"
set_occurs = {}
for i in st_occurences:
    set_occurs[i] = 0

for i in st_occurences:
    set_occurs.update({i: set_occurs[i]++1})

print("Result of exercise 10: " + str(set_occurs))

# Exercise 11
# Reverse a given string
st_to_reverse = "PYnative"
st_to_reverse = st_to_reverse[::-1]
print("Result of exercise 11: " + str(st_to_reverse))

