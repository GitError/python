## NHTSA Lookup
A simple script using [NHTSA Batch API](https://vpic.nhtsa.dot.gov/api/) to decode *.csv containing a list of VINs into a *.csv with the latest NHTSA attributes (UTF-8 format).

### Input file
- *.csv
- no header
- columns: vin#, model year


| VIN# (required)   | Model Year (optional)
| ------------------|-----------------------|
| WBAYB6C58DC997953 | 2015
| 1GCRCREA2BZ230013 | 2016
| 1J4PN2GK0BW516677 | 2016

### Output file
- *.csv
- header (column list)
- columns: 150+ (the latest definition)


## Script Usage
python nhtsa_lookup.py input_file_path.csv output_file_path.csv batch_size


### Defaults
- input_file_path:    \\.input.csv
- output_file_path:    \\.output.csv
- batch_size_int: 10