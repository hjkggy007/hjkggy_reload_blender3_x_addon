# Blender Reload Blender3.x Addon
## Above all:
- This Addon is changed by me from [hextant_reload_addon](https://github.com/hextantstudios/hextant_reload_addon) which doesn't work in Blender 3.x.
- And I add a `extra button` to reload the addon you wish.

## Install Addon：
-   Download the latest add-on build from [here](https://github.com/hextantstudios/hextant_reload_addon/releases/latest/download/hextant_reload_addon.zip) or clone it using _git_ to your custom Blender `...\scripts\addons\` folder.
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
