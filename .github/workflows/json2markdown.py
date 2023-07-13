import json
import sys
from bs4 import BeautifulSoup


def load_html_from_file(filename):
    with open(filename) as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Extract values from HTML using CSS selectors
    tests = soup.select('#tests .counter')[0].text
    failures = soup.select('#failures .counter')[0].text
    ignored = soup.select('#ignored .counter')[0].text
    duration = soup.select('#duration .counter')[0].text
    successRate = soup.select('#successRate .percent')[0].text
    # Create a dictionary with extracted values
    data = {
        'tests': int(tests),
        'failures': int(failures),
        'ignored': int(ignored),
        'duration': duration,
        'successRate': successRate
    }
    # Convert dictionary to JSON
    json_data = json.dumps(data)
    return json_data


def load_json_from_file(filename):
    with open(filename) as file:
        return json.load(file)


def extract_vulnerabilities(data):
    vulnerabilities = []
    results = data.get("Results", [])
    for result in results:
        result_vulnerabilities = result.get("Vulnerabilities", [])
        for vulnerability in result_vulnerabilities:
            extracted_vulnerability = {
                "VulnerabilityID": vulnerability.get("VulnerabilityID"),
                "PkgName": vulnerability.get("PkgName"),
                "InstalledVersion": vulnerability.get("InstalledVersion"),
                "FixedVersion": vulnerability.get("FixedVersion"),
                "Severity": vulnerability.get("Severity")
            }
            vulnerabilities.append(extracted_vulnerability)
    return vulnerabilities


def convert_json_to_markdown(vulnerabilities):
    # Extract headers from the keys of the first item
    headers = list(vulnerabilities[0].keys())
    # Generate the markdown table header
    markdown = "| " + " | ".join(headers) + " |\n"
    markdown += "| " + " | ".join(["-" * len(header) for header in headers]) + " |\n"

    # Generate the markdown table rows
    for item in vulnerabilities:
        row = "| " + " | ".join(str(value) for value in item.values()) + " |\n"
        markdown += row
    return markdown

# Getting type of report
type = str(sys.argv[1])
output_file = 'report_' + type + '.md'

# Load JSON
if type == 'UNITTEST':
    json_unittest = load_html_from_file("./build/reports/tests/test/index.html")
elif type == 'VULNERABILITY':
    json_data = load_json_from_file("report.json")
    json_vulnerability = extract_vulnerabilities(json_data)

# Convert vulnerabilities to Markdown table
markdown = convert_json_to_markdown(vulnerabilities)

# Write the Markdown table to file
with open(output_file, "w") as file:
    file.write(markdown)