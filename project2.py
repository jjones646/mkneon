#!/usr/bin/env python2

# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np


def main(args):
    """Main wrapper function.
    """
     im = cv2.imread(args.image.name)
     imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
     ret,thresh = cv2.threshold(imgray,127,255,0)
     im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Project 2 for Computational Photography by Jonathan Jones')
    parser.add_argument('image', type=argparse.FileType('r'), help='Image to operate on')
    args = parser.parse_args()
    main(args)
