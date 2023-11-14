import json


json_path = './datasets/archive/drone-mscoco.json'

"""
COCO_CLASSES = (
    "Human",
)
"""

with open(json_path, 'r') as j:
    data = json.load(j)
    dataset = data
    categories = dataset['categories']

    for category in categories:
        print('"', end="")
        print(category['name'], end="")
        print('",')