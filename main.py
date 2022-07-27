import random

with open("words.txt") as file:
    print(file.read())


def greeting():
    print("Введите ваше имя")
    user_name = input()
    return user_name


def rearranging_letters(word):
    """
    Перемешивает буквы в слове
    :return:
    """
    word_list = [symbol for symbol in word]
    random.shuffle(word_list)
    rearranging_word = "".join(word_list)

    return rearranging_word


print(rearranging_letters("Привет"))
