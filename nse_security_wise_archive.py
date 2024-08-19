import threading
from nsepython import *
import nse_report_writer as nseReportWriter
import nse_apis as nseApis
import utils as utils;
import constants as constants
import logging as log

def synchronized(wrapped):
    lock = threading.Lock()

    def _wrap(*args, **kwargs):
        with lock:
            return wrapped(*args, **kwargs)

    return _wrap

@synchronized
def nseGenerateSecurityWiseArchiveReport(fileName,stockList, selectedType,noOfDaysFromPresent,input):
    toDate = utils.getTodayDate();
    fromDate= utils.getPastWeekDate(noOfDaysFromPresent);
    log.info(f"no of days from present date is {noOfDaysFromPresent} days")
    log.info(f"Report is generating is Started and the period is from {fromDate} to {toDate}");
    log.info(f"List of {selectedType} Stock Symbols are displaying below Please check");
    log.info(stockList);
    listOfDics = [];
    log.info(f"Started Process for getting the list of nse security wise archive data.")
    for stockSymbol in stockList :
        try:
            log.info(f"{stockSymbol} Stock Started fetching the data from server.....")
            result = nseApis.security_wise_archive(fromDate, toDate,stockSymbol)
            listOfDics.extend(result);
            log.info(f"{stockSymbol} Stock Completed fetching the data from server.....")
        except Exception as e:
            log.info(f"Something went wrong due to exception {e}")
            continue;

    log.info("Completed Process for getting the list of nse security wise archive data.")
    log.info("Number of records fetched from Api is ");
    log.info(f"Started writing Security wise archive Data to CSV and filename is {fileName}");
    nseReportWriter.writeDataToCSV(fileName+".csv",constants.HEADERS,listOfDics)
    withFilters = bool(input['withFilters']);
    filterOptions = input['filterOptions'];
    percentages = filterOptions['percentages'];
    if withFilters:
        filtered_result =[];
        filtered_result = list(filter(lambda d: getCondition(d,percentages) , listOfDics))
        nseReportWriter.writeFiltersDataToCSV(fileName+"_filtered"+".csv",constants.FILTERS_HEADERS,filtered_result)
    log.info(f"Completed writing Security wise archive Data to CSV and filename is {fileName}");
    log.info(f"Report is generating is completed and the period is from {fromDate} to {toDate}");
    pass

def getCondition(d,percentages):
    conditon = d['COP_DELIV_PERC'] != '-' and int(d['COP_DELIV_PERC']) is not None ;
    for percentage in percentages:
        if percentage['operator'] == '<=':
            conditon = conditon and int(d['COP_DELIV_PERC']) <= percentage['percentage'];
        if percentage['operator'] == '>=':
            conditon = conditon and int(d['COP_DELIV_PERC']) >= percentage['percentage'];
        if percentage['operator'] == '<':
            conditon = conditon and int(d['COP_DELIV_PERC']) < percentage['percentage'];
        if percentage['operator'] == '>':
            conditon = conditon and int(d['COP_DELIV_PERC']) > percentage['percentage'];
        if percentage['operator'] == '!=':
            conditon = conditon and int(d['COP_DELIV_PERC']) != percentage['percentage'];
        if percentage['operator'] == '==':
            conditon = conditon and int(d['COP_DELIV_PERC']) == percentage['percentage'];
    return conditon;