# 安装配置AidLux环境

同济子豪兄 2023-6-25 7-26

## 加入AidLux社群

添加AidLux小助手（微信号：AidLux_Me），回复“子豪兄”，免费加入答疑社群

## 官网

官网：https://aidlux.com

文档：https://docs.aidlux.com

## 第一步：安装APP

手机应用市场下载AidLux

## 第二步：配置APP

赋予各种系统权限，打开手机开发者模式，按照提示完成配置

手机和电脑连接同一个Wifi

阅读`新手指引`

## 第三步：获取手机IP地址

在手机上点击`Cloud+ip`蓝色云朵图标，获取IP地址，例如：`192.168.1.4:8000`

## 第四步：电脑浏览器访问AidLux桌面

在电脑浏览器中输入IP地址

默认密码：`aidlux`

## 第五步：电脑命令行SSH访问AidLux

- 在电脑上，打开SSH工具，输入IP地址，访问AidLux

例如：PuTTY：https://www.putty.org

例如：命令行直接输入`ssh root@192.168.1.4 -p 9022`

- 运行Linux命令：

```shell
ls          # 显示当前目录文件

uname -a    # 查看Linux内核版本

lscpu       # 查看CPU信息

nproc       # 查看CPU核心数

free -h     # 显示当前内存使用情况

top         # 查看当前进程、CPU和内存信息，按1和2切换

aid install aid-desktop # 重新安装或升级AidLux桌面

```

## 第六步：电脑给手机远程传输文件

电脑浏览器中输入`http://192.168.1.4:38080`

默认密码：`aidlux`

## 第七步：安装Jupyter Notebook

应用中心-Jupyter-安装

在命令行中输入
```shell
jupyter notebook --allow-root
```
在电脑浏览器中输入`http://192.168.1.4:10000`

## 第八步：玩转`例子中心`自带的例子

