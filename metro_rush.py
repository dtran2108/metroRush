from sys import argv


def get_map(filename):
    """ return a list contains the lists that
        has the line name and station name and
        a list that contains the requirements"""
    f = open(filename, 'r')
    content = f.read().splitlines()
    lst = []
    lines = []
    for element in content[:-4]:
        if element.startswith('#') and lst:
            lines.append(lst)
            lst = []
        lst.append(element)
    lines.append(lst)
    return lines, [element for element in content[-3:]]


def main():
    print(get_map(argv[-1]))


if __name__ == '__main__':
    main()