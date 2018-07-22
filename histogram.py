#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2 as editor
import numpy as np


def calc_histogram(image):
    """Return the histogram from a image."""
    histogram = [0] * 256
    print(image)
    for row in range(image.shape[0]):
        for column in range(image.shape[1]):
            histogram[image[row, column]
                      ] = histogram[image[row, column]] + 1
    return histogram


def accumulate(histogram):
    """Return a accumulated histogram."""
    for i in range(1, len(histogram)):
        histogram[i] = histogram[i-1] + histogram[i]
    return histogram


def equalize_hist(histogram, image):
    """Equalizes the histogram."""
    # image = editor.imread(str(image_path), 0)
    interval = (0, 255)
    for i in range(1, len(histogram)):
        print(' histogram[i] ',
              histogram[i],
              ' image.shape[0]*image.shape[1] ',
              image.shape[0]*image.shape[1],
              ' div ',
              float(float(histogram[i])/float(image.shape[0]*image.shape[1])))

        histogram[i] = int(
            round((interval[1]-interval[0]) *
                  (float(histogram[i]) / float(histogram[-1])))
            )
        return histogram


def optimization(v_max, v_min, value):
    """Optimization function."""
    return (255 / v_max) * (value - v_min)


# Show a image while any key is pressed.
def show(image):
    """Show a given image till ENTER is pressed."""
    editor.imshow('press ENTER to close', image)
    editor.waitKey(0)


def apply(raw_image):
    """Appy the process of equalization of histogram."""
    image = np.array(raw_image)

    histogram = calc_histogram(image)

    acumulated_hist = accumulate(histogram)

    equalized_hist = equalize_hist(acumulated_hist, image)

    # rebuilding the image by the equalized histogram
    for row in range(image.shape[0]):
        for column in range(image.shape[1]):
            image[row, column] = equalized_hist[image[row, column]]
    return image


def main():
    """Execute the main function."""
    img = editor.imread("images/sapo.png", editor.IMREAD_GRAYSCALE)
    print(img)
    processed_image = apply(img)
    show(processed_image)


main()
