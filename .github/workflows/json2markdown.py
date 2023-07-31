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

def load_vulnerabilities_html(filename):

    # Parse the HTML content with BeautifulSoup
    print('starting script')
    with open(filename) as file:
    print('Opening file')
    soup = BeautifulSoup(file, 'html.parser')

    # Find all rows containing vulnerability information
    rows = soup.find_all('tr', class_=['severity-HIGH', 'severity-CRITICAL'])  # Assuming all vulnerability rows have the class 'severity-HIGH'

    vulnerabilities = []
    for row in rows:
        vulnerability_id = row.find('td', text=lambda text: 'CVE-' in text)
        if vulnerability_id:
            package = row.find('td', class_='pkg-name').text.strip()
            severity = row.find('td', class_='severity').text.strip()
            installed_version = row.find('td', class_='pkg-version').text.strip()

            # Extract the fixed versions as a list from the correct <td> element
            fixed_version = [version.strip() for version in row.find_all('td')[4].text.split(',')]


            # Append the vulnerability information to the list
            vulnerabilities.append({
                'Package': package,
                'Vulnerability ID': vulnerability_id.text.strip(),
                'Severity': severity,
                'Installed Version': installed_version,
                'Fixed Version': fixed_version
            })

    # Print all extracted vulnerabilities
    if vulnerabilities:
        for vulnerability in vulnerabilities:
            print(vulnerability)
    else:
        print("No vulnerabilities found in the table.")

    return vulnerabilities


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
    json_data = load_json_from_file("report.html")
    json_formatted = extract_vulnerabilities(json_data)

# Convert json data to Markdown table
markdown = convert_json_to_markdown(json_formatted)

# Write the Markdown table to file
with open(output_file, "w") as file:
    file.write(markdown)