import numpy as np
import matplotlib
import cv2


# Removes white from an RGB image and creates an alpha mask
# Supports 8-bit 16-bit 32-bit images
def RemoveWhite(img):
    source_type = img.dtype
    # get the origional value range
    max_value = np.iinfo(source_type).max

    # convert to HSV for processing
    if source_type == 'uint8':
        # use opnecv for faster 8 bit conversion
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        (h, s, v) = np.dsplit(img, img.shape[-1])
        h = h.astype(float) / max_value
        s = s.astype(float) / max_value
        v = v.astype(float) / max_value
    else:
        # use matplotlib for all other types, slow
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

    # return to source scale
    alpha *= max_value
    #  return to source type
    rgb = rgb.astype(source_type)
    alpha = alpha.astype(source_type)

    return rgb, alpha
