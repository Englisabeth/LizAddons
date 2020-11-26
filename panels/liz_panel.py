import bpy

#LizOPS LMAO

class VIEW3D_PT_LizAddon(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_LizAddon"
    bl_label ="Liz Addons"
    bl_category = "LizAddons"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

############################################
# Draw center origin button
    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("view3d.orbit_select", text="Toggle orbit around selection")
        row = layout.row()
        row.operator("view3d.snap_selected_to_cursor", text="Snap Selected Object to Center")
        row = layout.row()
        row.operator("view3d.cursor_center", text="Center 3D Cursor to World Origin")
        row = layout.row()
        row.operator("view3d.lizhplp", text="Rename toggle high/low")
