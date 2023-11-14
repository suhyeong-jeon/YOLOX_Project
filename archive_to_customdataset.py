import os
import glob
import json
import shutil
from pycocotools.coco import COCO
from collections import OrderedDict


image_paths = glob.glob(os.path.join('./datasets/archive', '*', '*', '*.jpg'))
json_path = './datasets/archive/drone-mscoco.json'
# print(image_paths)


os.makedirs('./datasets/COCO2/train2017', exist_ok=True)
os.makedirs('./datasets/COCO2/val2017', exist_ok=True)
for path in image_paths:
    splitted = path.split('\\')
    image_file_name = splitted[3].split('_')[1]
    image_file_name =  image_file_name.lstrip("0")
    if splitted[1] == 'Drone' and splitted[2] == '3300':

        shutil.copyfile(path, f'./datasets/COCO2/val2017/{os.path.basename(path)}')
    elif splitted[1] == 'Drone' and splitted[2] != 'frames':
        shutil.copyfile(path, f'./datasets/COCO2/train2017/{os.path.basename(path)}')


train_json = {}
train_json['annotations'] = []
train_json['categories'] = []
train_json['images'] = []

val_json = {}
val_json['annotations'] = []
val_json['categories'] = []
val_json['images'] = []


os.makedirs('./datasets/COCO2/annotations', exist_ok=True)

with open(json_path, 'r') as j:
    data = json.load(j)
    dataset = data
    anno = dataset['annotations']

    for an in anno:
        bbox = an['bbox']
        # bbox[2] = bbox[0] + bbox[2]
        # bbox[3] = bbox[1] + bbox[3]
        # an['bbox'][2] = bbox[2]
        # an['bbox'][3] = bbox[3]
        if int(an['image_id']) < 3300:
            train_json['annotations'].append(an)
        else:
            val_json['annotations'].append(an)

    for category in dataset['categories']:
        train_json['categories'].append(category)
        val_json['categories'].append(category)

    for image in dataset['images']:
        image_file_name = image['file_name']
        image_name = image_file_name.split('-')[1]
        image_name = image_name.split('_')[1]
        image_name = image_name.lstrip("0")
        image_name = image_name.replace('.jpg', '')
        image['file_name'] = os.path.basename(image_file_name)

        if int(image_name) < 3300:
            train_json['images'].append(image)
        else:
            val_json['images'].append(image)


with open('./datasets/COCO2/annotations/instances_train2017.json', 'w') as json_file:
    json.dump(train_json, json_file, indent=4)

with open('./datasets/COCO2/annotations/instances_val2017.json', 'w') as json_file:
    json.dump(val_json, json_file, indent=4)