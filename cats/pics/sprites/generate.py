import os
import re
import json
from PIL import Image

json_obj={}

subgroups = {}

pattern=re.compile('([a-zA-Z0-9_]+)_([0-9]+)_([0-9]+).png')
files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.png')]

for f in files:
    m = pattern.match(f)

    state = m.group(1)
    sub = m.group(2)
    ind = m.group(3)

    if state not in subgroups:
        subgroups[state] = {}

    if sub not in subgroups[state]:
        subgroups[state][sub] = []

    img = Image.open(f)
    width, height = img.size
    
    subgroups[state][sub].append([width, height])

for state in subgroups:
    json_obj[state] = []
    for sub in subgroups[state]:
        json_obj[state].append(subgroups[state][sub])

json_string = json.dumps(json_obj)
print(json_string)
