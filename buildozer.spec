[app]
title = 翁法罗斯
package.name = omphalos
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,ttc,txt
version = 1.0
requirements = python3,kivy,requests
orientation = portrait
osx.kivy_version = 2.2.0

# ------------------ 关键 Android 配置 ------------------
# (必须开启，否则无法联网)
android.permissions = android.permission.INTERNET

# (核心修复：锁定 NDK 为 23b，绝对能绕过 r28c 的报错)
android.ndk = 25c
# (配合 NDK 23b 使用的 API 版本)
android.ndk_api = 21

# (自动同意协议 & 锁定 Build-Tools)
android.accept_sdk_license = True
android.build_tools = 34.0.0

# (安卓版本配置)
android.api = 33
android.minapi = 21

# (打包架构)
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
fullscreen = 0
android.entrypoint = org.kivy.android.PythonActivity
android.debug_artifact = apk

[buildozer]
log_level = 2
