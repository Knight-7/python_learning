import glob
import os
import threading

from PIL import Image

PREFIX = 'thumbnails'


def generate_thumbnail(infle, size, format='PNG'):
    """生成指定图片的缩略图"""