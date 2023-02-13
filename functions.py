# create a function that return 2 var , one Enddate equal to the current date and the other one named Startdate equal to the current date -120 days
import datetime


def createDates():
    #a time list in exact format like [YYYY][“-”][MM][“-”][DD][“T”][HH][“:”][MM][“:”][SS] where the 1st element is the enddate equal to date time now and the 2nd element is the start date equal to enddate -120 days
    time = [datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"), (datetime.datetime.now() - datetime.timedelta(days=120)).strftime("%Y-%m-%dT%H:%M:%S")]
    return time

def writehelp():
    # kill the process and then print how to use the script , the -h or --help option is used to print the help message , -w is used to search for a keyword , -p is used to search for a product , -v is used to search for a version and need to be use with -p only , -V is used to search for a vendor
    print("Usage: python3 main.py [OPTION] [ARGUMENT]")
    print("Search for CVEs in the NVD database")
    print("Options:")
    print("-h(help) : print this help message")
    print("-w(keyword) : search for a keyword (use \" \" for multiple words) (use alone only)")
    print("-p(product) : search for a product")
    print("-v(version) : search for a version of a product (use with -p only)")
    print("-V(vendor) : search for a vendor")
    print("Examples:")
    print("python3 main.py -w apache")
    print("python3 main.py -p apache")
    print("python3 main.py -p apache -v 2.4.18")
