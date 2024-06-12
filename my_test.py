mine = "./pfhedge/"
import os
import subprocess

def generate_uml(directory, project_name, output_format='png'):
    # Generate .dot files using pyreverse
    pyreverse_command = f'pyreverse -o dot -p {project_name} {directory}'
    subprocess.run(pyreverse_command, shell=True)

    # Convert .dot files to UML diagrams using PlantUML
    dot_files = ['classes.dot', 'packages.dot']
    for dot_file in dot_files:
        if os.path.exists(dot_file):
            plantuml_command = f'plantuml {dot_file} -t{output_format}'
            subprocess.run(plantuml_command, shell=True)

    # Cleanup .dot files
    for dot_file in dot_files:
        if os.path.exists(dot_file):
            os.remove(dot_file)

# Replace '/path/to/directory' with the directory you want to analyze
generate_uml(mine, 'pfhedge')

