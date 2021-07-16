# Awesome-icon

自定义的小图标，基于Flask和OpenCV实现

![](https://awesome-icon.vercel.app/?repo=beiyuouo/awesome-icon)

![](https://awesome-icon.vercel.app/?txt=好耶)

# Usage

对于显示仓库star数，在README中的等价写法`![](https://awesome-icon.vercel.app/?repo=beiyuouo/awesome-icon)`

对于显示文字的，需要空缺`repo`参数，`![](https://awesome-icon.vercel.app/?txt=好耶)`

可选参数

<details>
    <summary>点击展开</summary>

## `url`
图片链接
默认值：`None`

## `repo`
仓库`<用户名>/<仓库名>`

## `txt`
文字内容
默认值：`好！`

## `size`
图片大小
默认值：`32`

## `border`
边界
默认值：`3`

## `barlen`
长度
默认值`auto`

## `fontsize`
字体大小
默认值：`15`

## `barradius`
默认值：`5`

## `scale`
默认值：`1`

## `fontcolor`
字体颜色
默认值：`auto`

## `shadow`
阴影
默认值：`0.5`

## `backcolor`
背景颜色
默认值：`auto`

## `anime`
动画时间
默认值：`0.5`

</details>



# Deployment
首先申请一个Github的token，至少要拥有仓库权限

步骤：右上角头像->Settings->Developer settings->Personal access tokens->Generate new token->Select scopes->repo->Generate token

> 请不要将此token交给任何人!

点击下方按钮部署到vercel

[![Deploy to Vercel](https://camo.githubusercontent.com/f209ca5cc3af7dd930b6bfc55b3d7b6a5fde1aff/68747470733a2f2f76657263656c2e636f6d2f627574746f6e)](https://vercel.com/import/project?template=https://github.com/beiyuouo/awesome-icon)

配置环境变量`GITHUB_TOKEN`
![](docs/images/gh_token_env_init)

根据vercel分配的domain就可以愉快的玩耍了！

# Reference
- [https://github.com/RimoChan/unv-shield](https://github.com/RimoChan/unv-shield) - 我实在看不惯这种中文编程了呜呜呜