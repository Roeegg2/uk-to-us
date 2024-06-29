# Title



```
go recursively over each directory, and for each file:
    go over the whole file:
        if couldnt open file:
            print error
            return
        for each word in the file:
            if word is all capital, part of a URI, part of a URL:
                skip to next word
            else if the word has a dict entry 
                OR word STARTS with PREFIX (re, un, pre, mis, dis) and the rest has a dict entry
                OR word ENDS with SUFFIX (d, s):
                swap word with its entry
                log out: p:file_path l:line ow:old_word nw:new_word  

```