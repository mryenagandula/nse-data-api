import csv

def writeDataToCSV(fileName: str,headers, result) :
    with open(fileName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f);
        print("Started writing data to CSV");
        writer.writerow(headers);
        for data in result :
            writer = csv.DictWriter(f, data.keys())
            writer.writerow(data);
        print("Completed writing data to CSV")
        print("Successfully Saved the file to specified directory ", fileName)