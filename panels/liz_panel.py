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
        row = layout.row()

        row.operator("view3d.emu_numpad", text="Toggle Numpad Emulation", icon="VIEW_ORTHO")
        row = layout.row()

        layout.label(text="Snapping Shortcuts", icon="SNAP_ON")
        row = layout.row()

        row.label(text="Object to", icon="SNAP_ON")
        row.operator("view3d.snap_selected_to_cursor", text="Snap to 3D Cursor", icon="OUTLINER_OB_MESH")
        row.operator("view3d.liz3dorigin", text="Snap origin to 3D Cursor", icon="ORIENTATION_CURSOR")
        row = layout.row()
        row.label(text="3D cursor to", icon="SNAP_ON")
        row.operator("view3d.cursor_center", text="to World Origin", icon="WORLD_DATA")
        row.operator("view3d.snap_cursor_to_selected", text="to Object Origin", icon="FORWARD")
        row = layout.row()
    
        layout.label(text="Hardpoly Workflow", icon="MESH_CUBE")
        row = layout.row()

        row.operator("view3d.lizhplp", text="Rename toggle high/low", icon="SORTALPHA")
        row = layout.row()

        layout.operator("mesh.liznormal", text="Apply Auto Smooth @ 45 Degrees", icon="SURFACE_NSPHERE")
        row = layout.row()
