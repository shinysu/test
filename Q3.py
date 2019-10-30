def clean_string(inp_str):
    stg = ''.join(e for e in inp_str if (e.isalnum() or e == " "))
    stg = " ".join(stg.lower().split())
    return stg

    '''stg = inp_str.translate(str.maketrans('', '', string.punctuation))
    return stg.lower().strip()'''


s = "     string. With.  Punctuation?"
print(clean_string(s))