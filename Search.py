import requests
from conf import apikey
from Cleaner import *


def KeywordSearch(keyword):
    try:
        response = requests.get("https://services.nvd.nist.gov/rest/json/cves/2.0",
                                headers={"apiKey": apikey},
                                params={"keywordSearch": keyword, "noRejected": ""})
        response.raise_for_status()
        return cveCleaner(response.json())
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error calling API: {e}")
        return None
    # return the json response


def MatchstringSearch(MatchString):
    try:
        response = requests.get("https://services.nvd.nist.gov/rest/json/cves/2.0",
                                headers={"apiKey": apikey},
                                params={"virtualMatchString": MatchString, "noRejected": ""})
        response.raise_for_status()
        return cveCleaner(response.json())
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error calling API: {e}")
        return None
    return None
