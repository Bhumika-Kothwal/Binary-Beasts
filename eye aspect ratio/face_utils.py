def rect_to_bb(rect):
    # rect-> assumed to be a bounding box rectangle produced by dlib detector
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y
    return x, y, w, h


def shape_to_np(shape, dtype='int'):
    # initialize the list of (x,y)-coordinates
    coords = np.zeros((68, 2), dtype=dtype)

    # looping over 68 facial landmarks and converting them to a 2-tuple of (x, y) coordinates
    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    return coords


