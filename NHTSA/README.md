## NHTSA Lookup
A simple script using NHTSA Batch API to decode a file (*.csv) containing a list of VINs into an output (*.csv) file composed of the latest NHTSA attributes.

Input file structure:
- *.csv
- no header
- columns: vin#, model year


| VIN# (required)   | Model Year (optional)
| ------------------|-----------------------|
| WBAYB6C58DC997953 | 2015
| 1GCRCREA2BZ230013 | 2016
| 1J4PN2GK0BW516677 | 2016

Output file structure:
- *.csv
- header
- columns: 150+ (the latest definition)


## Script Usage
python3 nhtsa_lookup.py input_file_path.csv output_file_path.csv batch_size_int 

##### note: output file and batch size arguments are optional; defaults: \\.output.csv, 10
