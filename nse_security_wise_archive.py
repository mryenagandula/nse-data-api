from nsepython import *
import nse_report_writer as nseReportWriter
import nse_index_stocks_list as nseIndexStocksList
import nse_apis as nseApis
import utils as utils;
import constants as constants
import threading

def nseGenerateSecurityWiseArchiveReport():
    toDate = utils.getTodayDate();
    fromDate= utils.getPastWeekDate();
    print("Report is generating is Started and the period is from ",fromDate, " to ", toDate);
    niftyFiftyList = nseIndexStocksList.getNiftyFiftyStockList();
    print("List of Nifty Fifty Stock Symbols are displaying below Please check");
    print(niftyFiftyList);
    print();
    listOfDics = [];
    print("Started Process for getting the list of nse security wise archive data.")
    for stockSymbol in niftyFiftyList :
        print(stockSymbol,"Stock Symbol Started fetching the data from server.....")
        result = nseApis.security_wise_archive(fromDate, toDate,stockSymbol)
        listOfDics.extend(result);
        print(stockSymbol,"Stock Symbol Completed fetching the data from server.....")

    print("Completed Process for getting the list of nse security wise archive data.")
    print("Number of records fetched from Api is ",listOfDics.__sizeof__);
    fileName = utils.getAutoGeneratedFileName();
    print("Started writing Security wise archive Data to CSV and filename is ",fileName);
    nseReportWriter.writeDataToCSV(fileName,constants.NIFTY_FIFTY_HEADERS,listOfDics)
    print("Completed writing Security wise archive Data to CSV and filename is ",fileName);
    print("Report is generating is completed and the period is from ",fromDate, " to ", toDate);

