import cv2
import numpy as np


def do_Mosaic(filename, patch):
    img = cv2.imread(filename)
    img_mosaic = img.copy()
    h, w, _ = img.shape

    if patch == 'Big':
        patch_size = 10
    elif patch == 'Mid':
        patch_size = 30
    else:
        patch_size = 50

    neighbor_h = int(h / patch_size)
    neighbor_w = int(w / patch_size)

    for r in range(0, h, neighbor_h):
        for c in range(0, w, neighbor_w):
            patch = img[r:r + neighbor_h, c:c + neighbor_w, :]
            avg_patch = np.mean(np.mean(patch, axis=0), axis=0)
            avg_patch = np.expand_dims(np.expand_dims(avg_patch, 0), 0)
            img_mosaic[r:r + neighbor_h, c:c + neighbor_w, :] = avg_patch

    fn = filename.rsplit('.', 1)
    newfile = fn[0] + "_q." + ''.join(fn[1:])
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