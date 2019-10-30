def clean_string(inp_str):
    st = ''.join(letter for letter in inp_str if (letter.isalnum() or letter == " "))
    return st.lower().split()


def top_words(inp_str):
    st = clean_string(inp_str)
    d = {}
    for word in st:
        d[word] = d.get(word, 0) + 1

    sorted_d = dict(sorted(d.items(),key=lambda kv:kv[1],reverse=True))
    return list(sorted_d.keys())[:5]


s="Pittas are a family, Pittidae, of passerine birds found in Asia, Australasia and Africa. There are thought to be 40 to 42 species of pittas, all similar in general appearance and habits. The pittas are Old World suboscines, and their closest relatives among other birds are the broadbills in the genera Smithornis and Calyptomena. Initially placed in a single genus, as of 2009 they have been split into three genera: Pitta, Erythropitta and Hydrornis. Pittas are medium-sized by passerine standards, at 15 to 25 cm (5.9–9.8 in) in length, and stocky, with strong, longish legs and long feet. They have very short tails and stout, slightly decurved bills. Many have brightly coloured plumage.Most pitta species are tropical; a few species can be found in temperate climates. They are mostly found in forests, but some live in scrub and mangroves. They are highly terrestrial and mostly solitary, and usually forage on wet forest floors in areas with good ground cover. They eat earthworms, snails, insects and similar invertebrate prey, as well as small vertebrates. Pittas are monogamous and females lay up to six eggs in a large domed nest in a tree or shrub, or sometimes on the ground. Both parents care for the young. Four species of pittas are fully migratory, and several more are partially so, though their migrations are poorly understood.Four species of pitta are listed as endangered by the International Union for Conservation of Nature; a further nine species are listed as vulnerable and several more are near-threatened. The main threat to pittas is habitat loss in the form of rapid deforestation, but they are also targeted by the cage-bird trade. They are popular with birdwatchers because of their bright plumage and the difficulty in seeing them"
print(top_words(s))