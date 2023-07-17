import json
import sys
import os
from bs4 import BeautifulSoup


def load_html_from_file(filename):
    unittests = []
    with open(filename) as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Extract values from HTML using CSS selectors
    tests = soup.select('#tests .counter')[0].text
    failures = soup.select('#failures .counter')[0].text
    ignored = soup.select('#ignored .counter')[0].text
    duration = soup.select('#duration .counter')[0].text
    successRate = soup.select('#successRate .percent')[0].text
    if ( int(failures) > 0 ):
        icon = ":x:"
    else:
        icon = ":white_check_mark:"
    # Create a dictionary with extracted values
    extracted_result = {
        "Tests": int(tests),
        "Failures": int(failures),
        "Ignored": int(ignored),
        "Duration": duration,
        "SuccessRate": successRate,
        "Status": icon
    }
    unittests.append(extracted_result)

    return unittests


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


def convert_json_to_markdown(formatted_json):
    # Extract headers from the keys of the first item
    headers = list(formatted_json[0].keys())

    # Generate the markdown table header
    markdown = "| " + " | ".join(headers) + " |\n"
    markdown += "| " + " | ".join(["-" * len(header) for header in headers]) + " |\n"

    # Generate the markdown table rows
    for item in formatted_json:
        row = "| " + " | ".join(str(value) for value in item.values()) + " |\n"
        markdown += row
    return markdown

# Getting type of report
type = str(sys.argv[1])
output_file = 'report_' + type + '.md'
# Load JSON
if type == 'UNITTEST':
    json_formatted = load_html_from_file("./build/reports/tests/test/index.html")
elif type == 'VULNERABILITY':
    json_data = load_json_from_file("report.json")
    json_formatted = extract_vulnerabilities(json_data)

# Convert vulnerabilities to Markdown table
markdown = convert_json_to_markdown(json_formatted)

# Write the Markdown table to file
with open(output_file, "w") as file:
    file.write(markdown)