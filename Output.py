import datetime


def write_cvssMetricV2(cve, f, cvss='cvssMetricV2'):  # this function is used to write the cvssMetricV2 in the output
    # file in .md format as it is a json, making possible to store easily the json in the class CVE
    if cvss in cve.metrics: # if the cvssis in the metrics, write it in the output file
        f.write(f'- **{cvss}:**\n')
        for i in range(len(cve.metrics[cvss])):
            for key, value in cve.metrics[cvss][i].items(): # write the key and the value of the json in the output file
                if key != 'cvssData':
                    f.write(f'   - **{key}:** {value}\n')
                else:
                    for key, value in cve.metrics[cvss][i]['cvssData'].items():
                        f.write(f'   - **{key}:** {value}\n')
    else:
        f.write(f'- **{cvss}:** N/A\n')


def create_output(nb, cvelist):  # this function is used to create the output file in .md format
    date = datetime.datetime.now() # get the current date
    with open(f'output.{date}.md', 'w') as f: # create the output file
        f.write(f'# Vulnerability Details\n')
        f.write(f'- **Number of CVEs:** {nb}\n')
        for cve in cvelist:
            f.write(f'## {cve.id}\n')
            f.write(f'- **Source Identifier:** {cve.sourceIdentifier}\n')
            f.write(f'- **Published:** {cve.published}\n')
            f.write(f'- **Last Modified:** {cve.lastModified}\n')
            f.write(f'- **Vulnerability Status:** {cve.vulnStatus}\n')
            f.write(f'- **Description:** {cve.descriptions}\n')
            if 'cvssMetricV2' in cve.metrics:  # if the cvssMetricV2 is in the metrics, write it in the output file
                write_cvssMetricV2(cve, f)
            elif 'cvssMetricV3' in cve.metrics:
                write_cvssMetricV2(cve, f, 'cvssMetricV3')
            elif 'cvssMetricV31' in cve.metrics:
                write_cvssMetricV2(cve, f, 'cvssMetricV31')
            else:
                f.write(f'- **CVSS:** N/A\n')
    print('all the results are saved in the output file named in the format output.md')
    return print(f'output.{date}.md')  # return the name of the output file for parsing purpose
