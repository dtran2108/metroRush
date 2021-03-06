from sys import exit, stderr


def get_all_line_name(content):
    """ return a dictionary contains all of the lines
        and its stations """
    result = {}
    for element in content[:-4]:
        if element.startswith('#'):
            line = element.strip('#')
            result[line] = []
        else:
            result[line].append(element)
    return result


def get_requirements(content):
    """ return a dictionary that contains
        the requirements """
    requirements = {}
    for element in content[-3:]:
        requirements[element.split('=')[0]] = element.split('=')[-1]
    return requirements


def check_file(filename):
    """ check the file Permission and Existence """
    try:
        f = open(filename, 'r')
    except Exception:
        print('Invalid file', file=stderr)
        exit()
    return f


def get_map(filename):
    """ return a dictionary contains the lists that
        has the line name and station name and
        a list that contains the requirements"""
    file = check_file(filename)
    content = file.read().splitlines()
    result = get_all_line_name(content)
    requirements = get_requirements(content)
    return result, requirements
