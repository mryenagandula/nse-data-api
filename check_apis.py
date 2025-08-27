from nsepython import *

def checking_internet_connection():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        if response.status_code == 200:
            print("✅ Internet connection is active.")
            return True
        else:
            print("❌ Internet connection is not active.")
            return False
    except Exception as e:
        print(f"❌ Error occurred while checking internet connection: {e}")
        return False

def security_wise_archive_api_health():
    message = None;
    print("Started Checking Nse API Securewise API Health")
    try:
        url = "https://www.nseindia.com/api/historical/securityArchives?from=28-07-2025&to=27-08-2025&symbol=ULTRACEMCO&dataType=priceVolumeDeliverable&series=ALL"
        response = nsefetch(url);
        print(f"Response Status Code: {response.status_code}")
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)

        if "Resource not found" in response.text:
            print("Nse API Securewise API Health is not good")
            print("⚠️ Resource not found in HTML content.")
            message = "⚠️ Resource not found in HTML content."
        else:
            print("✅ Resource fetched successfully.")
            message = "✅ Resource fetched successfully."
            message = "SUCCESS";
            # Process response.text or response.content

    except requests.exceptions.HTTPError as http_err:
        print("Nse API Securewise API Health is not good")
        print(f"HTTP error occurred: {http_err}")  # e.g., 404 Not Found
        message = (f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print("Nse API Securewise API Health is not good")
        print(f"Request failed: {err}")  # Network issues, timeouts, etc.
        message = f"Request failed: {err}"
    print("Completed Checking Nse API Securewise API Health")
    return message;

def large_deals_api_health():
    message = None;
    print("Started Checking Nse API Large Deals API Health")
    try:
        url = "https://www.nseindia.com/api/snapshot-capital-market-largedeal"
        response = nsefetch(url);
        print(f"Response Status Code: {response.status_code}")
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)

        if "Resource not found" in response.text:
            print("Nse API Large Deals API Health is not good")
            print("⚠️ Resource not found in HTML content.")
            message = "⚠️ Resource not found in HTML content."
        else:
            print("✅ Resource fetched successfully.")
            message = "✅ Resource fetched successfully."
            message = "SUCCESS";
            # Process response.text or response.content

    except requests.exceptions.HTTPError as http_err:
        print("Nse API Large Deals API Health is not good")
        print(f"HTTP error occurred: {http_err}")  # e.g., 404 Not Found
        message = (f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print("Nse API Large Deals API Health is not good")
        print(f"Request failed: {err}")  # Network issues, timeouts, etc.
        message = f"Request failed: {err}"
    print("Completed Checking Nse API Large Deals API Health")
    return message;
