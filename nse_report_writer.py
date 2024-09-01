import csv
import logging as log
from nse_utils import getDictkeyAndValue
from constants import DEALS_HEADERS,DEALS_CUSTOM_HEADERS
import nse_data_consecutive_days as nse_consecutive

def writeDataToCSV(fileName: str,headers, result) :
    with open(fileName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f);
        log.info("Started writing data to CSV");
        writer.writerow(headers);
        for data in result :
            writer.writerow([
                getDictkeyAndValue("_id",data),
                getDictkeyAndValue("CH_SYMBOL",data),
                getDictkeyAndValue("CH_SERIES",data),
                getDictkeyAndValue("CH_MARKET_TYPE",data),
                getDictkeyAndValue("CH_TRADE_HIGH_PRICE",data),
                getDictkeyAndValue("CH_TRADE_LOW_PRICE",data),
                getDictkeyAndValue("CH_OPENING_PRICE",data),
                getDictkeyAndValue("CH_CLOSING_PRICE",data),
                getDictkeyAndValue("CH_LAST_TRADED_PRICE",data),
                getDictkeyAndValue("CH_PREVIOUS_CLS_PRICE",data),
                getDictkeyAndValue("CH_TOT_TRADED_QTY",data),
                getDictkeyAndValue("CH_TOT_TRADED_VAL",data),
                getDictkeyAndValue("CH_52WEEK_HIGH_PRICE",data),
                getDictkeyAndValue("CH_52WEEK_LOW_PRICE",data),
                getDictkeyAndValue("COP_DELIV_QTY",data),
                getDictkeyAndValue("COP_DELIV_PERC",data),
                getDictkeyAndValue("CH_TOTAL_TRADES",data),
                getDictkeyAndValue("VWAP",data),
                getDictkeyAndValue("CH_TIMESTAMP",data),
                getDictkeyAndValue("CH_ISIN",data),
                getDictkeyAndValue("createdAt",data),
                getDictkeyAndValue("updatedAt",data),
                getDictkeyAndValue("TIMESTAMP",data),
                getDictkeyAndValue("mTIMESTAMP",data)
            ]);
        log.info("Completed writing data to CSV")
        log.info(f"Successfully Saved the file to specified directory {fileName}")


def writeFiltersDataToCSV(fileName: str,headers, result) :
    with open(fileName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f);
        log.info("Started Filters writing data to CSV");
        writer.writerow(headers);
        for data in result :
            writer.writerow([
                getDictkeyAndValue("mTIMESTAMP",data),
                getDictkeyAndValue("CH_SYMBOL",data),
                getDictkeyAndValue("COP_DELIV_PERC",data),
                getDictkeyAndValue("COP_DELIV_QTY",data),
                getDictkeyAndValue("CH_TOT_TRADED_QTY",data),
                getDictkeyAndValue("CH_OPENING_PRICE",data),
                getDictkeyAndValue("CH_TRADE_HIGH_PRICE",data),
                getDictkeyAndValue("CH_TRADE_LOW_PRICE",data),
                getDictkeyAndValue("CH_CLOSING_PRICE",data),
                getDictkeyAndValue("CH_52WEEK_HIGH_PRICE",data),
                getDictkeyAndValue("CH_52WEEK_LOW_PRICE",data),
                getDictkeyAndValue("CH_TOTAL_TRADES",data),
                getDictkeyAndValue("CH_LAST_TRADED_PRICE",data),
                getDictkeyAndValue("CH_PREVIOUS_CLS_PRICE",data),
                getDictkeyAndValue("VWAP",data),
                getDictkeyAndValue("CH_TIMESTAMP",data),
                getDictkeyAndValue("CH_ISIN",data),
                getDictkeyAndValue("createdAt",data),
                getDictkeyAndValue("updatedAt",data),
                getDictkeyAndValue("TIMESTAMP",data),
                getDictkeyAndValue("CH_TOT_TRADED_VAL",data),
                getDictkeyAndValue("CH_SERIES",data)
            ]);
        log.info("Completed Filters writing data to CSV")
        log.info(f"Successfully Saved the filters file to specified directory {fileName}")

def writeFiltersConsecutiveDataToCSV(fileName1: str, fileName2,headers, result, consecutiveDays, percentages) :
    log.info("Completed consecutive days writing data to CSV")
    consecutiveRecords = nse_consecutive.consecutive_days(fileName2,result,percentages,consecutiveDays); 
    print(consecutiveRecords)
    writeFiltersDataToCSV(fileName1,headers, consecutiveRecords); 
    log.info(f"Successfully Saved the consecutive days file to specified directory {fileName1} - {fileName2}")
        

def writeDealsDataToCSV(fileName: str,deal:str, result) :
    with open(fileName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f);
        log.info(f"Started Deals-{deal} writing data to CSV");
        writer.writerow(DEALS_HEADERS);
        for data in result :
            writer.writerow(data.values());
        log.info(f"Completed Deals-{deal} writing data to CSV")
        log.info(f"Successfully Saved {deal} the file to specified directory {fileName}")


def writeDealsCustomDataToCSV(fileName: str,deal:str, result) :
    with open(fileName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f);
        log.info(f"Started Deals-{deal} writing data to CSV");
        writer.writerow(DEALS_CUSTOM_HEADERS);
        for data in result :
             writer.writerow([
                getDictkeyAndValue("_id",data),
                getDictkeyAndValue("BD_DT_DATE",data),
                getDictkeyAndValue("BD_SYMBOL",data),
                getDictkeyAndValue("BD_SCRIP_NAME",data),
                getDictkeyAndValue("BD_CLIENT_NAME",data),
                getDictkeyAndValue("BD_BUY_SELL",data),
                getDictkeyAndValue("BD_QTY_TRD",data),
                getDictkeyAndValue("BD_TP_WATP",data),
                getDictkeyAndValue("createdAt",data),
                getDictkeyAndValue("updatedAt",data),
            ]);
        log.info(f"Completed Deals-{deal} writing data to CSV")
        log.info(f"Successfully Saved {deal} the file to specified directory {fileName}");