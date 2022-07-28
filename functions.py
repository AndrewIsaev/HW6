"""Functions for game"""
import random


def shuffle_letters(word: str):
    """
    Shuffle letters in word
    :param word: word which we need to shuffle
    :return: shuffle word
    """
    word_list = [symbol for symbol in word]
    random.shuffle(word_list)
    shuffle_word = "".join(word_list)

    return shuffle_word


def get_word(file_name: str):
    """
    Get words from file
    :param file_name: name if file
    :return: list of word
    """
    words = []
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            words.append(line.strip())
    return words


def write_history(name: str, score: int):
    """
    Write history to file
    :param name: username
    :param score: game score
    :return:
    """
    with open("history.txt", "a", encoding="utf-8") as stats:
        stats.write(f"{name} {score}\n")


def get_statistics(file_name: str):
    """
    From file with history get amount of games and max score
    :param file_name: filename
    :return: quantity of games , max result
    """
    with open(file_name) as file:
        score_list = []
        for line in file:
            score_list.append(int(line.split()[1]))
    return len(score_list), max(score_list)


def print_statistics(total_games: int, max_score: int):
    """
    Print statistic
    :param total_games: quantity of games
    :param max_score: max result
    """
    print(f"Всего игр сыграно: {total_games}")
    print(f"Максимальный рекорд: {max_score}")
