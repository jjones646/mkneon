#!/usr/bin/env python2

"""
Jonathan Jones
Computational Photography
Project 2
"""

# Python 2/3 compatibility
from __future__ import print_function

import os
import cv2
import numpy as np
from random import randint

from make_unique import add_unique_postfix


def get_contours_at_thresh(image, threshold, blur=(65,65)):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, blur, 0)
    # threshold then clean out some noise
    thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    return cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]


def main(args):
    """Main wrapper function.
    """
    #  read in the image
    im = cv2.imread(args.image.name)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # named window so we can set it's display size later
    cv2.namedWindow("Contours", cv2.WINDOW_NORMAL);

    # blank image for drawing the contours
    im_gen = np.zeros((im.shape[0], im.shape[1], 3), np.uint8)

    # set a random step size for how we iterate over the threshold values
    step = randint(15, 100)

    # iterate over everything
    for thresh in range(5, 250, step):
        thickness = randint(1, 30)
        for c in get_contours_at_thresh(im, thresh):
            color = tuple([randint(0, 255) for i in range(3)])
            # cv2.drawContours(im_gen, [c], -1, color, cv2.CV_FILLED)
            cv2.drawContours(im_gen, [c], -1, color, thickness, cv2.CV_AA)

    # uncomment below to add edges
    # edges = cv2.Canny(gray, 250, 550, apertureSize=7)
    # lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, 100, 10)
    # for x1,y1,x2,y2 in lines[0]:
    #     cv2.line(im_gen, (x1,y1), (x2,y2), (0,200,0), 20)

    # show the image
    if args.display:
        cv2.imshow("Contours", im_gen)
        cv2.resizeWindow("Contours", 800, 800);
        cv2.waitKey(0)

    # save the resulting image
    fn = add_unique_postfix(os.path.basename(args.image.name))
    print('saving to {}'.format(fn))
    cv2.imwrite(fn, im_gen)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Project 2 for Computational Photography by Jonathan Jones')
    parser.add_argument('image', type=argparse.FileType('r'), help='Image to operate on')
    parser.add_argument('-d', '--display', action='store_true', help='Display the computed image before saving')
    args = parser.parse_args()
    main(args)
