import os
import json
from jinja2 import Environment, FileSystemLoader

# Directory containing project JSON files
projects_dir = 'projects'

# Load project metadata from JSON files
projects = []
for filename in os.listdir(projects_dir):
    if filename.endswith('.json'):
        with open(os.path.join(projects_dir, filename), 'r') as file:
            project_data = json.load(file)
            projects.append(project_data)

# Load the template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template_v2.html')

# Output directory for generated HTML files
output_dir = 'ProjectPages'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate HTML files for each project
for project in projects:
    output_path = os.path.join(output_dir, f"{project['name'].replace(' ', '_').lower()}.html")
    with open(output_path, 'w') as f:
        f.write(template.render(**project))

print(f"Generated {len(projects)} project files.")
