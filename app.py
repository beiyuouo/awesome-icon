# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/7/16 17:15
# Description:

__author__ = "BeiYu"

from flask import Flask, request, Response
import random
from apis.utils import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    args_ = request.args.to_dict()
    print(args_)

    args = {}
    for k, v in args_.items():
        tp = api.__annotations__.get(k, float)
        args[k] = trans(tp, v)

    resp = Response(handle(**args))
    resp.headers = {'Cache-Control': f'max-age={random.randint(60 * 10, 60 * 120)}'}
    resp.mimetype = 'image/svg+xml'

    return resp


if __name__ == '__main__':
    app.run(debug=True)
