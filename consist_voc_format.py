"""
VOCdevkit
  |___VOC2012
     |___Annotations
     |___ImageSets
            |___Main
                   |___train.txt
                   |___valid.txt
     |___JPEGImages
"""

import shutil
import os

os.makedirs('./datasets/VOCdevkit/Annotations', exist_ok=True)



