#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
import json
import shutil
from operator import itemgetter
import cv2

img = cv2.imread('characters.png', cv2.IMREAD_UNCHANGED)
layout = json.load(open('characters.json'))
frames = layout['textures'][0]['frames']

for frm in frames:
    path = 'custom/' + frm['filename']
    if not os.path.isfile(path):
        continue
    x, y, w, h = itemgetter(*'xywh')(frm['frame'])
    cst = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if cst.shape != (h, w, 4):
        continue
    img[y:y+h, x:x+w] = cst

shutil.copy('characters.png', 'characters.bk.png')
cv2.imwrite('characters.png', img)
