import time
import argparse
import sys
import os
import numpy as np
import imageio.v3 as iio

import removeWhite


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Removes white from an RGB image, returning an adjusted RGB + Alpha',
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-i", "--image",
                        help="path to an image, any opencv supported formates",
                        type=str, required=True)

    parser.add_argument("-a", "--alpha_suffix",
                    help="Alpha Suffix, only if you want a seperate alpha,\n"
                    "or for file formats that dont support alpha",
                    type=str, required=False)

    parser.add_argument("--plugin",
                    help="[Advanced] plugin to use for writing the results,"
                    " may require installation\n"
                    "freeimage, pillow, ITK, GDAL, tifffile\n"
                    "compleate list: https://imageio.readthedocs.io/en/stable/formats/formats_by_plugin.html ",
                    type=str, required=False)

    parser.add_argument("-o", "--output",
                        help="Path and filename to write the results",
                        type=str, required=True)

    # print help message if bad input
    try:
        args = parser.parse_args()
        if not args.plugin:
            args.plugin = None
    except:
        print("Bad input paramater")
        parser.print_help()
        sys.exit(0)
 
    img = iio.imread(args.image)

    tick = time.perf_counter()
    img, alpha = removeWhite.RemoveWhite(img)
    tock = time.perf_counter()
    print(f"Time: {tock - tick:0.4f} seconds")

    if args.alpha_suffix:
        iio.imwrite(args.output, img, plugin=args.plugin)

        # build alpha path with user designated suffix
        alpha_path = os.path.splitext(args.output)[0]
        alpha_path = alpha_path + args.alpha_suffix
        alpha_path = alpha_path + os.path.splitext(args.output)[1]

        # expects 3 channels as seperate file
        alpha_out = np.dstack((alpha, alpha, alpha))
        iio.imwrite(alpha_path, alpha_out, plugin=args.plugin)
    else:
        img = np.dstack((img, alpha))
        iio.imwrite(args.output, img, plugin=args.plugin)
