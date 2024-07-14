import logging as log
from nsepythonserver import *
from pandas import *
import nse_report_writer as nseReportWriter;
import threading

import utils

def synchronized(wrapped):
    lock = threading.Lock()

    def _wrap(*args, **kwargs):
        with lock:
            return wrapped(*args, **kwargs)

    return _wrap

@synchronized
def nse_largedeals_customization(deal,fileName,fromDate,toDate):
  url = 'https://www.nseindia.com/api/historical/';
  modifiedUrl = url + deal + '?' + 'from='+fromDate+ '&to='+toDate;
  log.info(url);
  payload = nsefetch(modifiedUrl)
  print(payload)
  newFileName  = fileName + "_" + deal +"_custom" + ".csv";
  nseReportWriter.writeDealsDataToCSV(newFileName,deal,payload['data'])
  pass

def nse_largedeals(listOfDeals, fileName, noOfDaysFromPresent):
  toDate = utils.getTodayDate();
  fromDate= utils.getPastWeekDate(noOfDaysFromPresent);
  for deal in listOfDeals:
    nse_largedeals_customization(deal,fileName,fromDate, toDate);
  pass

# nse_largedeals(["bulk-deals","block-deals","short-selling"],"deals",7)
# nse_largedeals_customization("bulk-deals","deals","07-07-2024","14-07-2024");
# nse_largedeals_customization("block-deals","deals","07-07-2024","14-07-2024");
# nse_largedeals_customization("short-selling","deals","07-07-2024","14-07-2024");