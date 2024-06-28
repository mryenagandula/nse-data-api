from nsepythonserver import *
from pandas import *
import nse_report_writer as nseReportWriter;
import threading

def synchronized(wrapped):
    lock = threading.Lock()

    def _wrap(*args, **kwargs):
        with lock:
            return wrapped(*args, **kwargs)

    return _wrap

@synchronized
def nse_largedeals(listOfDeals,fileName):
  payload = nsefetch('https://www.nseindia.com/api/snapshot-capital-market-largedeal')
  for deal in listOfDeals:
    newFileName  = fileName + "_" + deal + ".csv";
    nseReportWriter.writeDealsDataToCSV(newFileName,deal,payload[deal])
  pass

# nse_largedeals(["BULK_DEALS_DATA","SHORT_DEALS_DATA","BLOCK_DEALS_DATA"],"deals")
