class ComplexityScoresStruct:
    length = None
    # combination = None
    # ...


def get_complexity(password):
    complex_scores_struct = ComplexityScoresStruct()

    complex_scores_struct.length = get_length_complexity(password)

    return complexity_calculator(complex_scores_struct)


def test(complex_scores_struct):
    length = get_length_complexity(password)
    complex_scores_struct.length = length


def complexity_calculator(complexity_scores_struct):
    complexity_score = complexity_scores_struct.length

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
