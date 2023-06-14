# https://www.mdpi.com/1424-8220/22/22/8801

import os

import numpy as np
import supervisely as sly
from dotenv import load_dotenv
from supervisely.io.fs import (
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)

# # if sly.is_development():
# load_dotenv("local.env")
# load_dotenv(os.path.expanduser("~/supervisely.env"))

# api = sly.Api.from_env()
# team_id = sly.env.team_id()
# workspace_id = sly.env.workspace_id()


# project_name = "Insulator-Defect Detection"
dataset_path = "/home/alex/DATASETS/TODO/Insulator-Defect Detection/VOC/images"
anns_path = "/home/alex/DATASETS/TODO/Insulator-Defect Detection/VOC/labels"
batch_size = 30
images_ext = ".jpg"
ann_ext = ".txt"


def create_ann(image_path, ds_name):
    labels = []

    image_np = sly.imaging.image.read(image_path)[:, :, 0]
    img_height = image_np.shape[0]
    img_wight = image_np.shape[1]

    ann_path = os.path.join(anns_path, ds_name, get_file_name(image_path) + ann_ext)

    if file_exists(ann_path):
        with open(ann_path) as f:
            content = f.read().split("\n")

            for curr_data in content:
                if len(curr_data) != 0:
                    curr_data = list(map(float, curr_data.split(" ")))
                    obj_class = idx_to_class[int(curr_data[0])]

                    left = int((curr_data[1] - curr_data[3] / 2) * img_wight)
                    right = int((curr_data[1] + curr_data[3] / 2) * img_wight)
                    top = int((curr_data[2] - curr_data[4] / 2) * img_height)
                    bottom = int((curr_data[2] + curr_data[4] / 2) * img_height)
                    rectangle = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
                    label = sly.Label(rectangle, obj_class)
                    labels.append(label)

    return sly.Annotation(img_size=(img_height, img_wight), labels=labels)


obj_class_pollution = sly.ObjClass("pollution-flashover", sly.Rectangle)
obj_class_broken = sly.ObjClass("broken", sly.Rectangle)
obj_class_insulator = sly.ObjClass("insulator", sly.Rectangle)

idx_to_class = {0: obj_class_pollution, 1: obj_class_broken, 2: obj_class_insulator}


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=list(idx_to_class.values()))
    api.project.update_meta(project.id, meta.to_json())

    for ds_name in os.listdir(dataset_path):
        images_path = os.path.join(dataset_path, ds_name)

        images_names = os.listdir(images_path)

        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

        for images_names_batch in sly.batched(images_names, batch_size=batch_size):
            img_pathes_batch = [
                os.path.join(images_path, image_name) for image_name in images_names_batch
            ]

            img_infos = api.image.upload_paths(dataset.id, images_names_batch, img_pathes_batch)
            img_ids = [im_info.id for im_info in img_infos]

            anns = [create_ann(image_path, ds_name) for image_path in img_pathes_batch]
            api.annotation.upload_anns(img_ids, anns)

            progress.iters_done_report(len(images_names_batch))

    return project
