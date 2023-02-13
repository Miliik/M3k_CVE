import re

from CVEClass import *
from Output import *

# def inputcleaner(string):
#     #remove all special characters from the input string except space between words and put it to lower case
#     string = re.sub(r'[^a-zA-Z0-9 ]', '', string).lower()
#     return string

def cveCleaner(data):
    cvelist = []

    for i in range(len(data['vulnerabilities'])):
        cve = CVE(data['vulnerabilities'][i]['cve']['id'],
                  data['vulnerabilities'][i]['cve']['sourceIdentifier'],
                  data['vulnerabilities'][i]['cve']['published'],
                  data['vulnerabilities'][i]['cve']['lastModified'],
                  data['vulnerabilities'][i]['cve']['vulnStatus'],
                  data['vulnerabilities'][i]['cve']['descriptions'][0]['value'],
                  data['vulnerabilities'][i]['cve']['metrics'],)
        cvelist.append(cve)

    return create_output(len(cvelist), cvelist)


def printAll(cvelist):
    for i in range(len(cvelist)):
        cvelist[i].showAll()

    print("\n" + "Total number of CVEs: " + str(len(cvelist)))
