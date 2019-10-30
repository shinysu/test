import string

def clean_string(inp_str):
    st = str.maketrans('', '', string.punctuation)
    return inp_str.translate(st).lower().strip().split()


def get_trigrams(text):
    text = text.replace("?", ".")
    text = text.replace("!", ".")
    text_lines = text.split(".")
    trigram_list = []
    for line in text_lines:
        st = clean_string(line)
        for trigram in zip(st[:-2], st[1:], st[2:]):
            trigram_list.append(" ".join(trigram))
    return list(set(trigram_list))


inp_s = "This is a test. This is another test, along with another Final Test."
print(get_trigrams(inp_s))
