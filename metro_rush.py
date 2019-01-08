#!/usr/bin/env python3
from sys import argv
from MapParsers import get_map
from graph import Graph


def main():
    map = Graph(get_map(argv[-1]))
    print(map.run_the_trains())


if __name__ == '__main__':
    main()