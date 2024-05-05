import requests
import csv
from io import StringIO
import logging as log


def getNiftyFiftyStockList():
    # URL for the CSV data
    url = "https://archives.nseindia.com/content/indices/ind_nifty50list.csv";

    # Fetch the CSV data
    response = requests.get(url)
    csv_content = response.content.decode("utf-8")

    # Parse the CSV content
    csv_reader = csv.reader(StringIO(csv_content))
    header = next(csv_reader)  # Read the header row

    log.info(f"Column Names: {header}")

    niftyFiftyStocksList = [];
    for row in csv_reader:
        niftyFiftyStocksList.append(row[2])

    niftyFiftyStocksList.sort();
    return niftyFiftyStocksList;
