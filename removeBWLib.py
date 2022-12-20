# Copyright (C) 2010-2022, Mikeal Simburger
#
# removeBW is distributed under the terms of the new BSL License.
# The full license can be found in 'license.txt'.


import numpy as np
import matplotlib
import cv2


# Removes white from an RGB image
# returns altered image and alpha mask
# Supports RGB 8/16-bit images
def RemoveWhite(img):
    source_type = img.dtype
    
    # get the origional value range
    if (source_type == 'float32') | (source_type == 'float64'):
        max_value = 1.0
    else:
        max_value = np.iinfo(source_type).max

    # convert to HSV for processing
    if source_type == 'uint8':
        # use opencv for much faster 8 bit conversion
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        (h, s, v) = np.dsplit(img, img.shape[-1])
        
        # type conversion is faster after split
        h = h.astype(float) / max_value
        s = s.astype(float) / max_value
        v = v.astype(float) / max_value
    else:
        # use matplotlib for all other types, slow, accuate
        img = img.astype(float)
        img /= max_value
        hsv = matplotlib.colors.rgb_to_hsv(img)
        (h, s, v) = np.dsplit(hsv, hsv.shape[-1])

    # define alpha
    alpha = 1.0-(v-s)
    # fix bounds
    alpha = np.fmin(np.fmax(alpha, 0.0, alpha), 1.0, alpha)

    # adjust to compensate for tranparency
    s = np.where((alpha < 1.0),
                 np.divide(s, alpha, s,
                           where=((alpha != 0.0) & (alpha < 1.0))), s)
    v = np.where((alpha < 1.0), s, v)

    s = np.fmin(np.fmax(s, 0.0, s), 1.0, s)
    v = np.fmin(np.fmax(v, 0.0, v), 1.0, v)

    # merge channels
    if source_type == 'uint8':
        # faster 8 bit method
        h *= max_value
        s *= max_value
        v *= max_value
        img = np.dstack((h.astype(source_type),
                        s.astype(source_type),
                        v.astype(source_type)))
        # to rgb
        rgb = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    else:
        img = np.dstack((h, s, v))
        # to rgb
        rgb = matplotlib.colors.hsv_to_rgb(img)
        # return to source scale
        rgb *= max_value

    # return alpha to source scale
    alpha *= max_value
    #  return to source type
    if rgb.dtype != source_type:
        rgb = rgb.astype(source_type)
    if alpha.dtype != source_type:
        alpha = alpha.astype(source_type)

    return rgb, alpha


def RemoveBlack(img):
    # invert image
    max_value = np.iinfo(img.dtype).max
    img = max_value - img

    img, alpha = RemoveWhite(img)

    # invert image back
    img = max_value - img

    return img, alpha
