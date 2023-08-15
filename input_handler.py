from typing import List


def user_input():
    pass_list = []
    password = input("Please input your password(s): ")

    while password:
        pass_list.append(password)
        password = input()

    return pass_list


def file_input():
    # TODO - Read password from a file
    pass


def get_input() -> List[str]:
    return user_input()
