import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def process(filename, binary=0, flip=0, save=0):
    img = cv.imread(filename, 0)
    if binary == 1:
        ret, img = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
    if flip == 1:
        img = cv.flip(img, 1)
    if save == 1:
        fn = filename.rsplit('.', 1)
        newfile = fn[0] + "_p." + ''.join(fn[1:])
        print(newfile)
        cv.imwrite(newfile, img)
    return img


def main():
    images = []
    images.append(process('1231.jpg', binary=1))
    images.append(process('1231.jpg', flip=1))
    images.append(process('1231.jpg', binary=1, flip=1, save=1))
    for i in range(3):
        plt.subplot(1, 3, i + 1)
        plt.imshow(images[i], 'gray')
        plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    main()
