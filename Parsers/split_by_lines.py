"""
Split a text file into multiple files based on a batch (# of lines) size.
Output file name: {input_file_name}{_BatchNumber}.txt
"""

import sys

def main(argv):
    try:
        input_file_name = argv[1] if len(argv) > 1 else r".\big.txt"
        batch_size = int(argv[2]) if len(argv) > 2 else 50000
        iteration = 1
        smallfile = None
        
        with open(input_file_name) as bigfile:
            for lineno, line in enumerate(bigfile):
                if lineno % batch_size == 0:
                    if smallfile:
                        smallfile.close()                        
                        iteration = iteration + 1
                    small_filename = input_file_name[:-4] + '_{}.txt'.format(iteration)
                    smallfile = open(small_filename, "w")
                smallfile.write(line)
            if smallfile:
                smallfile.close()

    except ValueError as exception:
        print(exception)


if __name__ == "__main__":
    main(sys.argv)

