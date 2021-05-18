# python -m perception_tools from parent folder

from .perception_convert import *

perception_folder = '/home/user/.config/unity3d/DefaultCompany/tutorial/a37a249f-940d-47fc-947b-143f325114e2'

if __name__ == '__main__':
    print(perception_folder)
    coco_dataset_dict = convert_perception(perception_folder)

    print(coco_dataset_dict.keys())
