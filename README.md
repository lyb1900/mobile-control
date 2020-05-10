# 手机控制智能助手简介
手机控制智能助手,通过电脑自动控制手机执行任务。通过扩展的方式支持各种APP的自动控制。
# 基本原理
这个开源手机群控助手软件是基于airtest开发的，通过adb和poco对手机进行控制。  
采用chatterbot对问答进行训练，完成自动聊天回复功能。  
使用百度ocr进行图片文字识别  
# 目前实现功能
- 设备管理
    - 支持同时管理多台手机。  
      连接好手机后，执行脚本可以自动发现手机，并管理
- 闲鱼自动回复买家咨询
    - 执行脚本后自动执行聊天线程，发现有买家咨询后自动复用。
# 请大家一起来完善
- 近期待认领任务
    - [ ] 将脚本打包成exe方便非开发人员使用
    - [ ] 支持闲鱼自动上下架

- 有兴趣一起完善此开源软件可加微信17388075023

# 目前没有exe版本，使用说明如下
## 环境准备 
安装python 3.6.5  
安装Airtest框架 pip install airtest  
安装poco框架 pip install pocoui  
安装开源聊天机器人ChatterBot pip install chatterbot  
安装百度OCR pip install baidu-aip  

## 运行
1.手机打开发者模式，安装上https://github.com/lyb1900/mobile-control/tree/master/install软件，接上电脑  
2.运行 xywork.py  
3.手机上提示都允许  
4.开始工作  

