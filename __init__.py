# Copyright 2022 by Hextant Studios. https://HextantStudios.com
# This work is licensed under GNU General Public License Version 3.
# License: https://download.blender.org/release/GPL3-license.txt

bl_info = {
    "name": "Reload Add-on",
    "author": "hjkggy",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "script.reload_addon (Ctrl+Alt+R)",
    "description": "Reloads only the configured add-on (Ctrl+Alt+R) or " \
        "all scripts (Ctrl+Alt+Shift+R).",
    "doc_url": "https://github.com/hextantstudios/hextant_reload_addon",
    "category": "Development",
}

import bpy, importlib, sys
from bpy.types import Operator, AddonPreferences
from bpy.props import StringProperty

#
# Addon Preferences
#

# Preferences to select the addon package name, etc.
class ReloadAddonPreferences(AddonPreferences):
    bl_idname = __package__

    package_name: StringProperty(name="Add-on Package",
        description="The name of the add-on package that will be reload.")

    def draw(self, context):
        self.layout.use_property_split = True
        self.layout.prop(self, 'package_name')

#
#  Operators
#

# Reloads the add-on package specified in the operator or addon preferences.
class ReloadAddon(Operator):
    """Reload an activated add-on."""
    bl_idname = "script.reload_addon"
    bl_label = "Reload Add-on"

    # Allow overriding the package name from a key-binding or script call.
    package_name: StringProperty(name="Add-on Package")

    def execute(self, context):
        # Get the name of the addon package to reload.
        addon_prefs = context.preferences.addons[__package__].preferences
        package = self.package_name if self.package_name else addon_prefs.package_name
        
        if not package:
            self.report({'ERROR'}, "Reload Add-on: Package name not configured.")
            return {'FINISHED'}

        # Get the addon's module.wrongfunc!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        module = sys.modules.get(package)
        if not module:
            self.report({'ERROR'}, f"Reload Add-on: '{package}' not found or not activated.")
            return {'FINISHED'}
        
        # Call unregister() on the previously loaded addon.
        # Ensure that the new version of the addon is always reloaded by continuing.
        try:
            module.unregister()

            all_modules = sys.modules
            all_modules = dict(sorted(all_modules.items(),key= lambda x:x[0])) #sort them
            
            for k,v in all_modules.items():
                if (k == package):
                    continue
                if k.startswith(package):
                    del sys.modules[k]

            print(f"Un-registering: {package},clean the module dict space")
            
        except Exception:
            import traceback
            print("----------------------------------------------------------------------")
            traceback.print_exc()
            self.report({'ERROR'}, "Reload Add-on: 'unregister()' threw an exception! " +
                "Restart may be required.")
            print("----------------------------------------------------------------------")
            
        # Reload and register the addon.
        print(f"Reloading: {package}")
        importlib.reload(module)

        print(f"Registering: {package}")
        try:
            module.register()
            self.report({'INFO'}, f"Reloaded Add-on: {package}")
        except Exception:
            import traceback
            print("----------------------------------------------------------------------")
            traceback.print_exc()
            self.report({'ERROR'}, "Reload Add-on: 'register()' threw an exception! " +
                "Restart may be required.")
            print("----------------------------------------------------------------------")

        return {'FINISHED'}
def draw_reload_op(self,context):
    layout=self.layout
    addon_prefs = context.preferences.addons[__package__].preferences
    package_name = addon_prefs.package_name
    if package_name!='':
        layout.operator("script.reload_addon",text=package_name,icon="FILE_REFRESH")
#
# Registration
#

_classes = (ReloadAddonPreferences, ReloadAddon)
_register, _unregister = bpy.utils.register_classes_factory(_classes)
_keymaps = []

def register():
    _register()
    bpy.types.VIEW3D_MT_editor_menus.append(draw_reload_op)
    # Add a shortcut: Ctrl+Alt+R
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Window', space_type='EMPTY', region_type='WINDOW')
    
    kmi = km.keymap_items.new(ReloadAddon.bl_idname, 'R', 'PRESS', ctrl=True, alt=True)
    _keymaps.append((km, kmi))
    
    kmi = km.keymap_items.new(bpy.ops.script.reload.idname_py(), 'R', 'PRESS', ctrl=True, alt=True, shift=True)
    _keymaps.append((km, kmi))


def unregister():
    _unregister()

    # Remove shortcuts.
    for km, kmi in _keymaps: km.keymap_items.remove(kmi)
    _keymaps.clear()

