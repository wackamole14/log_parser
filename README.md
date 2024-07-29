# Log Parser

A simple Python script to parse log files and find adjacent host connections within a given timestamp range.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/wackamole14/log_parser.git
    cd log_parser
    ```

## Usage

1. Run the script by passing the file name, the start time (Unix timestamps), end time (Unix timestamps), and the host to search for during the given period, to the program:
    ```sh
    python log_parser.py <file_path> <file_name> <start_time_unix> <end_time_unix> <search_host_string>
    ```

    Example:
    ```sh
    python log_parser.py input-file-10000__1_.txt 1366815793 1366815811 Kadan
    ```

3. The script will output the adjacent hosts.

## Example

Given a log file with the following content:

1565647204351 Eron Matina
1565647205599 Keimy Dmetri
1565647212986 Tyreonna Rehgan
1565647228897 Heera Eron
1565647246869 Jeremyah Morrigan

Running the command:
```sh
python log_parser.py input-file-10000__1_.txt 1565647204351 1565647228897 'Eron'

Will output:

['Matina', 'Heera']

```

## Using the Makefile

You can also use the provided `Makefile` to run the script and tests.

### Running the Script

To run the script using the `Makefile`, use the `run` target. You need to provide the `start`, `end`, and `string` variables:

```sh
make run start=<start_time_unix> end=<end_time_unix> host=<search_host_string>
```

## Running Tests

To run the tests using the `Makefile`, use the `test` target:

```sh
make test
```

