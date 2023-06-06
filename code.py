import pykakasi

def jlpt_kanji(word):
    kks = pykakasi.kakasi()
    kks.setMode("J", "H")
    conv = kks.getConverter()
    result = conv.do(word)
    
    print(word)
    print("")

    jlpt_levels = {
        "N5": "n5_kanji.txt",
        "N4": "n4_kanji.txt",
        "N3": "n3_kanji.txt",
        "N2": "n2_kanji.txt",
        "N1": "n1_kanji.txt"
    }

    for level, file_name in jlpt_levels.items():
        with open(file_name) as f:
            kanji_list = [line.strip() for line in f.readlines()]

        for item in kanji_list:
            if item in word:
                print("{} Kanji: {} ({})".format(level, item, conv.do(item)))
