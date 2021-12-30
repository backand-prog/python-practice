# Write a program to remove characters from a string starting from zero up to n and return a new string.


def remove_chars():
    while True:
        word = input("Give the word: ")
        num = input("Give the number: ")

        if int(len(word)) < int(num):
            print("The number's mustn't be bigger than the lenght of the word! ")
        else:
            new_word = word[int(num):]
            return new_word


print(remove_chars())
