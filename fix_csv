import csv
import re

def convert_duration(filename):
    arr = []
    with open(f"{filename}.csv", 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            try:
                row[0] = re.findall(r'\d+', row[0])[0]
                row[9] = re.findall(r'\d+', row[9])[0]
                arr.append(row)
            except:
                arr.append(row)

    with open(f"{filename}_new.csv", 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        for row in arr:
            csv_writer.writerow(row)


convert_duration('data/netflix_titles')
convert_duration('data/hulu_titles')
convert_duration('data/disney_plus_titles')
convert_duration('data/amazon_prime_titles')