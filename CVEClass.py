import json


# first try to create object in python
def beautify_json(json_str):  # this function is used to beautify the json output in the terminal
    parsed = json.loads(json_str)
    return json.dumps(parsed, indent=4, sort_keys=True)


class CVE:  # this is the class that contains all the information about a CVE
    id = None
    sourceIdentifier = None
    published = None
    lastModified = None
    vulnStatus = None
    descriptions = None
    metrics = None

    def __init__(self, id, sourceIdentifier, published, lastModified, vulnStatus, descriptions,
                 metrics):  # this is the constructor of the class
        self.id = id
        self.sourceIdentifier = sourceIdentifier
        self.published = published
        self.lastModified = lastModified
        self.vulnStatus = vulnStatus
        self.descriptions = descriptions
        self.metrics = metrics

    def showAll(self):  # this function is used to print all the information about a CVE
        print("ID: " + self.id)
        print("SourceIdentifier: " + self.sourceIdentifier)
        print("Published: " + self.published)
        print("LastModified: " + self.lastModified)
        print("VulnStatus: " + self.vulnStatus)
        print("Descriptions: " + self.descriptions)
        print("Metrics: " + beautify_json(json.dumps(self.metrics)))
