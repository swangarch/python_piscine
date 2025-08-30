#!/usr/bin/python3

import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray | None:
    """Function that loads an image with path, prints its format,
    and its pixels content in RGB format. The function works with
    JPG and JPEG format."""

    try:
        img = Image.open(path)
        arr = np.array(img)
        return arr

    except Exception as e:
        print("Error:", e)
        return None
