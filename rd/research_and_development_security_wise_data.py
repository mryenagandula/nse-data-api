from nsepython import nsefetch
import pandas as pd
import requests as request
# https://www.nseindia.com/api/historical/securityArchives?from=23-11-2024&to=30-11-2024&symbol=YESBANK&dataType=priceVolumeDeliverable&series=ALL

def security_wise_archive(from_date, to_date, symbol, series="ALL"):  
    print("Adfffffffffffffffffffffffffffff") 
    base_url = "https://www.nseindia.com/api/historical/securityArchives"
    url = f"{base_url}?from={from_date}&to={to_date}&symbol={symbol.upper()}&dataType=priceVolumeDeliverable&series={series.upper()}"
    print(url)
    # headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'}
    # payload = request.get(url, headers=headers);
    payload = request.get('https://www.nseindia.com/api/historical/securityArchives?from=10-09-2024&to=10-12-2024&symbol=INFY&dataType=priceVolumeDeliverable&series=ALL')
    print(payload.json())
    return pd.DataFrame(payload['data'])

def security_wise_archiveqq(from_date, to_date, symbol, series="ALL"):   
    base_url = "https://www.nseindia.com/api/historical/securityArchives"
    url = f"{base_url}?from={from_date}&to={to_date}&symbol={symbol.upper()}&dataType=priceVolumeDeliverable&series={series.upper()}"
    payload = nsefetch(url)
    print(payload)
    return pd.DataFrame(payload['data'])

security_wise_archive('01-11-2024', '29-11-2024', 'SBIN')