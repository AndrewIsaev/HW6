# import file with functions
from functions import *


def main():
    # define variables
    words_txt = "words.txt"
    history_txt = "history.txt"
    score = 0

    # name request
    print("Введите ваше имя")
    user_name = input()

    for word in get_word(words_txt):
        print(f"Угадайте слово: {shuffle_letters(word)}")
        user_answer = input()
        if user_answer == word:
            score += 10
            print("Верно! Вы получаете 10 очков.")
        else:
            print(f"Неверно! Верный ответ – {word}.")

    # Write results in file and print statistic
    write_history(user_name, score)
    game_amount, max_total_score = get_statistics(history_txt)
    print_statistics(game_amount, max_total_score)


if __name__ == "__main__":
    main()
