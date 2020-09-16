import bpy
from ..utils import liztools

class LizCenterCursor(bpy.types.Operator):
    bl_idname = "view3d.cursor_center"
    bl_label = "Simple operator"
    bl_description = "Center 3d cursor"

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_center()
        return {'FINISHED'}

class LizHPLPRenamer(bpy.types.Operator):
    bl_idname = "mesh.hplprenamer_liz"
    bl_label = "Simple operator"
    bl_description = "HP LP renamer"

    def execute(self, context):
        selection = []
        selection = liztools.active_get
        lp_s = '_low'
        hp_s = '_high'

        lp = s_lp_end
        
        hp = s_hp_end

        

        for obj in selection:
            if obj is lp:
                bpy.context.object.name = hp_rename
    
        for obj in selection:
            if obj is hp:
                bpy.context.object.name = lp_rename


        
        return {'FINISHED'}