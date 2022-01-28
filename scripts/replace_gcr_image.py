import os
from typing import Optional

KEY_WD = 'gcr'
FOLDER_NEED_SEARCH = ['apps', 'common', ]
ROOT = os.path.dirname(os.getcwd())
PREFIX = 'registry.cn-beijing.aliyuncs.com/kubeflow1_4/'

def get_gcr_image(filepath: str) -> Optional[str]:
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            image_line = line.split('image:')
            if len(image_line) > 1 and KEY_WD in image_line[1]:
                return image_line[1].strip()


if __name__ == "__main__":
    with open('dockerfile_list.csv', 'r') as fp:
        for line in fp.readlines():
            dockerfile, version, image, file_path, original_image = line.split(',')
            file = ROOT + file_path
            with open(file, 'r') as config:
                text = config.read()

                new_image_str = f'{PREFIX}{image}'
                if version != 'latest':
                    new_image_str += f':{version}'

                text = text.replace(original_image.strip(), new_image_str)
                
            with open(file, 'w') as config:
                config.write(text)



        # for file in os.listdir(os.path.join(ROOT, folder)):
