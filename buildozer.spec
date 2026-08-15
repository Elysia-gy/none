# This .spec config file tells Buildozer an app's requirements for being built.
# 已适配「翁法罗斯」游戏项目 - 使用 Kivy + 远程 API

[app]

# (str) Title of your application
title = 翁法罗斯

# (str) Package name
package.name = omphalos

# (str) Package domain
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include. 包含了 ttc 字体的支持！
source.include_exts = py,png,jpg,kv,atlas,ttf,ttc,txt

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy,requests

# (list) Supported orientations
orientation = portrait

# OSX specific
osx.kivy_version = 2.2.0

#
# Android specific
#

# (bool) 自动接受 Android SDK 许可协议 (解决云端打包卡住的问题)
android.accept_sdk_license = True

# (str) 锁定一个稳定的 Android Build-Tools 版本 (避免下载 37.0.0 报错)
android.build_tools = 34.0.0

# (list) 游戏需要联网权限，必须加上！
android.permissions = android.permission.INTERNET

# (int) 目标 Android API
android.api = 33

# (int) 最低支持的安卓版本
android.minapi = 21

# (list) 构建的 CPU 架构
android.archs = arm64-v8a, armeabi-v7a

# (bool) 开启备份功能
android.allow_backup = True

# 是否显示为全屏，0 为不全屏（保留状态栏），1 为全屏
fullscreen = 0

# 入口文件
android.entrypoint = org.kivy.android.PythonActivity

# 调试版本输出为 apk
android.debug_artifact = apk

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2
