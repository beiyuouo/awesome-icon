# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/7/16 22:31
# Description:

__author__ = "BeiYu"


import time
import base64
import colorsys
import statistics
from pathlib import Path
from functools import lru_cache

import cv2
import hrml
import jinja2
import requests
import numpy as np
from github import Github

from apis import config

g = Github(config.gh_token)


def get_star(name):
    return _get_star(name, int(time.time()) // 1800)


@lru_cache(maxsize=1024)
def _get_star(name, t):
    repo = g.get_repo(name)
    return repo.stargazers_count


def trans(tp, x):
    try:
        return tp(x)
    except Exception:
        return x


dir = Path(__file__).absolute().parent.parent

template = jinja2.Template(
    hrml.masturbate(
        open(dir / 'templates/template.hrml', encoding='utf8').read()
    )
)

MB = 1024 * 1024


def middle_center_cut(img):
    r, c = img.shape[:2]
    d = abs(r - c) // 2
    if r > c:
        return img[d:d + c, :]
    else:
        return img[:, d:d + r]


def main_color(img):
    img = img[:, :, :3]
    img = cv2.resize(img, (32, 32))
    img //= 16
    img *= 16
    r, c = img.shape[:2]
    img = img.reshape((r * c, 3))
    color = statistics.mode(map(tuple, img))
    return np.array(color, dtype=np.int32)


@lru_cache(maxsize=16)
def download(url, limit_size):
    r = requests.get(url, stream=True)
    data = r.raw.read(limit_size)
    return data


@lru_cache(maxsize=4)
def original(url):
    if not url:
        img_data = open(dir / 'templates/template.jpg', 'rb').read()
    else:
        img_data = download(url, 10 * MB)
        if len(img_data) == 10 * MB:
            raise Exception('Too large!')
    img = cv2.imdecode(np.frombuffer(img_data, np.uint8), -1)
    img = middle_center_cut(img)
    return img


@lru_cache(maxsize=512)
def _original(url, limit):
    img = original(url)
    backcolor = main_color(img)[::-1]
    if img.shape[0] > limit:
        img = cv2.resize(img, (limit, limit))
    good, data = cv2.imencode('.webp', img, [cv2.IMWRITE_WEBP_QUALITY, 75])
    if not good:
        raise Exception('imencode fail')
    data = base64.b64encode(data).decode()
    return data, backcolor


def color(h):
    r = int(h[0:2], 16)
    g = int(h[2:4], 16)
    b = int(h[4:6], 16)
    return r, g, b


@lru_cache(maxsize=1024)
def api(url: str = None, txt: str = '好!', size=32, border=3, barlen='auto', fontsize=15, barradius=5, scale=1,
        fontcolor: color = 'auto', shadow=0.5, backcolor: color = 'auto', anime=0.5):
    print([url, txt, size, border, barlen, fontsize, barradius, scale, fontcolor, shadow, backcolor, anime])
    if barlen == 'auto':
        l = len(txt) + len([x for x in txt if ord(x) > 127]) * 0.84
        barlen = fontsize * l * 0.55 + 2.6 * border

    size, border, barlen, fontsize, barradius = [int(x * scale) for x in (size, border, barlen, fontsize, barradius)]

    bb, b_color = _original(url, (size - 2 * border) * 4)
    if backcolor == 'auto':
        backcolor = b_color
    else:
        backcolor = np.array(backcolor, dtype=float)

    if fontcolor == 'auto':
        if backcolor.mean() > 214:
            fontcolor = (33, 33, 33)
        else:
            fontcolor = (255, 255, 255)

    h, l, s = colorsys.rgb_to_hls(*backcolor / 255)
    color1 = np.array(colorsys.hls_to_rgb(h, l + 0.02, s)) * 255
    color2 = np.array(colorsys.hls_to_rgb(h, l - 0.06, s)) * 255
    s = template.render(
        size=size,
        border=border,
        shadow=shadow,
        barradius=barradius,
        barlen=barlen,
        bartxt=txt,
        color1=color1,
        color2=color2,
        fontcolor=fontcolor,
        fontsize=fontsize,
        anime=anime,
        radius=99999,
        b64='data:image/webp;base64,' + bb,
    )
    return s


def handle(**d):
    try:
        repo = d.pop('repo', '')
        if repo:
            txt = f'☆{get_star(repo)}'
            return api(txt=txt, **d)
        print(d)
        return api(**d)
    except Exception as e:
        return api(txt=repr(e))