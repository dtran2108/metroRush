#!/usr/bin/env python3
from sys import argv, stderr
from MapParsers import get_map
from graph import Graph
from time import time


def main():
    start = time()
    map = Graph(get_map('delhi-metro-stations'))
    map.run_the_trains()
    end = time()
    print('run-time: {}s'.format(end-start))

if __name__ == '__main__':
    # try:
    main()
    # except:
    #     print('Invalid file', file=stderr)
