from search_words import get_best_k_completions, init_system
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("data_path", type=str)
    args = parser.parse_args()
    data_path = args.data_path
    init_system(data_path)

    print("Start typing and press enter to get suggestions\nPress Ctrl+c to kill program :)\n")
    while True:
        prefix = input("Type......\n")
        [print(sentence.completed_sentence) for sentence in get_best_k_completions(prefix)]


if __name__ == '__main__':
    main()
