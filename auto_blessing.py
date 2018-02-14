# -*-coding:utf-8-*-
import os
import time
from PIL import Image  # PIL(Python Imaging Library)提供基本图像操作,比如图像缩放、裁剪、旋转、颜色转换等

logpath = "/home/dmrf/fu"


def push_button(img, rec):
    c = img.getpixel((rec['x'], rec['y']))
    print("{:d} {:d} ".format(rec['x'], rec['y']), c)
    if c == rec['color']:
        os.system("adb shell input tap {:d} {:d}".format(rec['x'], rec['y']))


def fu(fn):
    try_again = {
        'x': 550,
        'y': 1760,
        'color': (154, 102, 0, 255)
    }
    in_fu = {
        'x': 540,
        'y': 1600,
        'color': (253, 206, 118, 255)
    }
    img = Image.open(fn)
    push_button(img, try_again)
    push_button(img, in_fu)
    os.system("adb shell input tap 96 1225")


while True:
    t = int(time.time())
    fn = "{:s}/fu{:d}.png".format(logpath, t)
    print('截屏', os.system("adb shell screencap -p /sdcard/fu.png"))
    print('下载', os.system("adb pull /sdcard/fu.png " + fn))
    fu(fn)
