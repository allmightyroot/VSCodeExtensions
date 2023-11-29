import json
import urllib.request
import csv
from datetime import datetime

# Load the list of installed extensions
try:
    with open('extensions.txt', 'r') as f:
        extensions = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    print('Error: extensions.txt file not found. Please make sure the file exists in the same directory.')
    exit(1)

# Validate extension names
if not all(extensions):
    print('Error: Invalid extension names in extensions.txt. Please make sure the file contains valid extension names.')
    exit(1)

# Sort the list of extensions alphabetically
extensions.sort()

# Generate HTML content with Date Generated header
date_generated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

html_content = f'''<html>
<head>
<title>Installed Visual Studio Code Extensions</title>
</head>
<body>
<h1>Installed Visual Studio Code Extensions</h1>
<p>Date Generated: {date_generated}</p>
<table>
<tr>
<th>Extension</th>
<th>Description</th>
<th>Install</th>
</tr>
'''

# Generate Markdown content with Date Generated header
markdown_content = f'# Installed Visual Studio Code Extensions\n\nDate Generated: {date_generated}\n\n'

# Create CSV file and write header
with open('extensions.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Extension', 'Description', 'Install'])

# Iterate over each extension
for extension in extensions:
    # Get the extension metadata from the Visual Studio Code API
    try:
        url = 'https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery'
        query = {
            'filters': [
                {
                    'criteria': [
                        {
                            'filterType': 7,
                            'value': extension
                        }
                    ],
                    'pageSize': 1,
                    'sortBy': 0,
                    'sortOrder': 0
                }
            ],
            'assetTypes': [],
            'flags': 914
        }
        headers = {
            'Accept': 'application/json;api-version=3.0-preview.1',
            'Content-Type': 'application/json'
        }
        req = urllib.request.Request(url, json.dumps(query).encode('utf-8'), headers=headers)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
        extension_metadata = data['results'][0]['extensions'][0]

        # Check if the extension is part of an extension pack (exclude if it is)
        flags = extension_metadata.get('flags', [])
        if isinstance(flags, list) and any(flag['name'] == 'ExtensionPack' for flag in flags):
            continue

    except (urllib.error.URLError, urllib.error.HTTPError, IndexError, KeyError) as e:
        print(f'Error: Failed to fetch metadata for extension "{extension}" from the Visual Studio Code API: {e}.')
        continue

    # Extract the extension name, description, and URL
    name = extension_metadata['displayName']
    description = extension_metadata['shortDescription']
    url = extension_metadata['versions'][0]['fallbackAssetUri']
    url += '/Microsoft.VisualStudio.Services.VSIXPackage?install=true'

    # Add the extension information to the HTML content
    html_content += f'<tr>\n<td>{name}</td>\n<td>{description}</td>\n<td><a href="{url}">Install</a></td>\n</tr>\n'

    # Add the extension information to the Markdown content
    markdown_content += f'## {name}\n\n{description}\n\nInstall: [{name}]({url})\n\n'

    # Write the extension information to the CSV file
    with open('extensions.csv', 'a', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([name, description, url])

html_content += '</table>\n</body>\n</html>'

# Write the HTML content to a file
with open('extensions.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# Write the Markdown content to a file
with open('extensions.md', 'w', encoding='utf-8') as f:
    f.write(markdown_content)

print('extensions.html, extensions.md, and extensions.csv files have been generated.')

