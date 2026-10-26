import csv
import json
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path

BRANDS = {
    "APPLE", "SAMSUNG", "XIAOMI", "REDMI", "POCO", "HUAWEI", "HONOR", "OPPO", "REALME", "VIVO",
    "ONEPLUS", "GOOGLE", "MOTOROLA", "NOKIA", "HMD", "SONY", "ASUS", "ASUSTEK", "NOTHING", "LENOVO",
    "ZTE", "TCL", "ALCATEL", "TECNO", "INFINIX", "ITEL", "LG", "BLACKVIEW", "DOOGEE", "ULEFONE",
    "CAT", "FAIRPHONE",
}

UPPER = {"TCL", "ZTE", "LG", "HMD", "SE", "XL", "FE", "GB", "TB", "NFC", "LTE", "UW", "II", "III", "IV", "V2", "S"}
FIXED = {"IPHONE": "iPhone", "IPAD": "iPad", "ONEPLUS": "OnePlus", "REALME": "realme", "POCO": "POCO", "ASUSTEK": "ASUS"}


def pretty(name):
    words = []
    for w in name.split():
        u = w.upper()
        if u in FIXED:
            words.append(FIXED[u])
        elif u in UPPER or re.fullmatch(r"\d+G", u) or re.search(r"\d", u):
            words.append(u)
        else:
            words.append(w.capitalize())
    return " ".join(words)


def main(src, out):
    out = Path(out)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    shards = defaultdict(dict)
    with open(src, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            brand = row["Brand"].strip().upper()
            tac = row["TAC"].strip()
            if brand not in BRANDS or not re.fullmatch(r"\d{8}", tac):
                continue
            name = pretty(row["SPECS"].split(",")[0].strip())
            if name:
                shards[tac[:3]][tac] = name
    total = 0
    for prefix, entries in sorted(shards.items()):
        names = sorted(set(entries.values()))
        index = {n: i for i, n in enumerate(names)}
        data = {"n": names, "t": {t: index[n] for t, n in sorted(entries.items())}}
        (out / f"{prefix}.json").write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        total += len(entries)
    print(f"{total} TAC in {len(shards)} fisiere")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
