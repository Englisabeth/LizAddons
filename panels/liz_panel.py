import bpy

class VIEW3D_PT_LizAddon(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_LizAddon"
    bl_label ="Liz Addons"
    bl_category = "LizAddons"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

############################################
    def draw(self, context):
        layout = self.layout

        layout.label(text="Setting switches")
        row = layout.row()
        row.operator("view3d.orbit_select", text="Toggle orbit around selection")
        layout.label(text="Hardpoly Workflow")
        row = layout.row()
        row.operator("view3d.snap_selected_to_cursor", text="Snap Selected Object to 3D Cursor")
        row = layout.row()
        row.operator("view3d.cursor_center", text="Snap 3D Cursor to World Origin")
        row = layout.row()
        row.operator("view3d.lizhplp", text="Rename toggle high/low")
        layout = layout.row()
        layout.operator("mesh.liznormal", text="Smooth & Weight Normals")