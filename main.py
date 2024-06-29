import os

def m_ary_search(arr, target):
    if target == "" or target == None:
        return True

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

def remove_chars_from_text(text, chars):
    trans_table = str.maketrans('', '', chars)
    return text.translate(trans_table)

def get_word_prefix_suffix(main_word, sub_word):
    search_in = remove_chars_from_text(main_word.lower(), ',."\';\:!?')
    index = search_in.find(sub_word)
    if index != -1:
        before = main_word[:index]
        after = main_word[index + len(sub_word):]
        return True, before, after
    else:
        return False, "", ""

def find_word_in_line(uk_word, line, filepath, line_num):
    for input_word in line.split():
        retcode, before, after = get_word_prefix_suffix(input_word, uk_word)
        if retcode:
            if m_ary_search(prefixes, before):
                if m_ary_search(suffixes, after):
                    print(f"found word: '{input_word}' before: '{before}' after: '{after}' uk word: '{uk_word}' in: '{filepath}' at line: {line_num}")
                elif m_ary_search(suffixes, remove_chars_from_text(after, 's')):
                    print(f"found word: '{input_word}' before: '{before}' after: '{after}' uk word: '{uk_word}' in: '{filepath}' at line: {line_num}")


def is_legal_extension(filepath):
    for ext in legal_file_extensions:
        if filepath.endswith(ext):
            return True
    return False


def search_files(directory):
    for root, _, files in os.walk(directory):
        if british_words == []:
            exit()
        for filename in files:
            filepath = os.path.join(root, filename)

            if not is_legal_extension(filepath):
                continue

            with open(filepath, "r") as f: # for each file
                line_num = 0
                for line in f: # for each line
                    line_num += 1
                    if ('/' in line or '-' in line) and " " not in line:
                        print(f"SKIPPING LINE: '{line}' in: '{filepath}' at line: {line_num}")
                        continue
                    for uk_word in british_words: # for each uk word
                        find_word_in_line(uk_word, line, filepath, line_num)

# storys stories exception
# monologue monolog exception
# programme program


if __name__ == "__main__":
    directory = "/home/roeet/Projects/tyk-docs"
    # NOTE config.toml
    # maybe add .sh .xml?
    legal_file_extensions = [".html", ".json", ".md", ".yml", ".yaml", ".css", ".scss", ".sh", ".xml"]

    prefixes = [
        "a", "ab", "ac", "ad", "af", "ag", "al", "am", "an", "ap", "ar", "as", "at", "auto",
        "be", "bi", "by", "cata", "circum", "cis", "co", "col", "com", "con", "contra", "counter", "crypto",
        "de", "demi", "di", "dia", "dis", "dys", "e", "ec", "el", "em", "en", "epi", "eu", "ex", "exo", "extra",
        "fore", "hemi", "hetero", "homo", "hyper", "hypo", "neo", "non", "ob", "oct", "omni", "out", "over",
        "il", "im", "in", "infra", "inter", "intra", "ir", "macro", "mal", "mega", "meta", "micro", "mid", "milli", 
        "mini", "mis", "mono", "multi", "pan", "para", "penta", "per", "peri", "poly", "post", "pre", "pro", "proto", 
        "pseudo", "quad", "quasi", "re", "retro", "semi", "sub", "super", "supra", "sur", "sym", "syn", "tele", "trans", 
        "tri", "ultra", "un", "under", "uni", "up", "vice"
    ]

    suffixes = [
        'ature', 'ectomy', 'land', 'gate', 'er', 'ate', 'icity', 'ite', 'acity', 'tomy', 'philia', 'ic', 'dynia',
        'ostomy', 'ous', 'cracy', 'phyte', 'i', 's', 'iveness', 'ology', 'ing', 'ize', 'iasis', 'esis', 'way', 'ial',
        'ware', 'ess', 'ence', 'itive', 'ific', 'oma', 'type', 'graph', 'like', 'aneous', 'or', 'ness', 'tic', 'fy',
        'ity', 'free', 'osis', 'plegic', 'ture', 'genic', 'etic', 'wise', 'atic', 'ique', 'phobia', 'ancy',
        'phile', 'tude', 'atory', 'ition', 'ant', 'arity', 'some', 'ise', 'ry', 'ory', 'ville', 'ile', 'ean',
        'orama', 'itis', 'ery', 'y', 'gram', 'ed', 'path', 'right', 'holic', 'ee', 'ways', 'aceous', 'fold',
        'ocity', 'ette', 'd', 'ible', 'ency', 'stan', 'tion', 'meter', 'eer', 'ern', 'ase', 'ism', 'age', 'dom',
        'ability', 'eous', 'acy', 'a', 'atious', 'proof', 'graphy', 'gamous', 'ful', 'erty', 'ion', 'nomics',
        'archy', 'penia', 'ual', 'ish', 'algia', 'e', 'kin', 'opathy', 'pathy', 'ble', 'esque', 'less', 'rama',
        'al', 'ical', 'ure', 'tory', 'itude', 'tight', 'worth', 'ance', 'ation', 'il', 'bility', 'est', 'mania',
        'plasty', 'factory', 'aholic', 'ality', 'worthy', 'oholic', 'philic', 'scope', 'ling', 'ssion', 'ibility',
        'ies', 'ly', 'ent', 'ese', 'most', 'able', 'ify', 'ward', 'th', 'ety', 'wards', 'cy', 'cious', 'ide',
        'sion', 'ade', 'tious', 'ative', 'ocracy', 'ist', 'an', 'ious', 'logy', 'maniac', 'athon', 'phobic',
        'ty', 'ian', 'otomy', 'ive', 'emia', 'ivity', 'ose', 'ary', 'en', 'tron', 'hood', 'cide', 'ine',
        'oid', 'ment', 'ship', 'let', 'ility', 'ae', 'thon', 'scape',
    ]

    british_words = [
        "accoutre", "accoutrement", "acknowledgement", "adaptor", "adaptors", "aerofoil", "aeroplane", "ageing", "aggrandis", 
        "aluminium", "americanis", 
        "americanising", "amphitheatre", "anaemia", "anaemic", "anaesthetic", "anaesthetist", "analogue", "analys", "analysing",
        "apologis", "apologising", "appal", "arbour", "archaeology", "ardour", "armour", "armourer", "armouring", "armoury", 
        "arse", "artefact", "authoris", "autumn", "axe", 
        "baulk", "behaviour", "behove", "benefitted", "bisulphate", "breathalys", "burglaris", "calibre", "calliper", "cancelled", 
        "cancelling", "candour",
        "capitalis", "carat", "carburettor", "catalogue", "catalogued", "cataloguing", "catalys", "categoris", "categorisation", 
        "categorising", "centre", "centrefold", "characteris", "cheque", "chilli", "civilisation", "clamour", "cognisance",
        "colonis", "colonisation", "colorisation", "colour", "compositae", "cosy", "counsell", "counsellor", "crayfish", "criticis", 
        "customis", "defenc", "demeanour", "dependant", "dialogue", "dialys", "disc", "distil", "disulphide", "doodah", "doughnut", 
        "draught", "draughtsman", "emphasis",
        "enamour","encyclopaedia","endeavour","energis","enquire","enquiries","enquiry","enrol","enrolment","enthral","equalled",
        "extemporis","faeces","fantasis","favour","favoured","favourite","favouritism","fervour","fibre","fibreboard","fibreglass",
        "finalis","flavour","foetus","fount","fuelled","fulfil","fulfilment",
        "furore","gauge","generalisation","glamour","goitre","grey","greyed","grovelling","haemoglobin","harbour","harmonis",
        "honour","honourable","humour","idolis","inflexion","instal","instalment","instil","jeweller","jewellery","judgement",
        "kerb","ketchup","kidnapper","kilogramme","kilometre","labelled","labour","labourer","learnt",
        "leukaemia","levell","liberalis","licenc","liquorice","litre","lustre","manoeuvre","maths","maximis","meagre","metre","minimis",
        "misdemeanour","mitre","mobilis","modell","modelling","monetis","monologue","mould",
        "moulding","moult","moustache","mum","naturalis","neighbour","neighbourhood","nitre","normalis","nought","ochre","odour",
        "oestrogen","offence","offencive","omelette","optimis","optimising","organis","organisation",
        "paediatric", "panellist", "paralys", "parlour", "pedlar", "pernickety", "personalis", "philtre", "picaninny", "plonk", 
        "plough", "popularis", "potter", "practis", "pretenc", "prioritis", "prise", "programme", "pyjamas", "quarrelling", "rancour", 
        "realis", "recognis", "reconnoitre", "reflexion", "rigour", "rumour", "rumoured", "sabre", "saltpetre", "satiris", "saviour", 
        "savour", "scallywag", "sceptic", "sceptical", "sceptre", "signaled",
        "signaling", "skilful", "smoulder", "snowplough", "socialis", "socialising", "sombre", "specialis", "speciality", "spectre", 
        "spelled", "splendour", "splendour", "stabilis", "standardis", "storey", "storeys", "succour", "sulphate", "sulphur", 
        "symbolis", "sympathis", "syphon", "theatre", "titbit", "travelled", "traveller", "travelling", "tumour", "tyre", 
        "tzar", "utilis", "valour", "vandalis", "vaporis", "vapour", "vigour", "waggon", "whisky", "wilful", "woollen", "worshipper",
    ]

    prefixes.sort()
    suffixes.sort()
    british_words.sort()
    search_files(directory)
