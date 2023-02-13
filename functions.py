# create a function that return 2 var , one Enddate equal to the current date and the other one named Startdate equal
# to the current date -120 days
import datetime


def createDates():  # this function is used to create the dates that will be used in the search in the nvd api with
    # the specific format [YYYY][“-”][MM][“-”][DD][“T”][HH][“:”][MM][“:”][SS]
    time = [datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            (datetime.datetime.now() - datetime.timedelta(days=120)).strftime("%Y-%m-%dT%H:%M:%S")]
    return time


def writehelp():  # this function is used to print the help of the script
    print("Usage: python3 M3k-cve.py [OPTION] [ARGUMENT]")
    print("Search for CVEs in the NVD database")
    print("Options:")
    print("-h(help) : print this help message")
    print("-w(keyword) : search for a keyword (use \" \" for multiple words) (use alone only)")
    print("-p(product) : search for a product")
    print("-v(version) : search for a version of a product (use with -p only)")
    print("-V(vendor) : search for a vendor")
    print("Examples:")
    print("python3 M3k-cve.py -w apache")
    print("python3 M3k-cve.py -p apache")
    print("python3 M3k-cve.py -p apache -v 2.4.18")
