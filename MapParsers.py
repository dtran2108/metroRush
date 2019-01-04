def get_all_line_name(content):
    """ return a dictionary contains all of the lines
        and its stations """
    lst = []
    lines = []
    for element in content[:-4]:
        if element.startswith('#') and lst:
            lines.append(lst)
            lst.clear()
        lst.append(element)
    lines.append(lst)
    result = []
    for line in lines:
        dic = {}
        dic[line[0]] = line[1:]
        result.append(dic)
    return result


def get_requirements(content):
    """ return a list of dictionary that contains
        the requirements """
    requirements = []
    for element in content[-3:]:
        dic = {}
        dic[element.split('=')[0]] = element.split('=')[-1]
        requirements.append(dic)
    return requirements


def get_map(filename):
    """ return a dictionary contains the lists that
        has the line name and station name and
        a list that contains the requirements"""
    f = open(filename, 'r')
    content = f.read().splitlines()
    result = get_all_line_name(content)
    requirements = get_requirements(content)
    return result, requirements