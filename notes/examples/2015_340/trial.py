import json
import yaml

with open("law.yaml") as fin:
    data = yaml.load(fin)

with open("law_dump.yaml", "w") as fout:
    yaml.dump(data, fout, allow_unicode=True)

with open("law.json") as fin:
    data = json.load(fin)
