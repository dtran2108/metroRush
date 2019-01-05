#!/usr/bin/env python3
from sys import argv
from MapParsers import get_map
from graph import Graph


def main():
    map = Graph(get_map(argv[-1]))
    stations = map.get_all_stations()
    requirements = map.get_requirements()
    start_line, start_stationId = requirements.get_start_point()
    print(stations['Blue Line'].get_stationId_from_name('Janak Puri West'))
    print(stations['Blue Line'].get_all_transfer_points())


if __name__ == '__main__':
    main()