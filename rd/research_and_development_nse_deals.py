from nsepythonserver import *
from pandas import *

def nse_largedeals(mode="bulk_deals"):
  payload = nsefetch('https://www.nseindia.com/api/snapshot-capital-market-largedeal')
  if(mode=="bulk_deals"):
    return pd.DataFrame(payload["BULK_DEALS_DATA"])
  if(mode=="short_deals"):
    return pd.DataFrame(payload["SHORT_DEALS_DATA"])
  if(mode=="block_deals"):
    return pd.DataFrame(payload["BLOCK_DEALS_DATA"])

payload = nse_largedeals()
print(payload)