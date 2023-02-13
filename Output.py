import datetime
import json

from CVEClass import beautify_json

def write_cvssMetricV2(cve, f, cvss='cvssMetricV2'):
    if cvss in cve.metrics:
        f.write(f'- **{cvss}:**\n')
        for i in range(len(cve.metrics[cvss])):
            for key, value in cve.metrics[cvss][i].items():
                if key != 'cvssData':
                    f.write(f'   - **{key}:** {value}\n')
                else:
                    for key, value in cve.metrics[cvss][i]['cvssData'].items():
                        f.write(f'   - **{key}:** {value}\n')
    else:
        f.write(f'- **{cvss}:** N/A\n')
def create_output(nb, cvelist):

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
            #as metrics contain json this json :{ "cvssMetricV2": [ { "acInsufInfo": false, "baseSeverity": "HIGH", "cvssData": { "accessComplexity": "LOW", "accessVector": "NETWORK", "authentication": "NONE", "availabilityImpact": "COMPLETE", "baseScore": 10.0, "confidentialityImpact": "COMPLETE", "integrityImpact": "COMPLETE", "vectorString": "AV:N/AC:L/Au:N/C:C/I:C/A:C", "version": "2.0" }, "exploitabilityScore": 10.0, "impactScore": 10.0, "obtainAllPrivilege": false, "obtainOtherPrivilege": false, "obtainUserPrivilege": false, "source": "nvd@nist.gov", "type": "Primary", "userInteractionRequired": false } ] } ", convert each key value pair to a string and write it to the file in .md format, BUT omitting the curly braces and the first cvssMetricV2
            if  'cvssMetricV2' in cve.metrics:
                write_cvssMetricV2(cve, f)
            elif 'cvssMetricV3' in cve.metrics:
                write_cvssMetricV2(cve, f, 'cvssMetricV3')
            elif 'cvssMetricV31' in cve.metrics:
                write_cvssMetricV2(cve, f, 'cvssMetricV31')
            else:
                f.write(f'- **CVSS:** N/A\n')
    print('all the results are saved in the output file named in the format output.md')
    return print(f'output.{date}.md')
