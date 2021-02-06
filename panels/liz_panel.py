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

        layout.label(text="Quicktoggle settings", icon="SETTINGS")
        row = layout.row()
        row.operator("view3d.orbit_select", text="Toggle orbit around selection", icon="CON_ROTLIKE")
        layout.label(text="Hardpoly Workflow", icon="MESH_CUBE")
        row = layout.row()
        row.operator("view3d.snap_selected_to_cursor", text="Snap Object to 3D Cursor", icon="BACK")
        row = layout.row()
        row.operator("view3d.cursor_center", text="Snap 3D Cursor to World Origin", icon="EMPTY_AXIS")
        row = layout.row()
        row.operator("view3d.lizhplp", text="Rename toggle high/low", icon="SORTALPHA")
        row = layout.row()
        row.operator("mesh.liznormal", text="Smooth & Weight Normals", icon="SURFACE_NSPHERE")
        row = layout.row()
        row.operator("export.lizhp", text="Move and export mesh back and forth", icon="EXPORT")