import sys

def parse_log_line(line):
    #Parses a line of the log file and returns a tuple of (timestamp, host1, host2).
    parts = line.split()
    if len(parts) != 3:
        raise ValueError(f"Invalid log line format: {line}")
    return int(parts[0]), parts[1], parts[2]

def search_log(file_path, start_time, end_time, search_string):
    #Searche the log file for entries within the specified time range and finds adjacent strings.
    adjacent_strings = []

    with open(file_path, 'r') as file:
        for line in file:
            timestamp, host1, host2 = parse_log_line(line)
            if start_time <= timestamp <= end_time:
                if search_string == host1:
                    adjacent_strings.append(host2)
                elif search_string == host2:
                    adjacent_strings.append(host1)

    return adjacent_strings

def main():
    if len(sys.argv) != 5:
        print("Usage: python3 log_parser.py <file_path> <start_time> <end_time> <search_string>")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = int(sys.argv[2])
    end_time = int(sys.argv[3])
    search_string = sys.argv[4]
    results = search_log(file_path, start_time, end_time, search_string)
    print(results)

if __name__ == "__main__":
    main()

