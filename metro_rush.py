from sys import argv


def get_map(filename):
    f = open(filename, 'r')
    content = f.read().splitlines()
    lst = []
    lines = []
    for element in content:
        if element.startswith('#') and lst:
            lines.append(lst)
            lst = []
        lst.append(element)
        print(element)
    return lines


def main():
    print(get_map(argv[-1]))


if __name__ == '__main__':
    main()