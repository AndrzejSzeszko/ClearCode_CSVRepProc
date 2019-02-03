#!/usr/bin/python3.7
import csv
import os
import argparse
import pycountry
from datetime import datetime
from collections import OrderedDict

if __name__ == '__main__':
    input_file_name = 'example_input.csv'

    with open('example_input.csv', 'r') as input_file:
        csv_reader = csv.reader(input_file)

        input_file_name_no_ext = input_file_name[:-4] if input_file_name.endswith('.csv') else input_file_name
        with open(f'{input_file_name_no_ext}_output.csv', 'w') as output_file:
            csv_writer = csv.writer(output_file)

            aux_dict = {}
            for line in csv_reader:
                input_date, state_name, no_of_impr, CTR_prct = line
                no_of_impr = int(no_of_impr)
                output_date = datetime.strptime(input_date, '%m/%d/%Y').strftime('%Y-%m-%d')
                try:
                    country_code = pycountry.countries.get(alpha_2=pycountry.subdivisions.lookup(state_name).country_code).alpha_3
                except LookupError:
                    country_code = 'XXX'
                clicks = round(no_of_impr * float(CTR_prct.strip('%')) / 100)
                if aux_dict.get(f'{output_date}/{country_code}'):
                    aux_dict[f'{output_date}/{country_code}'][0] += no_of_impr
                    aux_dict[f'{output_date}/{country_code}'][1] += clicks
                else:
                    aux_dict[f'{output_date}/{country_code}'] = [no_of_impr, clicks]

            aux_dict = OrderedDict(sorted(aux_dict.items(), key=lambda value: value[0]))
            for key, value in aux_dict.items():
                csv_writer.writerow(key.split('/') + value)
