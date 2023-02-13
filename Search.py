import requests
from conf import apikey
from Cleaner import *
from functions import *


def KeywordSearch(keyword):
    time = None
    i = input("would you like the only the most recent CVE (3 last months) ? (y/n) ")
    if i == "y":
        time = createDates()
    try:
        if time is None:
            response = requests.get("https://services.nvd.nist.gov/rest/json/cves/2.0",
                                    headers={"apiKey": apikey},
                                    params={"keywordSearch": keyword, "noRejected": ""})
        else:
            response = requests.get("https://services.nvd.nist.gov/rest/json/cves/2.0",
                                    headers={"apiKey": apikey},
                                    params={"keywordSearch": keyword, "noRejected": "", "pubStartDate": time[1],
                                            "pubEndDate": time[0]})
        response.raise_for_status()
        return cveCleaner(response.json())
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error calling API: {e}")
        return None



def MatchstringSearch(MatchString):

    time = None
    i = input("would you like the only the most recent CVE (3 last months) ? (y/n) ")
    if i == "y":
        time = createDates()
    try:

        if time is None:

            response = requests.get("https://services.nvd.nist.gov/rest/json/cves/2.0",
                                    headers={"apiKey": apikey},
                                    params={"virtualMatchString": MatchString, "noRejected": ""})
        else:

            response = requests.get("https://services.nvd.nist.gov/rest/json/cves/2.0",
                                    headers={"apiKey": apikey},
                                    params={"virtualMatchString": MatchString, "noRejected": "",
                                            "pubStartDate": time[1], "pubEndDate": time[0]})

        response.raise_for_status()
        return cveCleaner(response.json())
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error calling API: {e}")
        return None
