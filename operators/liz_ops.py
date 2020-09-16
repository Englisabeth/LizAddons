import bpy

class LizCenterCursor(bpy.types.Operator):
    bl_idname = "liz.center.cursor"
    bl_label = "Simple operator"
    bl_description = "Center 3d cursor"

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_center()
        return {'FINISHED'}