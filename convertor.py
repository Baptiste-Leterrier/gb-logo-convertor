#!/usr/bin/env python3

import subprocess
import numpy as np
from PIL import Image
import sys

# Color used are the one set in doc https://www.gbstudio.dev/docs/assets/backgrounds
palette = [
    7,24,33,
    48,104,80,
    134,192,108,
    224,248,207
    ] + [0,] * 232 * 3


# Write "map.png" that is a 24x1 pixel image with one pixel for each colour
entries = 24
resnp   = np.arange(entries,dtype=np.uint8).reshape(24,1)
resim = Image.fromarray(resnp, mode='P')
resim.putpalette(palette)
resim.save('map.png')

# Use Imagemagick to remap to palette saved above in 'map.png'
subprocess.run(['magick', sys.argv[1], '+dither', '-quantize', 'Lab', '-remap', 'map.png','result.png'])
# Resize image to 160x144 (remove ! to keep the image ratio)
subprocess.run(['convert', 'result.png', '-resize', '160x144!', 'final.png'])
