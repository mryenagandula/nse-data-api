import csv
import logging as log

def writeDataToCSV(fileName: str,headers, result) :
    with open(fileName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f);
        log.info("Started writing data to CSV");
        writer.writerow(headers);
        for data in result :
            writer = csv.DictWriter(f, data.keys())
            writer.writerow(data);
        log.info("Completed writing data to CSV")
        log.info(f"Successfully Saved the file to specified directory {fileName}")