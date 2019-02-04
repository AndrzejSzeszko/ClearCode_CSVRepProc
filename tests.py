#!/usr/bin/python3.7
import unittest
import csv
import os
from CSVRepProc import convert_csv


class CSVConvertTestCase(unittest.TestCase):
    """
    Compares content of 'example_output.csv' file with content of files
    generated form 'example_input_utf8.csv' and 'example_input_utf16.csv'
    Running:
        1) navigate to directory containning this file
        2) python -m unitest tests.py
    """
    def setUp(self):
        self.test_input_file_utf8 = 'example_input_utf8.csv'
        self.test_input_file_utf16 = 'example_input_utf16.csv'

    def tearDown(self):
        os.remove('example_input_utf8_output.csv')
        os.remove('example_input_utf16_output.csv')

    def test_convert_csv(self):
        convert_csv(self.test_input_file_utf8)
        with open('example_output.csv') as reference_file:
            ref_csv_reader = csv.reader(reference_file)
            with open('example_input_utf8_output.csv') as utf8_output_file:
                utf8_reader = csv.reader(utf8_output_file)
                for ref, utf8 in zip(ref_csv_reader, utf8_reader):
                    self.assertEqual(ref, utf8)

        convert_csv(self.test_input_file_utf16)
        with open('example_output.csv') as reference_file:
            ref_csv_reader = csv.reader(reference_file)
            with open('example_input_utf16_output.csv') as utf16_output_file:
                utf16_reader = csv.reader(utf16_output_file)
                for ref, utf16 in zip(ref_csv_reader, utf16_reader):
                    self.assertEqual(ref, utf16)


if __name__ == '__main__':
    unittest.main()
