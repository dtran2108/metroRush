from sys import argv
from MapParsers import get_map
from graph import Graph


def main():
    map = Graph(get_map(argv[-1]))
    stations = map.get_all_stations()
    requirements = map.get_requirements()
    start_point = requirements.get_start_point()
    line_name = start_point.split(':')[0]
    station_id = int(start_point.split(':')[-1])
    print('start point: ', stations[line_name].get_station_name_from_id(station_id))


if __name__ == '__main__':
    main()