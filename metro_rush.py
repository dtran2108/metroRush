#!/usr/bin/env python3
from sys import argv
from MapParsers import get_map
from graph import Graph
from time import time


def main():
    start = time()
    
    map = Graph(get_map(argv[-1]))
    map.run_the_trains()

    end = time()
    print('run-time: {}s'.format(end-start))

if __name__ == '__main__':
    main()