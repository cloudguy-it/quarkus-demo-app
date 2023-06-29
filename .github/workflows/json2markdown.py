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

def convert_json_to_markdown(vulnerabilities):
    # Extract headers from the keys of the first item
    headers = list(vulnerabilities[0].keys())

    # Generate the markdown table header
    markdown = "| " + " | ".join(headers) + " |\n"
    markdown += "| " + " | ".join(["---"] * len(headers)) + " |\n"

    # Generate the markdown table rows
    for item in vulnerabilities:
        row = "| " + " | ".join(str(value) for value in item.values()) + " |\n"
        markdown += row

    return markdown

# Load JSON data from file
json_data = load_json_from_file("report.json")

# Extract vulnerabilities
vulnerabilities = extract_vulnerabilities(json_data)

print(vulnerabilities)

print("ppppppppppppppppp")

with open("report_compact.json", "w") as outfile:
    json.dump(vulnerabilities, outfile)

# Convert vulnerabilities to Markdown table
markdownold = vulnerabilities_to_markdown(vulnerabilities)
markdown = convert_json_to_markdown(vulnerabilities)

print(markdownold)

print("pppppppppppppp")

print(markdown)

# Write the Markdown table to file
with open("reportold.md", "w") as file:
    file.write(markdownold)

# Write the Markdown table to file
with open("report.md", "w") as file:
    file.write(markdown)