# This .spec config file tells Buildozer an app's requirements for being built.
# 已适配「翁法罗斯」游戏项目 - 使用 Kivy + 远程 API

[app]

# (str) Title of your application
title = 翁法罗斯

# (str) Package name
package.name = omphalos

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (leave empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf,txt

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (leave empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (leave empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv, __pycache__

# (list) List of exclusions using pattern matching
# Do not prefix with './'
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# 注意：必须包含 kivy 和 requests，绝对不能写 tkinter 或 ollama
requirements = python3,kivy,requests

# (str) Custom source folders for requirements
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

# (list) List of services to declare
#services = NAME:ENTRYPOINT_TO_PY

#
# OSX Specific
#
osx.kivy_version = 2.2.0

#
# Android specific
#

fullscreen = 0

# (str) Adaptive icon of the application (optional)
#icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
#icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (list) Permissions
# 必须添加 INTERNET 权限，因为游戏需要请求远程 API
android.permissions = android.permission.INTERNET

# (list) features
#android.features = android.hardware.usb.host

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 23b

# (int) Android NDK API to use
#android.ndk_api = 21

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android SDK
# android.skip_update = False

# (bool) If True, then automatically accept SDK license agreements
# android.accept_sdk_license = False

# (str) Android entry point, default is ok for Kivy-based app
# 这里指定我们的 Kivy 入口文件（main_kivy.py）
android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
#android.activity_class_name = org.kivy.android.PythonActivity

# (str) Extra xml to write directly inside the <manifest> element of AndroidManifest.xml
#android.extra_manifest_xml = ./src/android/extra_manifest.xml

# (str) Extra xml to write directly inside the <manifest><application> tag
#android.extra_manifest_application_arguments = ./src/android/extra_manifest_application_arguments.xml

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (bool) If True, your application will be listed as a home app
# android.home_app = False

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project
#android.add_src =

# (list) Android AAR archives to add
#android.add_aars =

# (list) Put these files or directories in the apk assets directory.
#android.add_assets =

# (list) Put these files or directories in the apk res directory.
#android.add_resources =

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependencies'
# contains an 'androidx' package, or any package from Kotlin source.
# android.enable_androidx = True

# (list) add java compile options
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Gradle repositories to add
#android.add_gradle_repositories =

# (list) packaging options to add
#android.add_packaging_options =

# (list) Java classes to add as activities to the manifest.
#android.add_activities =

# (str) OUYA Console category. Should be one of GAME or APP
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (list) Copy these files to src/main/res/xml/
#android.res_xml = PATH_TO_FILE,

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (str) screenOrientation to set for the main activity.
#android.manifest.orientation = fullSensor

# (list) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_mips = libs/android-mips/*.so

# (bool) Indicate whether the screen should stay on
#android.wakelock = False

# (list) Android application meta-data to set (key=value format)
#android.meta_data =

# (list) Android library project to add
#android.library_references =

# (list) Android shared libraries which will be added to AndroidManifest.xml using <uses-library> tag
#android.uses_library =

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Android logcat only display log for activity's pid
#android.logcat_pid_only = False

# (str) Android additional adb arguments
#android.adb_args = -H host.docker.internal

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (int) overrides automatic versionCode computation
# android.numeric_version = 1

# (bool) enables Android auto backup feature
android.allow_backup = True

# (str) XML file for custom backup rules
# android.backup_rules =

# (str) If you need to insert variables into your AndroidManifest.xml file
# android.manifest_placeholders = [:]

# (bool) Skip byte compile for .py files
# android.no-byte-compile-python = False

# (str) The format used to package the app for release mode (aab or apk or aar).
# android.release_artifact = apk

# (str) The format used to package the app for debug mode (apk or aar).
# android.debug_artifact = apk

# (str) A display cutout is an area on some devices that extends into the display surface.
#android.display_cutout = never

#
# Python for android (p4a) specific
#

# (str) python-for-android URL to use for checkout
#p4a.url =

# (str) python-for-android fork to use
#p4a.fork = kivy

# (str) python-for-android branch to use
#p4a.branch = master

# (str) python-for-android specific commit to use
#p4a.commit = HEAD

# (str) python-for-android git clone directory
#p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes
#p4a.local_recipes =

# (str) Filename to the hook for p4a
#p4a.hook =

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2

# (int) port number to specify an explicit --port= p4a argument
#p4a.port =

# (bool) Use setup.py instead of ignoring it
#p4a.setup_py = false

# (str) extra command line arguments to pass when invoking pythonforandroid.toolchain
#p4a.extra_args =

#
# iOS specific
#
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.12.2
ios.codesign.allowed = false

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
# bin_dir = ./bin
# 自动接受 Android SDK 的许可协议（解决云端打包失败的根源）
android.accept_sdk_license = True
# 指定一个较稳定的 Build-Tools 版本（避免依赖冲突）
android.build_tools = 34.0.0
