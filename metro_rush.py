from sys import argv
from MapParsers import get_map


def main():
    print(get_map(argv[-1]))


if __name__ == '__main__':
    main()