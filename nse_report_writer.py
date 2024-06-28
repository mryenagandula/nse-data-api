import csv
import logging as log
from nse_utils import getDictkeyAndValue
from constants import DEALS_HEADERS

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

def writeDealsDataToCSV(fileName: str,deal:str, result) :
    with open(fileName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f);
        log.info(f"Started Deals-{deal} writing data to CSV");
        writer.writerow(DEALS_HEADERS);
        for data in result :
            writer.writerow(data.values());
        log.info(f"Completed Deals-{deal} writing data to CSV")
        log.info(f"Successfully Saved {deal} the file to specified directory {fileName}")