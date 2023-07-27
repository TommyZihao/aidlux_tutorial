# 安装配置AidLux环境

同济子豪兄 2023-6-25 7-26

## 加入AidLux社群

添加AidLux小助手（微信号：AidLux_Me），回复“子豪兄”，免费加入答疑社群

## 官网

官网：https://aidlux.com

文档：https://docs.aidlux.com

## 第一步：安装APP

手机应用市场下载AidLux

手机和电脑连接同一个Wifi

## 第二步：配置APP

手机桌面-设置-应用管理

赋予AidLux各种系统权限，包括：媒体和文件、相机、麦克风、后台弹窗

手机-设置-关于手机-点击操作系统版本号多次，打开开发者模式

重启AidLux，按照提示完成配置

进入AidLux桌面，阅读`新手指引`

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
```

- 运行Linux命令，安装所需工具包

```shell
aid install aid-desktop                                                    # 重新安装或升级AidLux桌面

pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple   # pip换源至清华大学开源软件镜像站

/usr/bin/python3 -m pip install --upgrade pip                              # 更新pip

pip install numpy opencv-python matplotlib tqdm                            # 安装工具包

pip install torch torchvision                                              # 安装pytorch

pip install tensorflow                                                     # 安装tensorflow
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

查看端口号，比如10000

在电脑浏览器中输入`http://192.168.1.4:10000`

## 第八步：玩转`例子中心`自带的例子

- AidCode运行Python脚本

- examples里运行自带Demo：人脸、人体、手关键点检测、头发语义分割、人像语义分割、人脸检测、图像风格迁移、句子分类、古文断句

- 扩展阅读

Mediapipe Demo：https://mediapipe-studio.webapps.google.com/home

Mediapipe 3D目标检测：https://github.com/google/mediapipe/blob/master/docs/solutions/objectron.md

