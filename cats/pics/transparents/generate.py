import os
import re
import json
from PIL import Image
import math
import sys

json_obj={}

subgroups = {}

pattern=re.compile('([a-zA-Z0-9_]+)_([0-9]+)_([0-9]+).png')
files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.png')]

max_size = [0, 0]
sum_size = [0, 0]
filelen = 0

max_width = int(sys.argv[1]) if len(sys.argv) >= 2 and sys.argv[1].isdigit() else 1024

space = [0, 0]
row = 0

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
    max_size = [ max(width, max_size[0]), max(height, max_size[1]) ]
    sum_size = [ sum_size[0] + width, sum_size[1] + height ]
    
    subgroups[state][sub].append([f, width, height])
    filelen += 1
    row = max(height, row)

    if space[0] + width > max_width:
        space[0] = 0
        space[1] += row
        row = 0
    else:
        space[0] += width
space[1] += row

x = 0
y = 0
row = 0

sprites = Image.new('RGBA', (max_width, space[1]), 0)

for state in subgroups:
    json_obj[state] = []
    for sub in subgroups[state]:
        fileinfos = subgroups[state][sub]
        sub_sprites = []
        for info in subgroups[state][sub]:
            img = Image.open(info[0])
            if (x + info[1] > max_width):
                y += row
                row = 0
                x = 0
            sprites.paste(img, (x, y))
            sub_sprites.append([x, y, info[1], info[2]])
            row = max(info[2], row)
            x += info[1]
            img.close()
        json_obj[state].append(sub_sprites)

sprites.save('sprites.png', 'PNG')

json_string = json.dumps(json_obj)
print(json_string)
print(max_size)
print(sum_size)
print(space)
print(filelen, math.sqrt(filelen))
