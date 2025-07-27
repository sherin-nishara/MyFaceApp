[app]

title = KivyCameraApp
package.name = kivycamera
package.domain = org.test
source.dir = .
version = 0.1
orientation = portrait

requirements = python3,kivy,opencv-python-headless

android.archs = armeabi-v7a, arm64-v8a

android.permissions = CAMERA

fullscreen = 1

# Leave this empty if unsure
# android.ndk =

[buildozer]

log_level = 2
warn_on_root = 1
