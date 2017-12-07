import json

with open("json/law.json") as fin:
    data = json.load(fin)


special_roles = ['část', 'hlava', 'díl', 'oddíl', 'pododdíl', 'paragraf', 'odstavec', 'pododstavec', 'bod', 'článek', 'preambule']


def write_item(item, f, first=False, last=False):
    if item['role'] in ['část', 'hlava', 'díl', 'oddíl', 'pododdíl', 'paragraf', 'článek', 'preambule']:
        try:
            f.write(item['caption'] + "\n\n")
        except Exception:
            nothing = None
    elif item['role'] in ['paragraf', 'odstavec', 'pododstavec', 'bod']:
        try:
            f.write(item['caption'] + " ")
        except Exception:
            nothing = None

    try:
        f.write(item['title'] + "\n\n")
    except Exception:
        nothing = None

    try:
        if item['role'] in ['věta', 'block']:
            f.write(item['text'])
            if not last:
                f.write(" ")
            else:
                f.write("\n\n")
        else:
            f.write(item['text'] + "\n\n")
    except Exception:
        nothing = None

    try:
        i = 0
        for c in item['children']:
            if i == 0:
                first = True
            else:
                first = False
            if i == (len(item['children']) - 1):
                last = True
            else:
                last = False
            write_item(c, f, first, last)
            i += 1
    except Exception:
        nothing = None


with open("text/law.txt", "w") as fout:
    for item in data:
        write_item(item, fout)
