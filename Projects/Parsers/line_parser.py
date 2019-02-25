'''
Parse line delimited text file {delimiter}{file_name.txt} into multiple files 
'''

import sys

d_input = r'.\input.txt'
d_delimiter = r"--***"


def main(argv):
    try:
        input_file = argv[1] if len(argv) > 1 else d_input
        delimiter = argv[2] if len(argv) > 2 else d_delimiter

        with open(input_file, "r") as input_file:
            data = input_file.read().split(delimiter)
            i = 1
            while i < len(data):
                file_lines = data[i].split('\n')
                output_file = open(file_lines[0], "w+")
                j = 1
                while j < len(file_lines):
                    if len(file_lines[j]) > 0:
                        output_file.write(file_lines[j] + '\n')
                    j += 1
                output_file.close()
                i += 1
    except ValueError as exception:
        print(exception)


if __name__ == "__main__":
    main(sys.argv)

