import string


def clean_string(inp_str):
    st = str.maketrans('', '', string.punctuation)
    return inp_str.translate(st).lower().strip().split()


def get_bigrams(text):
    text = text.replace("?",".")
    text = text.replace("!",".")
    text_lines = text.split(".")
    bigram_list = []
    for line in text_lines:
        st = clean_string(line)
        for bigram in zip(st[:-1], st[1:]):
            bigram_list.append(" ".join(bigram))
    return list(set(bigram_list))


inp_str = "This is a test. This is another test, along with another Final Test."

print(get_bigrams(inp_str))
