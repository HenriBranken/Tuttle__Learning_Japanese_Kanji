import json
from os import listdir, rename, path

kanji_eng_dict = {
    "中": "middle",
    "右": "migi",
    "半": "half",
    "左": "hidari",
    "手": "te",
    "牛": "ushi",
    "意": "mind",
    "交": "mix",
    "午": "noon",
    "質": "quality",
    "正": "proper",
    "方": "direction",
    "声": "voice",
    "住": "reside",
    "示": "show",
    "仕": "serve",
    "重": "heavy",
    "軽": "light",
    "合": "match"
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
