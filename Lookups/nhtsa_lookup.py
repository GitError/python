"""
Decode a *.csv file containing a list of VIN# (+ optionally Model Year) into a *.csv with the latest NHTSA data attributes
"""

import csv
import json
import os
import sys

import pandas as pd
import requests as rq

api_url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/'

d_batch_size = 100
d_input_file = r'.\input.csv'
d_output_file = r'.\output.csv'


def main(argv):
    try:
        input_file = argv[1] if len(argv) > 1 else d_input_file
        output_file = argv[2] if len(argv) > 2 else d_output_file
        batch_size = argv[3] if len(argv) > 3 else d_batch_size
        data = get_vin_details_batch(input_file, batch_size)
        data.to_csv(output_file, sep=',', header=True, index=False,
                    line_terminator='\n', encoding='UTF-8', quoting=csv.QUOTE_ALL)
    except ValueError as exception:
        print(exception)


def get_vin_details_batch(input_file_path=d_input_file, batch_size=d_batch_size):
    try:
        vins = pd.read_csv(input_file_path, header=None)
        item_counter = 0
        api_param = ''
        input_vins_count = vins[0].count()
        output_data = pd.DataFrame()
        for index, row in vins.iterrows():
            api_param += str(row[0]) + "," + str(row[1]) + ";"
            item_counter += 1
            if item_counter == batch_size or index == input_vins_count or item_counter >= int(batch_size):
                post_fields = {'format': 'json', 'data': api_param}
                api_call_result = rq.post(api_url, data=post_fields)
                tmp = api_call_result.text.replace('\\u000d\\u000a', '').replace(
                    '\\u000a', '').replace('\\u000d', '')
                data = json.loads(tmp, strict=True)
                output_data = output_data.append(
                    data['Results'], ignore_index=True)
                api_param = ""
                item_counter = 0
        return output_data
    except ValueError as exception:
        print(exception)


if __name__ == "__main__":
    main(sys.argv)
