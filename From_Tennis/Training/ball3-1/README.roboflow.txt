
ball3 - v1 2023-10-24 1:21pm
==============================

This dataset was exported via roboflow.com on October 24, 2023 at 7:26 PM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 838 images.
Ball-Il4U are annotated in COCO Segmentation format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Fit (black edges))

The following augmentation was applied to create 3 versions of each source image:
* Random brigthness adjustment of between -47 and +47 percent
* Random Gaussian blur of between 0 and 1.25 pixels
* Salt and pepper noise was applied to 3 percent of pixels

The following transformations were applied to the bounding boxes of each image:
* Random brigthness adjustment of between -12 and +12 percent


