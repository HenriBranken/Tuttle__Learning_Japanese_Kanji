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
    "段": "grade"
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
