import json

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

def extract_coverage(data):
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

# Load JSON data from file
json_data = load_json_from_file("report.json")

# Extract vulnerabilities
vulnerabilities = extract_vulnerabilities(json_data)

with open("report_compact.json", "w") as outfile:
    json.dump(vulnerabilities, outfile)

# Convert vulnerabilities to Markdown table
markdown = convert_json_to_markdown(vulnerabilities)

# Write the Markdown table to file
with open("report.md", "w") as file:
    file.write(markdown)