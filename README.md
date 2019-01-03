# Metro Rush
A transit map is a topological map of a public transport system. It is composed of lines, stations, and transfer points. A line connects several stations in a direct route from a first station to an end station. A transfer point is a station that is crossed by two or more lines. A transfer point allows passengers to change from a line to one other.

The current project requires you to find the smallest number of turns that is required for all the trains to move from a specified station (start point) to another specified station (end point).

There are a few constraints you have to respect:

1. there can be only one train at a given station, except at the specified start and end points;
2. all the trains can move during a turn;
3. a train can move from a station to only one connected station of the current line during one turn;
4. a train can switch from a line to another at a transfer point during one turn;
5. a train can move from a station to another or it can switch from a line to another during one turn; it cannot do both during one turn.
## Specifications
You will write a Python script, name metro_rush.py, which takes a filename as an argument. This file contains a list of metro lines and metro stations of the following form:
```sh
#<line_name>
1:<station_name>
2:<station_name>
3:<station_name>
(…)
#<line_name>
1:<station_name>
2:<station_name>
3:<station_name>
(…)

START=<line_name>:<station_id>
END=<line_name>:<station_id>
TRAINS=n
```
Where:

- where all stations in a line are connected in the order of their IDs. A station that has two or more lines passing through will appear with the same name in all lines.
- a circular line will have the first and last ID with the same name.
- all trains will get their own label Tx (where x has a unique value between 1 and n).
- if the file is improperly formatted, your program will output "Invalid file" on stderr before exiting.
- To visualize the result, the program will print the state of the network at each turn in the following way: for each occupied station, print <station_name>(<line_name>:<station_id>)-<train_label>

Example:
```
Tagore Garden(Blue Line:18)-T15
```

The program stops when all trains have reached the end station.

Below is the picture of Delhi Metro network and example metro stations file that contain part of it. It's just for example, you can use this or other city metro map to create the metro stations file.

Source link: https://delhimetrorail.info/delhi-metro-map
