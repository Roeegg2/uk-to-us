import os
import sys
from colorama import Fore, init

init(autoreset=True)

# POTENTIAL ERRORS WITH prise, programme

uk_bases = ['acknowledgement', 'analys', 'authoris', 'behaviour', 'cancelled', 'capitalis', 'catalogue', 'categoris', 'centre', 'characteris', 'colour', 'customis', 'defenc', 'endeavour', 'enrol', 'finalis', 'flavour', 'fulfil', 'grey', 'honour', 'labelled', 'licenc', 'maximis', 'minimis', 'modell', 'monetis', 'neighbour', 'normalis', 'optimis', 'organis', 'personalis', 'prise', 'programme', 'recognis', 'specialis', 'spelt', 'standardis', 'utilis', 'wilful']
us_bases = ['acknowledgment', 'analyz', 'authoriz', 'behavior', 'canceled', 'capitaliz', 'catalog', 'categoriz', 'center', 'characteriz', 'color', 'customiz', 'defens', 'endeavor', 'enroll', 'finaliz', 'flavor', 'fulfill', 'gray', 'honor', 'labeled', 'licens', 'maximiz', 'minimiz', 'model', 'monetiz', 'neighbor', 'normaliz', 'optimiz', 'organiz', 'personaliz', 'prize', 'program', 'recogniz', 'specializ', 'spelled', 'standardiz', 'utiliz', 'willful']

# dir = '/home/roeet/Projects/uk-to-us/test'
dir0 = '/home/roeet/Projects/tyk-docs/tyk-docs/data'
dir1 = '/home/roeet/Projects/tyk-docs/tyk-docs/content'

def process_files(directory, i):
    total_replacements = 0
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.md') or filename.endswith('.json'):
                filepath = os.path.join(root, filename)
                replacements = process_file(filepath, i)
                total_replacements += replacements
    
    print(f"\nTotal replacements made: {total_replacements}")

def info_print(filepath, idx, line, uk_base, us_base, word):
    index = line.find(word)

    print(f"{Fore.WHITE}File: {Fore.MAGENTA}{filepath}")
    print(f"{Fore.WHITE}Line {idx + 1}: {Fore.GREEN}{line[:index]}{Fore.RED}{word}{Fore.GREEN}{line[index + len(word):]}")
    print(f"{Fore.WHITE}Replace '{Fore.RED}{uk_base}{Fore.WHITE}' with '{Fore.BLUE}{us_base}{Fore.WHITE}'? (y/n)", end='')

def handle_swap_words(uk_base, us_base, idx, line, lines, filepath, replacements, word): 
    info_print(filepath, idx, line, uk_base, us_base, word)   
    if input().lower() != 'n':
        lines[idx] = line.replace(uk_base, us_base)
        print(f"{Fore.YELLOW}Replaced successfully")
        return True, replacements + 1
    else:
        print(f"{Fore.YELLOW}Did not replace")
        return False, replacements

def process_file(filepath, i):
    replacements = 0
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        modified = False
        for idx, line in enumerate(lines):
            for word in line.split():
                if '-' in word or '/' in word:
                    continue
                if uk_bases[i] in word:
                    modified, replacements = handle_swap_words(uk_bases[i], us_bases[i], idx, line, lines, filepath, replacements, word)
                if uk_bases[i].capitalize() in word:
                    modified, replacements = handle_swap_words(uk_bases[i].capitalize(), us_bases[i].capitalize(), idx, line, lines, filepath, replacements, word)

        if modified:
            with open(filepath, "w", encoding="utf-8") as f:
                f.writelines(lines)
    
    except Exception as e:
        print(f"{Fore.RED}Error processing {filepath}: {str(e)}")
    
    return replacements

if __name__ == "__main__":
    i = 3
    process_files(dir0, i)
    process_files(dir1, i)
    # process_files(dir, i)

# i = 0
# cnt = 0
# for root, _, files in os.walk(dir):
#     for filename in files:
#         filepath = os.path.join(root, filename)
#         with open(filepath, "r") as f:
#             linenum = 1
#             lines = f.readlines()  # read all lines at once for potential modification
#             for idx, line in enumerate(lines):
#                 for word in line.split():
#                     if uk_bases[i] in word and '-' not in word and '/' not in word:
#                         cnt += 1
#                         print(Fore.WHITE + "LINENUM:" + Fore.RED + f"{linenum}")
#                         print(Fore.WHITE + "WORD:" + Fore.BLUE + f"'{word}'")
#                         print(Fore.WHITE + "FILE:" + Fore.MAGENTA + f"{filepath}")
#                         print(Fore.WHITE + "LINE:" + Fore.GREEN + f"{line}")
#                         lines[idx] = line.replace(uk_bases[i], us_bases[i])  # Modify the line directly

#                 linenum += 1

#         # Write modified lines back to the file
#         print(Fore.YELLOW + f"Replace '{uk_bases[i]}' with '{us_bases[i]}' in {filepath}? (y/n)")
#         replace = input()
#         if replace == 'y':
#             with open(filepath, "w") as f:
#                 f.writelines(lines)  # Write modified lines back to the file
#             print(Fore.YELLOW + f"Replaced successfully")
#         else:
#             print(Fore.YELLOW + f"Did not replace")


# '''
# for each file in dir
# for each line in file
# for each word in line
# if word matches with the uk base:
#     replace us base with the uk base


# '''