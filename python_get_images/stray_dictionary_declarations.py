import json
from os import listdir, rename, path

kanji_eng_dict = {
    "昨": "past",
    "即": "immediate",
    "尺": "measurement"
}

squares = [f for f in listdir("./") if f.endswith(".pdf")]
print(squares)
ls_convert = []
for s in squares:
    first_char = s[0]
    eng = kanji_eng_dict[first_char]
    if s.endswith("_block.pdf"):
        f_eng_block = eng + s[1:]
        ls_convert.append((s, f_eng_block))
    else:
        f_eng_curs = eng + s[1:]
        ls_convert.append((s, f_eng_curs))

print(ls_convert)

for a, b in ls_convert:
    dest = path.join("english", b)
    rename(a, dest)


# eng_kanji_dict = {}
# for key, value in kanji_eng_dict.items():
#     eng_kanji_dict[value] = key
#
# print(json.dumps(eng_kanji_dict, indent=4, sort_keys=True))
