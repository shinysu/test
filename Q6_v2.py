import string


def clean_string(inp_str):
    st = str.maketrans('', '', string.punctuation)
    return inp_str.translate(st).lower().strip().split()


def get_bigrams(text):
    text = text.replace("?",".")
    text = text.replace("!",".")
    textlist = text.split(".")
    bigram = []
    for line in textlist:
        st = clean_string(line)
        for i in range(len(st)-1):
            bigram.append(st[i]+" "+st[i+1])

    return list(set(bigram))



s = "This is a test. This is another test, along with another Final Test."
print(get_bigrams(s))


