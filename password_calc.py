from collections import defaultdict


class ScoreType:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight


class ComplexityDatabase:

    def __init__(self):
        self.score_list = []

    def add_score(self, name, value, weight):
        ScoreType(name, value, weight)
        self.score_list.append(ScoreType)


def get_complexity(password) -> float:
    """
    External interface to the calculator
    Returns the combined complexity
    :param password:
    :return: combined complexity  - {"password": 1.23, "password2": 2.43}
    """
    complexity_database = ComplexityDatabase()

    # [length_struct, char_dupli_struct]
    complexity_database.add_score('length', get_length_complexity(password), 1)
    complexity_database.add_score('char_dupli', get_char_duplication(password), 1)

    return complexity_calculator(scores)


def complexity_calculator(scores) -> float:
    """
    :param scores: - {"password":{"length":1.23, "char_dupli": 2.25},}
    :return:
    """
    total_score = 0

    for score_name, score_value in scores:
        total_score += (score_value * weight[score_name])

    complexity_score = total_score / len(scores)

    return complexity_score


def get_length_complexity(password):
    """
    https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
    A common maximum length is 64 characters due to limitations in certain hashing algorithms
    :param password: password which to check
    :return: length_complexity
    """
    # This is so that we don't go over 64
    password_min = min(len(password), 64)
    length_complexity = password_min / 64
    return length_complexity


def get_char_combination_complexity():
    pass


def get_char_duplication(password: str):
    # {"a":1,"b":3}
    # 64

    char_dict = defaultdict(int)

    for pass_char in password:
        char_dict[pass_char] += 1

    {"a": 1, "b": 3}

    # len(password) /

    for char in char_dict:
        a = 6
        a = 2
        b = 2
        c = 1
        d = 1
        total = 0

    return 1


def get_word_duplication(password: str):
    pass


if __name__ == "__main__":
    tset = get_char_duplication("0123456789")
    print(tset)
