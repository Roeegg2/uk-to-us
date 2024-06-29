import os

def replace_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    modified_content = content.replace('wonderfull', 'great')
    
    with open(file_path, 'w') as file:
        file.write(modified_content)

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            replace_in_file(file_path)

# Specify the directory path here

directory_path = "/home/roeet/Projects/uk-to-us/test"
process_directory(directory_path)
print("Replacement complete.")