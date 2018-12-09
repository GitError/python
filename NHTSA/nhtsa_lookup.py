"""Get NHTSA detail for a list of VIN# in csv format [VIN, Model Year]"""
import sys, json, csv
import pandas as pd
import requests as rq


NHTSA_API_URL = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/'
BATCH_SIZE = 5
DEFAULT_INPUT_FILE = 'input.csv'
DEFAULT_OUTPUT_FILE = 'output.csv'


def main(argv):
    try:
        vin_list = argv[1] if len(argv) > 1 else DEFAULT_INPUT_FILE
        output = argv[2] if len(argv) > 2 else DEFAULT_OUTPUT_FILE

        data = get_vin_details_batch(vin_list, BATCH_SIZE)
        data.to_csv(output, sep=',', header=True, index=False, 
            line_terminator='\n', encoding='UTF-8', quoting=csv.QUOTE_ALL)
    except ValueError as exception:
        print(exception)


def get_vin_details_batch(input_file_path, batch_size):
    try:
        vins = pd.read_csv(input_file_path, header=None)
        item_counter = 0
        api_param = ''
        input_vins_count = vins[0].count()
        output_data = pd.DataFrame()
        for index, row in vins.iterrows():
            api_param += str(row[0]) + "," + str(row[1]) + ";"
            item_counter = item_counter + 1
            if item_counter == batch_size or index == input_vins_count:
                post_fields = {'format': 'json', 'data': api_param}
                api_call_result = rq.post(NHTSA_API_URL, data=post_fields)
                tmp = api_call_result.text.replace('\\u000d\\u000a', '').replace('\\u000a', '').replace('\\u000d', '')
                data = json.loads(tmp, strict=True)
                output_data = output_data.append(data['Results'], ignore_index=True)
                api_param = ""
                item_counter = 0
        return output_data
    except ValueError as exception:
        print(exception)


if __name__ == "__main__":
    main(sys.argv)

