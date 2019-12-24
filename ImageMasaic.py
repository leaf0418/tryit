import cv2
import numpy as np


def do_Mosaic(filename, neighbor):
    img = cv2.imread(filename)
    img_mosaic = img.copy()
    h, w, _ = img.shape

    for r in range(0, h, neighbor):
        for c in range(0, w, neighbor):
            patch = img[r:r + neighbor, c:c + neighbor, :]
            avg_patch = np.mean(np.mean(patch, axis=0), axis=0)
            avg_patch = np.expand_dims(np.expand_dims(avg_patch, 0), 0)
            img_mosaic[r:r + neighbor, c:c + neighbor, :] = avg_patch

    fn = filename.rsplit('.', 1)
    newfile = fn[0] + "_p." + ''.join(fn[1:])
    print(newfile)
    cv2.imwrite(newfile, img_mosaic)

    return img_mosaic


def main():
    filename = '1231.jpg'
    img = do_Mosaic(filename, 9)
    cv2.imshow('img', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()