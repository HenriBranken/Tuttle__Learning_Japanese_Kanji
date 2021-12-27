import requests
import os

ls_kanji = [
    "山", "人", "一", "二", "三", "日", "白", "口", "回", "四", "月", "明", "木", "五", "目", "女", "大", "中", "八", "小",
    "貝", "六", "王", "玉", "心", "国", "全", "十", "早", "上", "下", "米", "自", "内", "右", "有", "肉", "半", "九", "春",
    "京", "見", "止", "七", "少", "南", "工", "左", "高", "買", "百", "円", "元", "首", "歩", "子", "好", "古", "火", "冬"
]

ls_curs_retry = []
ls_block_retry = []
for kanji in ls_kanji:
    print(kanji, end=": ")
    path_block_dest = f"http://kanji.nihongo.cz/image.php?text={kanji}&font=HGRMB.TTC&fontsize=300&color=black"
    path_curs_dest = f"http://kanji.nihongo.cz/image.php?text={kanji}&font=epgyosho.ttf&fontsize=300&color=black"

    try:
        if os.path.exists(f"{kanji}_block.pdf"):
            print("e", end=" ")
        else:
            response_block = requests.get(path_block_dest)
            with open(f"{kanji}_block.pdf", "wb") as file:
                file.write(response_block.content)
                print(1, end=" ")
    except Exception as e:
        print(0, end=" ")
        print(f"Stuggled to get the block {kanji}...")
        ls_block_retry.append(path_block_dest)

    try:
        if os.path.exists(f"{kanji}_curs.pdf"):
            print("e")
        else:
            response_curs = requests.get(path_curs_dest)
            with open(f"{kanji}_curs.pdf", "wb") as file:
                file.write(response_curs.content)
                print(1)
    except Exception as e:
        print(0)
        print(f"Struggled to get the cursive {kanji}...")
        ls_curs_retry.append(path_curs_dest)

if ls_block_retry:
    print(f"Unsuccessful cursive Kanji include: {ls_block_retry}.")
if ls_curs_retry:
    print(f"Unsuccessful cursive Kanji include: {ls_curs_retry}.")
