# Parsers

## line_parser.py

A simple script that breaks a *.txt that's line-delimited '{delimiter}{file_name.txt}' into multiple *.txt files

### Script Usage

python line_parser.py input_file_path.txt [delimiter]

#### Defaults

- input_file_path: \\.input.csv
- delimiter: --\*\*\*{file_name.txt}
- output files path: \\.