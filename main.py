import json

import input_handler, password_calc


def main():
    # cli_inputs = process_cli_inputs()
    complexity_dict = get_complexity_dict()
    print(complexity_dict)


def get_complexity_dict():

    complexity_dict = {}
    passwords = input_handler.get_input()

    for password in passwords:
        pass_complexity = password_calc.get_complexity(password)
        # {"password":1.23,...}
        complexity_dict[password] = pass_complexity

    return complexity_dict


def process_cli_inputs():
    pass


if __name__ == "__main__":
    main()
