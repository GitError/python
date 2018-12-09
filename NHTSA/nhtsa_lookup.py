import sys, os, json, csv
import pandas as pd
import requests as rq


NHTSA_API_URL = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/'
DEFAULT_BATCH_SIZE = 5
DEFAULT_INPUT_FILE = r'.\input.csv'
DEFAULT_OUTPUT_FILE = r'.\output.csv'


def main(argv):
    try:
        input_file = argv[1] if len(argv) > 1 else DEFAULT_INPUT_FILE
        output_file = argv[2] if len(argv) > 2 else DEFAULT_OUTPUT_FILE
        batch = argv[3] if len(argv) > 3 else DEFAULT_BATCH_SIZE 
        data = get_vin_details_batch(input_file, batch)
        data.to_csv(output_file, sep=',', header=True, index=False, 
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
            item_counter += 1
            if item_counter == batch_size or index == input_vins_count or item_counter >= int(batch_size): 
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

