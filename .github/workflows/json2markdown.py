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
                "Title": vulnerability.get("Title"),
                "Severity": vulnerability.get("Severity")
            }
            vulnerabilities.append(extracted_vulnerability)
    return vulnerabilities

def vulnerabilities_to_markdown(vulnerabilities):
    markdown = "| Vulnerability ID | Package Name | Installed Version | Fixed Version | Title | Severity |\n"
    markdown += "|------------------|--------------|-------------------|---------------|-------|----------|\n"
    for vulnerability in vulnerabilities:
        markdown += f"| {vulnerability['VulnerabilityID']} | {vulnerability['PkgName']} | {vulnerability['InstalledVersion']} | {vulnerability['FixedVersion']} | {vulnerability['Title']} | {vulnerability['Severity']} |\n"
    return markdown.strip()

# Load JSON data from file
json_data = load_json_from_file("report.json")

# Extract vulnerabilities
vulnerabilities = extract_vulnerabilities(json_data)

# Convert vulnerabilities to Markdown table
markdown = vulnerabilities_to_markdown(vulnerabilities)

# Write the Markdown table to file
with open("report.md", "w") as file:
    file.write(markdown)