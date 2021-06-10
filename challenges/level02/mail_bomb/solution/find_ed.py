#!/usr/bin/python3

import sys
import os
from PIL import Image
import pytesseract as pt

def find_target(path, target):
    for filename in os.listdir(path):
        filepath = Image.open(os.path.join(path, filename))
        text = pt.image_to_string(filepath, lang="eng")
        if target in text.lower():
            print("{} found in: {}".format(target, filename))
    print("Done.")
    return

def main(argv):
    if len(argv) == 3:
        find_target(argv[1], argv[2])
    else:
        print("Usage: python {} <path> <target>".format(argv[0]))
    return


if __name__ == "__main__":
    main(sys.argv)
