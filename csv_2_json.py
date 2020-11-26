import csv
from collections import namedtuple
import json


class Kanji:
    def __init__(self, id, kanji, level, meaning, readings):
        self.id = int(id)
        self.kanji = [kanji]
        self.level = level
        self.meaning = meaning
        self.readings = readings
        self.compounds = [["", "", ""]]


kanji_collection = []

with open("kanji_list.csv") as f:
    csv_reader = csv.reader(f, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            readings = []
            for r in row[6].strip().split("、"):
                readings.append(r)
            info = Kanji(
                row[0].strip(),
                row[1].strip(),
                row[4].strip(),
                row[5].strip(),
                readings,
            )
            print(info)
            kanji_collection.append(info)
            line_count += 1
    print(f"Processed {line_count} lines.")


def generate_json(level: str):
    kanji_list = []

    for kanji in kanji_collection:
        if kanji.level == level:
            kanji_list.append(kanji.__dict__)

    with open(f'level_{level}.json', 'w', encoding='utf8') as json_file:
        json.dump(kanji_list, json_file, ensure_ascii=False)


generate_json("3")
