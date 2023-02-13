from CVEClass import *
from Output import *


def cveCleaner(data, isoutput):  # this function is used to clean the data from the API and create a list of CVE
    cvelist = []

    for i in range(len(data['vulnerabilities'])):
        cve = CVE(data['vulnerabilities'][i]['cve']['id'],
                  data['vulnerabilities'][i]['cve']['sourceIdentifier'],
                  data['vulnerabilities'][i]['cve']['published'],
                  data['vulnerabilities'][i]['cve']['lastModified'],
                  data['vulnerabilities'][i]['cve']['vulnStatus'],
                  data['vulnerabilities'][i]['cve']['descriptions'][0]['value'],
                  data['vulnerabilities'][i]['cve']['metrics'], )
        cvelist.append(cve)
    if len(cvelist) == 0:
        print("No CVE found")
        return None
    if isoutput:
        return create_output(len(cvelist),
                             cvelist)  # if the user wants an output, return the list of CVE to the output function
    return printAll(cvelist)  # if the user doesn't want an output, print the list of CVE


def printAll(cvelist):  # this function is used to print the list of CVE using the show() function from the CVEClass
    for i in range(len(cvelist)):
        cvelist[i].showAll()  # print all the CVE in the list using the showAll() function from the CVEClass

    print("\n" + "Total number of CVEs: " + str(
        len(cvelist)))  # print the total number of CVE in the list for parsing purpose
