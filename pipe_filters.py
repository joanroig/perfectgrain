import os
import sys
from pathlib import Path

import cv2
import numpy as np
from blendmodes.blend import BlendType, blendLayers
from PIL import Image

indirectory=sys.argv[1]
outdirectory=sys.argv[2]
filter=sys.argv[3]
# Opaque is 255, input between 0-255
opacity=int(sys.argv[4])

Path(f'{outdirectory}').mkdir(parents=True, exist_ok=True)
 
files = os.listdir(indirectory)

# iterate files
for index, filename in enumerate(files):
    f = os.path.join(indirectory, filename)
    if os.path.isfile(f):

        print(f"Processing: {index + 1} of {len(files)}")

        filename = Path(f).stem
        source = cv2.imread(f)
        dimensions = source.shape
        height = source.shape[0]
        width = source.shape[1]

        # Convert cv2 image to PIL
        img = cv2.cvtColor(source, cv2.COLOR_BGR2RGB)
        im_pil = Image.fromarray(img)

        # Add noise overlay: https://github.com/FHPythonUtils/BlendModes
        background = im_pil
        foreground = Image.open(filter).crop((0, 0, width, height ))
        foreground.putalpha(opacity)
        blended = blendLayers(im_pil, foreground, BlendType.OVERLAY)

        # Remove alpha channel
        bg = Image.new('RGBA', blended.size, (255,255,255))
        final = Image.alpha_composite(bg, blended)

        # Save file with filters
        final.save(f'{outdirectory}/{filename}.png')