# def replace_words(input_file, output_file, replacements):
#     try:
#         with open(input_file, 'r') as file:
#             content = file.read()
        
#         for old_word, new_word in replacements.items():
#             content = content.replace(old_word, new_word)
        
#         with open(output_file, 'w') as file:
#             file.write(content)
        
#         print(f"Replacement complete. Result saved to {output_file}")
#     except FileNotFoundError:
#         print(f"Error: The file {input_file} was not found.")
#     except IOError:
#         print("Error: An I/O error occurred.")

# # Example usage
# input_file = 'input.txt'
# output_file = 'output.txt'
# replacements = {
#     'old': 'new',
#     'hello': 'hi',
#     'world': 'earth'
# }

# replace_words(input_file, output_file, replacements)

