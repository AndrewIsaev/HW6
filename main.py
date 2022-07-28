# import file with functions
from functions import *


def main():
    # define variables
    WORDS_FILE = "words.txt"
    HISTORY_FILE = "history.txt"
    score = 0

    # name request
    print("Введите ваше имя")
    user_name = input()

    for i in range(count_words_in_file(WORDS_FILE)):
        print(f"Угадайте слово: {shuffle_letters(chose_word(WORDS_FILE, i))}")
        user_answer = input()
        if user_answer == chose_word(WORDS_FILE, i):
            score += 10
            print("Верно! Вы получаете 10 очков.")
        else:
            print(f"Неверно! Верный ответ – {chose_word(WORDS_FILE, i)}.")

    # Write results in file and print statistic
    write_history(user_name, score)
    game_amount, max_total_score = get_statistics(HISTORY_FILE)
    print_statistics(game_amount, max_total_score)


if __name__ == "__main__":
    main()
