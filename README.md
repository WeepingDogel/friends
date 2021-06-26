# 一个自动生成友链页面的脚本
![](resources/Screenshot-2021-06-26-at-20-17-17-Friends.png)

# 使用
## 直接 git 到本地即可
```
$ git clone 
```
## 关于配置文件

添加友链时
```toml
[friends]
number = 2 #友链总数
    [friends.1]
    Avatar = "https://avatars.githubusercontent.com/u/440661" # 这里一般是图片的网络地址
    Title = "依云's Blog" # 博客标题
    URL = "https://blog.lilydjwg.me/" # 链接
    Bio = "Happy coding, happy living!" # Bio
    [friends.2]
    Avatar = "https://avatars.githubusercontent.com/u/34574198"
    Title = "李皓奇"
    URL = "https://liolok.com/zhs/"
    Bio = "岂有文章倾社稷，从来佞幸覆乾坤。"
```

**number** 的值绝对不能低于实际友链总数！否则会报错～

**Avatar** 一般是个图片链接
