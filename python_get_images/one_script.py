import requests
import os

ls_kanji = {
    "政": "politics",
    "議": "deliberation",
    "連": "take_along",
    "戦": "war",
    "当": "hit2",
    "約": "promise",
    "性": "sex",
    "務": "task",
    "加": "add",
    "権": "authority",
    "支": "branch",
    "報": "report",
    "済": "settle",
    "得": "acquire",
    "解": "unravel",
    "資": "assets",
    "勝": "victory",
    "告": "revelation",
    "判": "judgement",
    "認": "acknowledge",
    "参": "participate",
    "在": "exist",
    "件": "affair",
    "任": "responsibility",
    "求": "request",
    "論": "argument",
    "増": "increase",
    "感": "emotion",
    "情": "feelings",
    "投": "throw",
    "確": "assurance",
    "果": "fruit",
    "容": "contain",
    "演": "performance",
    "談": "discuss",
    "能": "ability",
    "位": "rank",
    "置": "placement",
    "流": "current",
    "格": "status",
    "疑": "doubt",
    "過": "overdo",
    "放": "set_free",
    "常": "usual",
    "状": "status_quo",
    "球": "ball",
    "職": "post",
    "供": "submit",
    "役": "duty",
    "構": "posture",
    "割": "proportion",
    "費": "expense",
    "優": "tenderness",
    "収": "income",
    "断": "severance",
    "違": "difference",
    "消": "extinguish",
    "規": "standard",
    "備": "equip",
    "宅": "home",
    "害": "harm",
    "警": "admonish",
    "蓆": "seat",
    "訪": "call_on",
    "想": "concept",
    "助": "help",
    "労": "labor",
    "例": "example",
    "限": "limit",
    "追": "chase",
    "葉": "leaf",
    "景": "scenery",
    "退": "retreat",
    "負": "defeat",
    "渡": "transit",
    "差": "distinction",
    "守": "guard",
    "種": "species",
    "命": "fate",
    "福": "blessing",
    "望": "ambition",
    "観": "outlook",
    "察": "guess",
    "段": "grade",
    "深": "deep",
    "財": "property",
    "識": "discriminating",
    "呼": "call",
    "阪": "heights",
    "候": "climate",
    "程": "extent",
    "満": "full",
    "敗": "failure",
    "値": "price",
    "突": "stab",
    "路": "path",
    "積": "volume",
    "他": "other",
    "処": "dispose",
    "客": "guest",
    "否": "negate",
    "師": "expert",
    "易": "easy",
    "存": "exist2",
    "殺": "kill",
    "座": "squat",
    "破": "rend",
    "除": "exclude",
    "責": "blame",
    "捕": "catch",
    "危": "dangerous",
    "給": "salary",
    "苦": "suffering",
    "迎": "welcome",
    "因": "cause2",
    "富": "wealth",
    "彼": "he",
    "舞": "dance",
    "適": "suitable",
    "寄": "draw_near",
    "込": "crowded",
    "類": "sort",
    "余": "too_much",
    "返": "return",
    "妻": "wife",
    "険": "precipitous",
    "頼": "trust",
    "覚": "memorize",
    "船": "ship",
    "途": "route",
    "許": "permit",
    "抜": "slip_out",
    "罪": "guilt",
    "努": "toil",
    "精": "refined",
    "散": "scatter",
    "喜": "rejoice",
    "浮": "float",
    "絶": "discontinue",
    "幸": "happiness",
    "倒": "overthrow",
    "等": "etc",
    "老": "old_man",
    "曲": "bend",
    "払": "pay",
    "徒": "on_foot",
    "勤": "diligence",
    "居": "reside",
    "招": "beckon",
    "刻": "engrave",
    "賛": "approve",
    "抱": "embrace",
    "犯": "crime",
    "恐": "fear",
    "息": "breath",
    "戻": "re",
    "越": "surpass",
    "欲": "longing",
    "互": "mutually",
    "似": "becoming",
    "探": "grope",
    "逃": "escape",
    "迷": "astray",
    "夢": "dream",
    "君": "mister",
    "閉": "closed",
    "緒": "thong",
    "折": "fold",
    "草": "grass",
    "暮": "evening2",
    "悲": "grieve",
    "到": "arrival",
    "寝": "lie_down",
    "盗": "steal",
    "吸": "suck",
    "陽": "sunshine",
    "御": "honorable",
    "歯": "tooth",
    "吹": "blow",
    "娘": "daughter",
    "誤": "mistake",
    "慣": "accustomed",
    "窓": "window",
    "貧": "poverty",
    "怒": "angry",
    "祖": "ancestor",
    "杯": "glass",
    "疲": "exhausted",
    "鳴": "chirp",
    "腹": "abdomen",
    "煙": "smoke",
    "眠": "sleep",
    "怖": "dreadful",
    "頂": "place_on_the_head",
    "箱": "box",
    "髪": "hair_of_the_head",
    "才": "genius",
    "靴": "shoes",
    "恥": "shame",
    "偶": "accidentally",
    "偉": "admirable",
    "猫": "cat",
    "誰": "who"
}

ls_so_retry = []
ls_typical_retry = []
ls_curs_retry = []
ls_block_retry = []
for kanji, english in ls_kanji.items():
    print(kanji, end=": ")
    path_so_dest = f"http://kanji.nihongo.cz/image.php?text={kanji}&font=sod.ttf&fontsize=300&color=black"
    path_typ_dest = f"http://kanji.nihongo.cz/image.php?text={kanji}&font=HGRKK.TTC&fontsize=300&color=black"
    path_block_dest = f"http://kanji.nihongo.cz/image.php?text={kanji}&font=HGRMB.TTC&fontsize=300&color=black"
    path_curs_dest = f"http://kanji.nihongo.cz/image.php?text={kanji}&font=epgyosho.ttf&fontsize=300&color=black"

    try:
        if os.path.exists(f"english/so_{english}.pdf"):
            print("e", end=" ")
        else:
            response_so = requests.get(path_so_dest)
            with open(f"english/so_{english}.pdf", "wb") as file:
                file.write(response_so.content)
                print(1, end=" ")
    except Exception as e:
        print(0, end=" ")
        print(f"Stuggled to get the stroke-ordered {kanji}...")
        ls_so_retry.append(path_so_dest)

    try:
        if os.path.exists(f"english/{english}.pdf"):
            print("e", end=" ")
        else:
            response = requests.get(path_typ_dest)
            with open(f"english/{english}.pdf", "wb") as file:
                file.write(response.content)
                print(1, end=" ")
    except Exception as e:
        print(0, end=" ")
        print(f"Stuggled to get the typical {kanji}...")
        ls_typical_retry.append(path_typ_dest)

    try:
        if os.path.exists(f"english/{english}_block.pdf"):
            print("e", end=" ")
        else:
            response_block = requests.get(path_block_dest)
            with open(f"english/{english}_block.pdf", "wb") as file:
                file.write(response_block.content)
                print(1, end=" ")
    except Exception as e:
        print(0, end=" ")
        print(f"Stuggled to get the block {kanji}...")
        ls_block_retry.append(path_block_dest)

    try:
        if os.path.exists(f"english/{english}_curs.pdf"):
            print("e")
        else:
            response_curs = requests.get(path_curs_dest)
            with open(f"english/{english}_curs.pdf", "wb") as file:
                file.write(response_curs.content)
                print(1)
    except Exception as e:
        print(0)
        print(f"Struggled to get the cursive {kanji}...")
        ls_curs_retry.append(path_curs_dest)

if ls_so_retry:
    print(f"Unsuccessful stroke-ordered Kanji include: {ls_so_retry}.")
if ls_typical_retry:
    print(f"Unsuccessful typical Kanji include: {ls_typical_retry}.")
if ls_block_retry:
    print(f"Unsuccessful block Kanji include: {ls_block_retry}.")
if ls_curs_retry:
    print(f"Unsuccessful cursive Kanji include: {ls_curs_retry}.")
