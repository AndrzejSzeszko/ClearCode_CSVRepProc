# ClearCode internship task 2019 - CSVReportProcessing
## Description:
This project basically converts CSV files (with commas as separators) having rows of the following values:
```
mm/dd/YYYY, ISO 3166-2 subdivision, number of impressions, CTR as %
eg.: 01/21/2019,Mandiana,883,0.38%
     01/21/2019,Lola,76,0.78%
```
into differently formatted CSV (also with comma separated values) and merge rows that belongs to the same country and date:
```
YYYY-mm-dd, ISO 3166 country alpha3 code, number of impressions, number of clicks
eg.: 2019-01-21,GIN,959,4
```

## QuickStart
1) Clone project on your machine.
2) Create and activate virtual environment and install required packages.
3) In terminal navigate to directory containing CSVRepProc.py.
4) Run script using "python3.7 CSVRepProc.py example_input_utf8.csv". Notice the output in the terminal saying that basically everything went successfully. New file called "example_input_utf8_output.csv" should appear in current directory.
5) Compare content of this file with "example_output.csv" delivered by ClearCode.
##### Moreover:
6) Run script with other delivered files passed as an argument ("example_input_utf16.csv" and "example_input_invalid.csv").<br>
7) Notice (or not) different terminal outputs and different content of newly created files.

## SlowStart
This checklist assumes that you are using Ubuntu 16.04 or higher, and have python3.7, git, pip and some stuff for creating virtual environments installed. And you can use it a little.
1) Navigate to directory you want to place project in:
    ```
    $ cd path/to/directory/of/your/choice
    ```
2) Clone project to your machine:
    ```angular2html
    $ git clone https://github.com/AndrzejSzeszko/ClearCode_CSVRepProc.git
    ```
3) Create and activate new virtual environment using tool and location of your choice. Remember to use python3.7 as an interpreter.  You can skip this step if you don't care about python packages conflicts (OK, I know you do)
4) Navigate to directory containing CSVRepProc.py:
    ```angular2html
    (env)$ cd path/to/directory/containing/mentioned/file
    ```
5) Chosen location should also have "requirements.txt" contained. Install required modules using pip:
    ```angular2html
    (env)$ pip install -r requirements.txt
    ```
6) Run CSVRepProc.py and pass to it some csv file you want to convert:
    ```commandline
    (env)$ python3.7 CSVRepProc.py relative/or/absolute/path/to/input/csv/file
    eg.: (env)$ python3.7 CSVRepProc.py example_input_utf8.csv
    ```
    This command creates output file named "<input_file_name>_output.csv" in current directory.
    In terminal there should appear "Done." message, and info about which lines have been skipped because of errors detected, and what those errors was. Criteria for claiming line invalid are described directly in source code docstrings.