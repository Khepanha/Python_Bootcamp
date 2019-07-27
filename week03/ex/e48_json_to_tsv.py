import os
import json
import csv
def json_to_tsv (First,Second):
    add = ''
    with open (First) as json_file:
        json_content = json.load(json_file)
        add += ("title\tcontent\tdifficulty\n")
        for el in json_content:
            if ("title" in el and "content" in el and "difficulty" in el):
                add += (el["title"] + "\t" + el["content"] + "\t" + el["difficulty"] + "\n")
            else:
                return -1
    tsv = open (Second,'w')
    tsv.write(add)
    tsv.close()
    return 1
print(json_to_tsv ())
