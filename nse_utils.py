import nse_index_stocks_list as nseIndexStocksList
from constants import *
from nse_nifty_indices_stocks_list import getNiftyIndicesStocksList
from filenames import *
from utils import getAutoGeneratedFileName

def getStockListAndFileName(selectedType, fileName, reportsDir):
    if(selectedType == NIFTY_FIFTY):
        fileName = getAutoGeneratedFileName(NIFTY_FIFTY_STOCKS,reportsDir);
        stockList = nseIndexStocksList.getNiftyFiftyStockList();
    elif (selectedType == NIFTY_NEXT_50_LIST):
        fileName = getAutoGeneratedFileName(NIFTY_NEXT_50_LIST_STOCKS),reportsDir;
        stockList = getNiftyIndicesStocksList(NIFTY_NEXT_50_LIST_FILENAME);
    elif (selectedType == NIFTY_100_LIST):
        fileName = getAutoGeneratedFileName(NIFTY_100_LIST_STOCKS,reportsDir);
        stockList = getNiftyIndicesStocksList(NIFTY_100_LIST_FILENAME);
    elif (selectedType == NIFTY_200_LIST):
        fileName = getAutoGeneratedFileName(NIFTY_200_LIST_STOCKS,reportsDir);
        stockList = getNiftyIndicesStocksList(NIFTY_200_LIST_FILENAME);
    elif (selectedType == NIFTY_500_LIST):
        fileName = getAutoGeneratedFileName(NIFTY_500_LIST_STOCKS,reportsDir);
        stockList = getNiftyIndicesStocksList(NIFTY_500_LIST_FILENAME);
    elif (selectedType == NIFTY_MICRO_CAP_250_LIST):
        fileName = getAutoGeneratedFileName(NIFTY_MICRO_CAP_250_LIST_STOCKS,reportsDir);
        stockList = getNiftyIndicesStocksList(NIFTY_MICRO_CAP_250_LIST_FILENAME);
    elif (selectedType == NIFTY_MID_CAP_50_LIST):
        fileName = getAutoGeneratedFileName(NIFTY_MID_CAP_50_LIST_STOCKS,reportsDir);
        stockList = getNiftyIndicesStocksList(NIFTY_MID_CAP_50_LIST_FILENAME);
    elif (selectedType == NIFTY_MID_CAP_100_LIST):
        fileName = getAutoGeneratedFileName(NIFTY_MID_CAP_100_LIST_STOCKS,reportsDir);
        stockList = getNiftyIndicesStocksList(NIFTY_MID_CAP_100_LIST_FILENAME);
    elif (selectedType == NIFTY_MID_CAP_150_LIST):
        fileName = getAutoGeneratedFileName(NIFTY_MID_CAP_150_LIST_STOCKS,reportsDir);
        stockList = getNiftyIndicesStocksList(NIFTY_MID_CAP_150_LIST_FILENAME);
    elif (selectedType == NIFTY_MID_CAP_SELECT_LIST):
        fileName = getAutoGeneratedFileName(NIFTY_MID_CAP_SELECT_LIST_STOCKS,reportsDir);
        stockList = getNiftyIndicesStocksList(NIFTY_MID_CAP_SELECT_LIST_FILENAME);
    elif (selectedType == NIFTY_MID_SMALL_CAP_400_LIST):
        fileName = getAutoGeneratedFileName(NIFTY_MID_SMALL_CAP_400_LIST_STOCKS,reportsDir);
        stockList = getNiftyIndicesStocksList(NIFTY_MID_SMALL_CAP_400_LIST_FILENAME);
    elif (selectedType == NIFTY_SMALL_CAP_50_LIST):
        fileName = getAutoGeneratedFileName(NIFTY_SMALL_CAP_50_LIST_STOCKS,reportsDir);
        stockList = getNiftyIndicesStocksList(NIFTY_SMALL_CAP_50_LIST_FILENAME);
    elif (selectedType == NIFTY_SMALL_CAP_100_LIST):
        fileName = getAutoGeneratedFileName(NIFTY_SMALL_CAP_100_LIST_STOCKS,reportsDir);
        stockList = getNiftyIndicesStocksList(NIFTY_SMALL_CAP_100_LIST_FILENAME);
    elif (selectedType == NIFTY_SMALL_CAP_250_LIST):
        fileName = getAutoGeneratedFileName(NIFTY_SMALL_CAP_250_LIST_STOCKS,reportsDir);
        stockList = getNiftyIndicesStocksList(NIFTY_SMALL_CAP_250_LIST_FILENAME);
    elif (selectedType == NIFTY_BANK):
        fileName = getAutoGeneratedFileName(NIFTY_BANK_STOCKS,reportsDir);
        stockList = NIFTY_BANK_LIST;
    else:
        fileName = getAutoGeneratedFileName(NIFTY_FIFTY_STOCKS,reportsDir);
        stockList = nseIndexStocksList.getNiftyFiftyStockList();
    
    myDict = {"fileName" :"", "stockList":[]}
    myDict["fileName"] = fileName;
    myDict["stockList"] = stockList;
    return myDict;


def getDictkeyAndValue(key,data):
    if key in data:
        return data[key] if data[key] else "";
    else:
        return '';
