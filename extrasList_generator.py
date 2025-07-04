import os
import json
from jinja2 import Environment, FileSystemLoader

# Load templates from the current directory
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('extrasList_template.html')

# Path to the projects folder
projects_folder = 'extras'

# List to hold all project data
projects = []

# Iterate through all JSON files in the projects folder
for filename in os.listdir(projects_folder):
    if filename.endswith('.json'):
        with open(os.path.join(projects_folder, filename), 'r') as file:
            project_data = json.load(file)
            projects.append(project_data)

# Render the template with the projects data
rendered_html = template.render(projects=projects)

# Save the rendered HTML to a file
with open('extrasList.html', 'w') as output_file:
    output_file.write(rendered_html)

print("Generated extrasList.html successfully.")
