# create a function that return 2 var , one Enddate equal to the current date and the other one named Startdate equal to the current date -120 days
import datetime


def createDates():
    enddate = datetime.datetime.now()
    startdate = enddate - datetime.timedelta(days=120)
    return startdate, enddate


def writehelp():
    #kill the process and then print how to use the script , the -h or --help option is used to print the help message , -w is used to search for a keyword , -p is used to search for a product , -v is used to search for a version and need to be use with -p only , -V is used to search for a vendor
    print("Usage: python3 main.py [OPTION] [ARGUMENT]")
    print("Search for CVEs in the NVD database")
    print("Options:")
    print("-h(help) : print this help message")
    print("-w(keyword) : search for a keyword (use \" \" for multiple words)")
    print("-p(product) : search for a product")
    print("-v(version) : search for a version")
    print("-V(vendor) : search for a vendor")
    print("Examples:")
    print("python3 main.py -w apache")
    print("python3 main.py -p apache")
    print("python3 main.py -p apache -v 2.4.18")