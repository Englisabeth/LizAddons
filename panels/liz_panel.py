import bpy
from . misc.aliases import *

#LizOPS LMAO

class VIEW3D_PT_LizAddon(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_LizAddon"
    bl_label ="Liz Addons"
    bl_category = "LizAddons"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator(poopy)

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('', text="3D Cursor to World Origin")
    