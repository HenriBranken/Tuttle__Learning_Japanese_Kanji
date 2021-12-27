import requests
import os

ls_kanji = [
    "山", "人", "一", "二", "三", "日", "白", "口", "回", "四", "月", "明", "木", "五", "目", "女", "大", "中", "八", "小",
    "貝", "六", "王", "玉", "心", "国", "全", "十", "早", "上", "下", "米", "自", "内", "右", "有", "肉", "半", "九", "春",
    "京", "見", "止", "七", "少", "南", "工", "左", "高", "買", "百", "円", "元", "首", "歩", "子", "好", "古", "火", "冬",
    "水", "安", "力", "夏", "千", "休", "手", "本", "化", "川", "体", "北", "田", "男", "家", "東", "思", "耳", "父", "言",
    "干", "金", "語", "士", "朝", "青", "土", "掛", "万", "雨", "電", "売", "者", "入", "雪", "門", "間", "出", "生", "牛",
    "美", "島", "寸", "寺", "先", "開", "鳥", "夕", "外", "舌", "図", "立", "親", "星", "秋", "西", "刀", "切", "曜", "周",
    "読", "斤", "天", "分", "物", "道", "新", "花", "名", "母", "私", "夜", "前", "多", "持", "書", "音", "会", "聞", "央",
    "近", "失", "弓", "馬", "週", "引", "秒", "甲", "気", "時", "話", "英", "訓", "押", "年", "来", "学", "意", "又", "赤",
    "公", "巾", "市", "主", "丁", "友", "団", "毎", "空", "町", "犬", "死", "行", "取", "村", "字", "具", "注", "品", "里",
    "林", "森", "旦", "黒", "交", "不", "後", "最", "太", "車", "受", "凶", "海", "校", "足", "糸", "同", "午", "愛", "離",
    "信", "酒", "進", "文", "戸", "事", "待", "兄", "県", "背", "晴", "走", "洗", "己", "転", "楽", "理", "番", "両", "民",
    "付", "弔", "泣", "銀", "問", "暗", "絵", "氏", "若", "由", "申", "要", "至", "比", "計", "所", "第", "旨", "着", "欠",
    "画", "可", "神", "亡", "占", "世", "定", "紙", "采", "軍", "姉", "羊", "介", "台", "急", "州", "辛", "服", "吉", "用",
        "次", "低", "孝", "茶", "利", "未", "末", "斗", "遊", "豆",
    "屋", "各", "形", "的", "矢", "界", "反", "良", "配", "遠", "忘", "完", "且", "都", "降", "婚", "祭", "指", "予", "活",
        "和", "経", "頭", "魚", "実"
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
