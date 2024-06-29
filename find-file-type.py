import os

def list_file_types(directory):
    file_types = set()  # Using a set to store unique file extensions
    
    for root, _, files in os.walk(directory):
        for file in files:
            _, ext = os.path.splitext(file)
            file_types.add(ext.lower())  # Convert to lowercase to normalize extensions
    
    return file_types

def main():
    directory = "/home/roeet/Projects/tyk-docs"
    
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return
    
    file_types = list_file_types(directory)
    
    if file_types:
        print("File types found in the directory and its subdirectories:")
        for file_type in sorted(file_types):
            print(file_type)
    else:
        print("No files found in the directory and its subdirectories.")

if __name__ == "__main__":
    main()
