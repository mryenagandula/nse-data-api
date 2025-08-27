import requests

# Define the endpoint URL
url = "https://www.nseindia.com/api/historical/bulk-deals"

# Define query parameters
params = {
    "from": "28-07-2025",
    "to": "27-08-2025"
}

# Define headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.nseindia.com/"
}

# Start a session to handle cookies
session = requests.Session()
session.headers.update(headers)

# Make the GET request
response = session.get(url, params=params)

# Check response
if response.status_code == 200:
    try:
        data = response.json()
        print("✅ Data received:")
        print(data)
    except ValueError:
        print("⚠️ Response is not in JSON format.")
        print(response.text)
else:
    print(f"❌ Failed with status code: {response.status_code}")
