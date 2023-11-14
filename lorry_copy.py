import glob
import os
import shutil

os.makedirs('./datasets/COCO3/annotations', exist_ok=True)
def lorry_images_copy():
    image_file_path = './datasets/training_image'
    images_path = glob.glob(os.path.join(image_file_path, '*.jpg'))
    os.makedirs('./datasets/COCO3/train2017', exist_ok=True)

    for image_path in images_path:
        image_name = image_path.split('\\')
        image_name = image_name[1]

        id = image_name.split('Truck')

        if 'Truck' in image_name:
            shutil.copyfile(image_path, f'./datasets/COCO3/train2017/{image_name}')


def lorry_txt_to_json():
    count = 0
    txt_file_path = './datasets/training_image'
    txts_path = glob.glob(os.path.join(txt_file_path, '*.txt'))

    for txt_path in txts_path:
        txt_name = txt_path.split('\\')
        txt_name = txt_name[1]

        id = txt_name.split('Truck')

        if 'Truck' not in txt_name:
            continue

        # shutil.copyfile(txt_path, f'./datasets/COCO3/train2017/{txt_name}')



lorry_images_copy()
lorry_txt_to_json()