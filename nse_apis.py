from nsepython import *
import threading
import logging as log

def synchronized(wrapped):
    lock = threading.Lock()

    def _wrap(*args, **kwargs):
        with lock:
            return wrapped(*args, **kwargs)

    return _wrap

@synchronized
def security_wise_archive(from_date, to_date, symbol, series="ALL"):   
    base_url = "https://www.nseindia.com/api/historical/securityArchives"
    url = f"{base_url}?from={from_date}&to={to_date}&symbol={symbol.upper()}&dataType=priceVolumeDeliverable&series={series.upper()}"
    log.info(f"nse security archives url :: {url}")
    log.info(f"{symbol} Started Fetching Data from NSE API");
    response = nsefetch(url);
    log.info(f"{symbol} Completed Fetching Data from NSE API");
    pass
    return response['data'];