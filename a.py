def remove_chars_from_text(text, chars):
    trans_table = str.maketrans('', '', chars)
    return text.translate(trans_table)

def get_word_prefix_suffix(org_word, uk_word):
    no_punc_word = remove_chars_from_text(org_word.lower(), ',.\"\';:!?[]()}{')
    index = no_punc_word.find(uk_word)
    if index != -1:
        pre = org_word[:index]
        suf = org_word[index + len(uk_word):]
        return True, pre, suf, org_word.replace(no_punc_word, pre + uk_word + suf)
    else:
        return False, "", ""


org_word = "\"hello!?\""
uk_word = "hey"

print(get_word_prefix_suffix(org_word, uk_word))