import random


def count_words_in_file(file_name):
    """
    Count lines in file
    :param file_name (str):file name
    :return: int
        quantity of line in file
    """
    counter_line = 0
    with open(file_name) as file:
        for line in file:
            counter_line += 1
    return counter_line


def shuffle_letters(word):
    """
    Shuffle letters in word
    :param word: str
    :return: str
    """
    word_list = [symbol for symbol in word]
    random.shuffle(word_list)
    shuffle_word = "".join(word_list)

    return shuffle_word


def chose_word(file_name, word_number):
    """
    Choose word from file with index
    :param file_name: str
    :param word_number: int
    :return: str
    """
    words = []
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            words.append(line.strip())
    return words[word_number]


def write_history(name, score):
    """
    Write history to file
    :param name: str
    :param score: int
    :return: None
    """
    with open("history.txt", "a", encoding="utf-8") as stats:
        stats.write(f"{name} {score}\n")


def get_statistics(file_name):
    """
    From file with history get amount of games and max score
    :param file_name: str
    :return:
    """
    with open(file_name) as file:
        score_list = []
        for line in file:
            score_list.append(int(line.split()[1]))
    return len(score_list), max(score_list)


def print_statistics(total_games, max_score):
    """
    Print statistic
    :param total_games: int
    :param max_score: int
    """
    print(f"Всего игр сыграно: {total_games}")
    print(f"Максимальный рекорд: {max_score}")
