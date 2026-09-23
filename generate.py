import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load project data
with open(os.path.join(BASE_DIR, 'projects.json'), 'r', encoding='utf-8') as f:
    projects = json.load(f)

# Load HTML template
with open(os.path.join(BASE_DIR, 'templates', 'template.html'), 'r', encoding='utf-8') as f:
    template = f.read()

# Ensure output directory exists
output_dir = os.path.join(BASE_DIR, 'output')
os.makedirs(output_dir, exist_ok=True)

# Generate one HTML file per project
for project in projects:
    html = template
    html = html.replace('{{TITLE}}', project['title'])
    html = html.replace('{{DESCRIPTION}}', project['description'])
    html = html.replace('{{TECHNOLOGIES}}', ', '.join(project['technologies']))
    html = html.replace('{{IMAGE}}', project['image'])
    html = html.replace('{{URL}}', project['url'])

    filename = f"project_{project['id']}.html"
    with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as out:
        out.write(html)

    print(f"Generated {filename}")

print("Done. All project pages generated.")