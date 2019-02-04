#!/usr/bin/python3.7
import csv
import argparse
import pycountry
from datetime import datetime
from collections import OrderedDict


parser = argparse.ArgumentParser(
    description="""
                Converts CSV with fields [mm/dd/YYYY, state_name, no of impressions, CTR%]
                to CSV with fields [YYYY-mm-dd, country_code, no of impressions, no of clicks]
                aggregated by date and country. Separators must be commas.
                """
)
parser.add_argument('input_file_path', type=str, help='Absolute or relative path to input CSV file.')
args = parser.parse_args()


def convert_csv(input_file_path):

    def write_csv_output(csv_reader):
        """
        Takes csv reader and creates output csv file. Returns None.
        """
        input_file_name_without_ext = input_file_path[:-4] if input_file_path.endswith('.csv') else input_file_path
        with open(f'{input_file_name_without_ext}_output.csv', 'w', newline='') as output_file:  # default encoding: utf-8
            csv_writer = csv.writer(output_file, lineterminator='\n')

            aux_dict = {}  # format: {'YYYY-mm-dd/country_code': [impressions, clicks]}
            for i, line in enumerate(csv_reader):
                """
                Lines are skipped if:
                - there is too many values in the line,
                - there is too few values in the line,
                - date is of wrong format,
                - cannot convert no_of_impressions literal into integer,
                - cannot convert CTR literal (stripped out of the % sign) into float.
                """
                try:
                    input_date, state_name, impressions, CTR_prct = line
                    output_date = datetime.strptime(input_date, '%m/%d/%Y').strftime('%Y-%m-%d')
                    impressions = int(impressions)
                    clicks = round(impressions * float(CTR_prct.strip('%')) / 100)
                    country_code = pycountry.countries.get(
                        alpha_2=pycountry.subdivisions.lookup(state_name).country_code
                    ).alpha_3
                except ValueError as VE:  # skip current line and add it's number to skipped_lines list
                    skipped_lines.append(i + 1)
                    print(f'Line {i + 1} skipped: {VE}')
                    continue
                except LookupError:
                    country_code = 'XXX'

                if aux_dict.get(f'{output_date}/{country_code}'):  # if key of given date and country already exist in the aux_dict
                    aux_dict[f'{output_date}/{country_code}'][0] += impressions
                    aux_dict[f'{output_date}/{country_code}'][1] += clicks
                else:
                    aux_dict[f'{output_date}/{country_code}'] = [impressions, clicks]

            aux_dict = OrderedDict(sorted(aux_dict.items(), key=lambda tuple: tuple[0]))
            for date_and_country_string, impr_and_clicks_list in aux_dict.items():
                csv_writer.writerow(date_and_country_string.split('/') + impr_and_clicks_list)

    skipped_lines = []
    try:  # try to open and parse file as utf-8 encoded
        with open(input_file_path, 'r') as input_file:
            write_csv_output(csv.reader(input_file))
    except UnicodeDecodeError:  # try to open and parse file as utf-16 encoded
        with open(input_file_path, 'r', encoding='utf-16') as input_file:
            write_csv_output(csv.reader(input_file))

    return f'Done. \nSkipped lines (total {len(skipped_lines)}): {skipped_lines}'


if __name__ == '__main__':
    print(convert_csv(args.input_file_path))
