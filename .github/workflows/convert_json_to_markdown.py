import json
from json2markdown import json2markdown

json_file_path = 'report.json'
markdown_file_path = 'report.md'

with open(json_file_path) as json_file:
    json_data = json.load(json_file)

markdown_content = json2markdown(json_data)

with open(markdown_file_path, 'w') as markdown_file:
    markdown_file.write(markdown_content)
