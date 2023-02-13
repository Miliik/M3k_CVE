import datetime
import json


def create_output(nb, cvelist):
    # write in a file output.DATENOW.md the number of cve and the list of cve , all separate by h1 being the cve id
    date = datetime.datetime.now()
    with open(f'output.{date}.md', 'w') as f:
        f.write(f'# Vulnerability Details\n')
        f.write(f'- **Number of CVEs:** {nb}\n')
        for cve in cvelist:
            f.write(f'## {cve.id}\n')
            f.write(f'- **Source Identifier:** {cve.sourceIdentifier}\n')
            f.write(f'- **Published:** {cve.published}\n')
            f.write(f'- **Last Modified:** {cve.lastModified}\n')
            f.write(f'- **Vulnerability Status:** {cve.vulnStatus}\n')
            f.write(f'- **Description:** {cve.descriptions}\n')
            for metric in cve.metrics.keys():
                if 'cvssMetric' in metric:
                    for key, value in cve.metrics[metric].items():
                        f.write(f'- **{key}:** {value}\n')

            # pattern = re.compile(r'^cvssMetric\d+$')
            #
            # # Loop through the matching keys
            # for key in cve['metrics']:
            #     if pattern.match(key):
            #         # Write the key-value pair
            #         f.write(f'- **{key}:** {cve["metrics"][key]}\n')