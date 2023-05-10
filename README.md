# Blender3.x Reload Addon
## Above all:
- This Addon is changed by me from [hextant_reload_addon](https://github.com/hextantstudios/hextant_reload_addon) which doesn't work in Blender 3.x.
- And I add a `extra button` to reload the addon you wish.

## Install Addon：
-   Download the latest add-on build from [here](https://github.com/hjkggy007/hjkggy_reload_blender3_x_addon/releases/download/v1.0/hjkggy_reload_addon.v1.0.zip) or clone it using _git_ to your custom Blender `...\scripts\addons\` folder.
-   From Blender's Main Menu:
    -   _Edit / Preferences_
    -   Click the _Install_ button and select the downloaded zip file.
    -   Check the check-box next to the addon to activate it.
    -   **IMPORTANT: Configure the package name for the add-on you wish to quick reload.** (This is the add-on's directory name or single-file name.)
        -   Note that this does not have to be done to simply use the reload _all_ scripts hotkey.

## Use Addon：

It works when your addon is totally runable.(So you DON'T NEED to know  [hextant_reload_addon#use](https://github.com/hextantstudios/hextant_reload_addon#use))

You can use a method of this list below to reload your own addon:
- press  `Ctrl + Alt + R`  
- press the  `Button`  on top of 3d viewport( make sure you have entered your addon name in this addon)

You also can reload all the scripts by:
- press  `Ctrl + Alt+ Shift + R`  


## Note:
- If you add `new class` or `new Property` in your `register()` and `unregister()` function, it's likely to get wrong, in this case you can reopen Blender to make it work.






## 声明:
- 这个插件从 [hextant_reload_addon](https://github.com/hextantstudios/hextant_reload_addon) 处经我的修改，原插件不支持Blender 3.x使用。
- 在原来`快捷键`启动的方式下，我额外添加了 `按钮` 重载你的插件.

## 安装：
-   从 [这里](https://github.com/hjkggy007/hjkggy_reload_blender3_x_addon/releases/download/v1.0/hjkggy_reload_addon.v1.0.zip) 下载zip压缩包插件.
-   从 Blender 窗口下:
    -   `编辑` / `偏好设置...`/`插件`
    -  点击 `安装`并选择该zip文件，确定安装
    -   勾选插件前面的勾选框，激活插件.
    -   **注意: 填写你要重载的插件的名称** (插件文件夹的名字)
        -   要注意的是这里不填也不影响重载Blender全部脚本.

## 使用：

只要你的插件是可用的，它就会起作用.(所以你 不需要 知道 [hextant_reload_addon#use](https://github.com/hextantstudios/hextant_reload_addon#use))

使用下面的任意方式重载你的插件:
- 按  `Ctrl + Alt + R`  
- 点击  `按钮`  在3D视图的顶部( 确保你已经填写了插件名称)

你也可以重载Blender全部脚本，通过:
- 按  `Ctrl + Alt+ Shift + R`  


注意:
- 如果你添加了 新的` class` 或者 新的 ` Property` 在你的 `register()` 和 `unregister()` 方法里, 那就可能出错,这种情况下你需要重启你的Blender.
