import cv2 as editor
import hist
import numpy as np

# import matplotlib.pyplot as plotter
# import pyplotter as plotter
# import matplotlib.pyplot as plt
extreme_values = [0, 0]


# def accumulate(histogram):
#     i = 0
#     accumulated[i] = histogram[i]
#     while i < ((len(histogram)) - 1):
#         acumulated[] =


def convert(vis):
    """Convert a image to grayscale."""
    vis2 = editor.cvtColor(vis, editor.COLOR_GRAY2BGR)
    return vis2


def is_extreme(number):
    """Update the min or max values according to the given number."""
    if number > extreme_values[1]:
        extreme_values[1] = number
    if number < extreme_values[0]:
        extreme_values[0] = number


def optimization(v_max, v_min, value):
    """Optimization function."""
    return (255 / v_max) * (value - v_min)


# Show a image while any key is pressed.
def show(image):
    """Show a given image till ENTER is pressed."""
    editor.imshow('press ENTER to close', image)
    editor.waitKey(0)


# Returns the number of times each value apears on image.
def countValues(image_path1):
    """Count the pixels per RGB value."""
    image1 = editor.imread(str(image_path1), 0)
    histogram = [0] * 256
    # histogram[255]
    i = 0
    extreme_values[0] = image1[0][0]
    extreme_values[1] = image1[0][0]
    while i < len(image1):
        j = 0
        while j < len(image1):
            value = int(image1[i][j])
            histogram[value] = histogram[value] + 1
            is_extreme(value)
            j = j + 1
        i = i + 1
    return histogram


def equalization(image_path1):
    """Equalizes the histogram."""
    countValues(image_path1)
    image1 = editor.imread(str(image_path1), 0)
    i = 0
    while i < len(image1):
        j = 0
        while j < len(image1):
            value = int(image1[i][j])
            image1[i][j] = int(optimization(extreme_values[1],
                                            extreme_values[0],
                                            value))
            j = j + 1
        i = i + 1
    return image1


def main():
    """Execute the main function."""
    # his = countValues('images/teste.png')
    # img = convert(editor.imread('images/teste.png', 0))
    img = editor.imread('images/teste.png')
    image = hist.histeq(img)
    show(image)

    # print_array(his)
    # print(extreme_values)
    # show(equalization('images/sapo.png'))


main()
