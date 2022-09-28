import numpy as np


def my_imfilter(image, imfilter):
    """function which imitates the default behavior of the build in scipy.misc.imfilter function.

    Input:
        image: A 3d array represent the input image.
        imfilter: The gaussian filter.
    Output:
        output: The filtered image.
    """
    # =================================================================================
    # TODO:
    # This function is intended to behave like the scipy.ndimage.filters.correlate
    # (2-D correlation is related to 2-D convolution by a 180 degree rotation
    # of the filter matrix.)
    # Your function should work for color images. Simply filter each color
    # channel independently.
    # Your function should work for filters of any width and height
    # combination, as long as the width and height are odd (e.g. 1, 7, 9). This
    # restriction makes it unambigious which pixel in the filter is the center
    # pixel.
    # Boundary handling can be tricky. The filter can't be centered on pixels
    # at the image boundary without parts of the filter being out of bounds. You
    # should simply recreate the default behavior of scipy.signal.convolve2d --
    # pad the input image with zeros, and return a filtered image which matches the
    # input resolution. A better approach is to mirror the image content over the
    # boundaries for padding.
    # Uncomment if you want to simply call scipy.ndimage.filters.correlate so you can
    # see the desired behavior.
    # When you write your actual solution, you can't use the convolution functions
    # from numpy scipy ... etc. (e.g. numpy.convolve, scipy.signal)
    # Simply loop over all the pixels and do the actual computation.
    # It might be slow.

    # NOTE:
    # Some useful functions:
    #     numpy.pad (https://numpy.org/doc/stable/reference/generated/numpy.pad.html)
    #     numpy.sum (https://numpy.org/doc/stable/reference/generated/numpy.sum.html)
    # =================================================================================

    # ============================== Start OF YOUR CODE ===============================

    output = np.zeros_like(image)
    img_h, img_w, img_c = image.shape
    fil_h, fil_w = imfilter.shape
    pad_h = fil_h // 2
    pad_w = fil_w // 2
    image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w), (0, 0)),
                   'constant',
                   constant_values=0)

    # pad_mat = np.zeros((img_h+2*pad_h,img_w+2*pad_w,3))
    # pad_mat[pad_h: img_h + pad_h, pad_w: img_w + pad_w] = image

    for k in range(img_c):
        for i in range(img_h):
            for j in range(img_w):
                output[i][j][k] = np.sum(imfilter *
                                         image[i:i + fil_h, j:j + fil_w, k])
    # =============================== END OF YOUR CODE ================================

    # Uncomment if you want to simply call scipy.ndimage.filters.correlate so you can
    # see the desired behavior.
    # import scipy.ndimage as ndimage
    # output = np.zeros_like(image)
    # for ch in range(image.shape[2]):
    #    output[:,:,ch] = ndimage.filters.correlate(image[:,:,ch], imfilter, mode='constant')

    return output