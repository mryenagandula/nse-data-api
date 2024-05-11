from nsepython import *
import nse_report_writer as nseReportWriter
import nse_index_stocks_list as nseIndexStocksList
import nse_apis as nseApis
import utils as utils;
import constants as constants
import logging as log

def nseGenerateSecurityWiseArchiveReport(fileName,stockList, selectedType):
    toDate = utils.getTodayDate();
    fromDate= utils.getPastWeekDate();
    log.info(f"Report is generating is Started and the period is from {fromDate} to {toDate}");
    log.info(f"List of {selectedType} Stock Symbols are displaying below Please check");
    log.info(stockList);
    listOfDics = [];
    log.info(f"Started Process for getting the list of nse security wise archive data.")
    for stockSymbol in stockList :
        log.info(f"{stockSymbol} Stock Started fetching the data from server.....")
        result = nseApis.security_wise_archive(fromDate, toDate,stockSymbol)
        listOfDics.extend(result);
        log.info(f"{stockSymbol} Stock Completed fetching the data from server.....")

    log.info("Completed Process for getting the list of nse security wise archive data.")
    log.info("Number of records fetched from Api is ");
    log.info(f"Started writing Security wise archive Data to CSV and filename is {fileName}");
    nseReportWriter.writeDataToCSV(fileName,constants.HEADERS,listOfDics)
    log.info(f"Completed writing Security wise archive Data to CSV and filename is {fileName}");
    log.info(f"Report is generating is completed and the period is from {fromDate} to {toDate}");