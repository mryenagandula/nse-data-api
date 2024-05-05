from nsepython import *
import threading
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
    print(symbol," Started Fetching Data from NSE API");
    response = nsefetch(url);
    print(symbol," Completed Fetching Data from NSE API");
    pass
    return response['data'];