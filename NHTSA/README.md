### NHTSA Lookup
A simple script utilizing public NHTAS Batch API to decode a list of VIN# into a *csv output file.

NHTSA Batch API - https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/

### Usage
nhtsa_lookup.py input_file_path.csv output_file_path.csv batch_size
note: output file and batch size are optional; defaults: output.csv, 50
