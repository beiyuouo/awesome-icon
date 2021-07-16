# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/7/16 17:23
# Description:

__author__ = "BeiYu"

import os

gh_token = ''
env_dict = os.environ

if 'GITHUB_TOKEN' in env_dict.keys():
    gh_token = env_dict['GITHUB_TOKEN']
