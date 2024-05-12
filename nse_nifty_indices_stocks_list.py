import csv
import os

def getNiftyIndicesStocksList(fileName):
    stockList = [];
    with open(os.path.join('nifty_indices', fileName), 'r') as file:
        csv_reader = csv.DictReader(file);
        for row in csv_reader:
            stockList.append(row['Symbol']);
    return stockList;