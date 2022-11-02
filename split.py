#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import shutil
from operator import itemgetter
import cv2

img = cv2.imread('characters.png', cv2.IMREAD_UNCHANGED)
layout = json.load(open('characters.json'))
frames = layout['textures'][0]['frames']
os.makedirs('split', exist_ok=True)

for frm in frames:
    x, y, w, h = itemgetter(*'xywh')(frm['frame'])
    cv2.imwrite('split/' + frm['filename'], img[y:y+h, x:x+w])
