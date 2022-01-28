import os
from typing import Optional

KEY_WD = 'gcr'
FOLDER_NEED_SEARCH = ['apps', 'common', ]
ROOT = os.path.dirname(os.getcwd())


def get_gcr_image(filepath: str) -> Optional[str]:
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            image_line = line.split('image:')
            if len(image_line) > 1 and KEY_WD in image_line[1]:
                return image_line[1].strip()


if __name__ == "__main__":
    with open('grc_image_list.csv', 'w') as fp:
        for folder in FOLDER_NEED_SEARCH:
            current_path = os.path.join(ROOT, folder)
            for parent, dirnames, filenames in os.walk(current_path):
                for filename in filenames:
                    file = os.path.join(parent, filename)
                    gcr_image = get_gcr_image(file)
                    if gcr_image:
                        fp.write(file.replace(ROOT, '') + ',' + gcr_image + '\n')

        # for file in os.listdir(os.path.join(ROOT, folder)):
