[app]
title = 翁法罗斯
package.name = omphalos
package.domain = org.omphalos
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,ttc,txt
package.version = 1.0

requirements = python3,kivy,requests

orientation = portrait

# ------------------ Android 配置 ------------------
android.permissions = INTERNET

android.ndk = 25c
android.accept_sdk_license = True
android.build_tools = 34.0.0

android.api = 33
android.minapi = 21

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
fullscreen = 0
android.entrypoint = org.kivy.android.PythonActivity
android.debug_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
