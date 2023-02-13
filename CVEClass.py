import json


def beautify_json(json_str):
    parsed = json.loads(json_str)
    return json.dumps(parsed, indent=4, sort_keys=True)


class CVE:
    id = None
    sourceIdentifier = None
    published = None
    lastModified = None
    vulnStatus = None
    descriptions = None
    metrics = None

    def __init__(self, id, sourceIdentifier, published, lastModified, vulnStatus, descriptions, metrics):
        self.id = id
        self.sourceIdentifier = sourceIdentifier
        self.published = published
        self.lastModified = lastModified
        self.vulnStatus = vulnStatus
        self.descriptions = descriptions
        self.metrics = metrics

    def showAll(self):
        print("ID: " + self.id)
        print("SourceIdentifier: " + self.sourceIdentifier)
        print("Published: " + self.published)
        print("LastModified: " + self.lastModified)
        print("VulnStatus: " + self.vulnStatus)
        print("Descriptions: " + self.descriptions)
        print("Metrics: " + beautify_json(json.dumps(self.metrics)))
