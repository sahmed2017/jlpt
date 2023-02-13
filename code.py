import pykakasi

def jlpt_kanji(word):
    kks = pykakasi.kakasi()
    kks.setMode("J", "H")
    conv = kks.getConverter()
    result = conv.do(word)
    
    print(word)
    print("")

    # Load the N5 vocabulary words from a text file
    with open("n5_kanji.txt") as f:
        n5_kanji = [line.strip() for line in f.readlines()]

    for item in n5_kanji:
        if item in word:
            print("N5 Kanji: {} ({})".format(item, conv.do(item)))

    with open("n4_kanji.txt") as f:
        n4_kanji = [line.strip() for line in f.readlines()]
    
    for item in n4_kanji:
        if item in word:
            print("N4 Kanji: {} ({})".format(item, conv.do(item)))

    with open("n3_kanji.txt") as f:
        n3_kanji = [line.strip() for line in f.readlines()]

    for item in n3_kanji:
        if item in word:
            print("N3 Kanji: {} ({})".format(item, conv.do(item)))
    
    with open("n2_kanji.txt") as f:
        n2_kanji = [line.strip() for line in f.readlines()]

    for item in n2_kanji:
        if item in word:
            print("N2 Kanji: {} ({})".format(item, conv.do(item)))

    with open("n1_kanji.txt") as f:
        n1_kanji = [line.strip() for line in f.readlines()]

    for item in n1_kanji:
        if item in word:
            print("N1 Kanji: {} ({})".format(item, conv.do(item)))
