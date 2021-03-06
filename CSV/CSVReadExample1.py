#CSVReadExample1.py

import csv

with open('python.txt',mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print(f'The Column names are as follows {",".join(row)}')
            line_count += 1

        print(f'\n{row["name"]} works in the {row["department"]} department and was born in {row["birthday_month"]}.')
        line_count +=1
    print(f'Processed {line_count} lines.')          