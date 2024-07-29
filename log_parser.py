import sys


def parse_log_line(line):
    """
        Parses a single log line into its components.

        Args:
            line (str): A single line from the log file.

        Returns:
            tuple: A tuple containing the timestamp (int), host1 (str), and host2 (str).

        Raises:
            ValueError: If the log line format is invalid.
        """
    parts = line.split()
    if len(parts) != 3:
        raise ValueError(f"Invalid log line format: {line}")
    return int(parts[0]), parts[1], parts[2]


def search_log(file_path, start_time, end_time, search_string, tolerance=300000):
    """
    Searches the log file for adjacent hosts within the specified time range.

    Args:
        file_path (str): The path to the log file.
        start_time (int): The start time in Unix timestamp.
        end_time (int): The end time in Unix timestamp.
        search_string (str): The host to search for.
        tolerance (int, optional): The tolerance in milliseconds for the end time. Defaults to 300000.

    Returns:
        list: A list of adjacent hosts found within the specified time range.
    """
    adjacent_strings = []
    with open(file_path, 'r') as file:
        for line in file:
            timestamp, host1, host2 = parse_log_line(line)
            if timestamp > end_time + tolerance:
                break
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

