import requests

from Cleaner import *
from conf import apikey
from functions import *


def KeywordSearch(keyword, output):  # searches for a keyword in the description of the CVE
    time = None
    i = input("would you like the only the most recent CVE (3 last months) ? (y/n) ")
    if i == "y":
        time = createDates() # creates the dates for the last 3 months
    try:  # try to get the response from the API
        if time is None:
            response = requests.get("https://services.nvd.nist.gov/rest/json/cves/2.0",
                                    headers={"apiKey": apikey},
                                    params={"keywordSearch": keyword, "noRejected": ""}) # get the response from the API with the keyword in the description, no rejected CVEs only
        else:
            response = requests.get("https://services.nvd.nist.gov/rest/json/cves/2.0",
                                    headers={"apiKey": apikey},
                                    params={"keywordSearch": keyword, "noRejected": "", "pubStartDate": time[1],
                                            "pubEndDate": time[0]}) # get the response from the API but using the fact that pubstartdate and pubenddate show the last 3 months of CVEs
        response.raise_for_status() # raise an error if the response is not 200
        return cveCleaner(response.json(), output) # return the response to the cveCleaner function
    except (requests.exceptions.RequestException, ValueError) as e:  # if the API doesn't respond, print the error
        print(f"Error calling API: {e}")  # print the error
        exit(1)  # exit the program


def MatchstringSearch(matchstring, output):  # searches for a matchstring in the cpe of the CVE
    time = None
    i = input("would you like the only the most recent CVE (3 last months) ? (y/n) ")
    if i == "y":
        time = createDates()
    try:

        if time is None:

            response = requests.get("https://services.nvd.nist.gov/rest/json/cves/2.0",
                                    headers={"apiKey": apikey},
                                    params={"virtualMatchString": matchstring, "noRejected": ""})
        else:

            response = requests.get("https://services.nvd.nist.gov/rest/json/cves/2.0",
                                    headers={"apiKey": apikey},
                                    params={"virtualMatchString": matchstring, "noRejected": "",
                                            "pubStartDate": time[1], "pubEndDate": time[0]})

        response.raise_for_status()
        return cveCleaner(response.json(), output)
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error calling API: {e}")
        exit(1)
