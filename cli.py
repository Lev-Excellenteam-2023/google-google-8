from search_wards import get_best_k_completions


def main():
    print("Start typing and press enter to get suggestions\nPress Ctrl+c to kill program :)\n")
    while True:
        prefix = input("Type......\n")
        [print(sentence) for sentence in get_best_k_completions(prefix)]


if __name__ == '__main__':
    main()
