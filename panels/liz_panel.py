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
        row = layout.row(align=True)
        row.operator("view3d.orbit_select", text="Toggle orbit around selection", icon="CON_ROTLIKE")
        row.operator("view3d.emu_numpad", text="Toggle Numpad Emulation", icon="VIEW_ORTHO")
        row = layout.row()
        layout.label(text="Snapping Shortcuts", icon="SNAP_ON")
        row = layout.row()
        row.label(text="Object", icon="OUTLINER_OB_MESH")
        row = layout.row(align=True)
        row.operator("view3d.snap_selected_to_cursor", text="Snap to 3D Cursor", icon="OUTLINER_OB_MESH")
        row.operator("view3d.liz3dorigin", text="Object Origin to 3D Cursor", icon="ORIENTATION_CURSOR")
        row = layout.row(align=True)
        row.operator("view3d.snap_cursor_to_selected", text="Object Origin", icon="LIGHTPROBE_SPHERE")
        row.operator("view3d.cursor_center", text="World Origin", icon="WORLD_DATA")
        row = layout.row(align=True)
    
        layout.label(text="Hardpoly Workflow", icon="MESH_CUBE")
        row = layout.row(align=True)
        row.operator("view3d.lizhplp", text="high/low", icon="SORTALPHA")
        row.operator("mesh.liznormal", text="~Auto Smooth~", icon="SURFACE_NSPHERE")

        row = layout.row()